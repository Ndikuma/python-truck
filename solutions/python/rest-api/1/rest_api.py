import json

class RestAPI:
    def __init__(self, database=None):
        self.users = {}
        if database and "users" in database:
            for user in database["users"]:
                self.users[user["name"]] = {
                    "owes": user["owes"],
                    "owed_by": user["owed_by"]
                }

    def _get_user_object(self, name):
        data = self.users[name]
        owes = data["owes"]
        owed_by = data["owed_by"]
        balance = sum(owed_by.values()) - sum(owes.values())
        return {
            "name": name,
            "owes": dict(sorted(owes.items())),
            "owed_by": dict(sorted(owed_by.items())),
            "balance": balance
        }

    def get(self, url, payload=None):
        if url == "/users":
            data = json.loads(payload) if payload else {}
            requested = data.get("users")
            if requested:
                user_list = [self._get_user_object(n) for n in sorted(requested)]
            else:
                user_list = [self._get_user_object(n) for n in sorted(self.users.keys())]
            return json.dumps({"users": user_list})

    def post(self, url, payload=None):
        data = json.loads(payload)
        if url == "/add":
            name = data["user"]
            self.users[name] = {"owes": {}, "owed_by": {}}
            return json.dumps(self._get_user_object(name))
            
        elif url == "/iou":
            lender, borrower = data["lender"], data["borrower"]
            amount = float(data["amount"])
            
            # Logic: If A owes B 3.0 and lends B 2.0, A now owes B 1.0.
            # We calculate net flow between the two.
            # 1. Update Lender (Adam)
            # Remove from 'owes' if he owes borrower, else add to 'owed_by'
            if borrower in self.users[lender]["owes"]:
                old_debt = self.users[lender]["owes"][borrower]
                if old_debt > amount:
                    self.users[lender]["owes"][borrower] -= amount
                elif old_debt < amount:
                    self.users[lender]["owes"].pop(borrower)
                    self.users[lender]["owed_by"][borrower] = amount - old_debt
                else:
                    self.users[lender]["owes"].pop(borrower)
            else:
                self.users[lender]["owed_by"][borrower] = self.users[lender]["owed_by"].get(borrower, 0.0) + amount

            # 2. Update Borrower (Bob)
            # Mirror the update for the other side
            if lender in self.users[borrower]["owed_by"]:
                old_credit = self.users[borrower]["owed_by"][lender]
                if old_credit > amount:
                    self.users[borrower]["owed_by"][lender] -= amount
                elif old_credit < amount:
                    self.users[borrower]["owed_by"].pop(lender)
                    self.users[borrower]["owes"][lender] = amount - old_credit
                else:
                    self.users[borrower]["owed_by"].pop(lender)
            else:
                self.users[borrower]["owes"][lender] = self.users[borrower]["owes"].get(lender, 0.0) + amount

            result = sorted([self._get_user_object(lender), self._get_user_object(borrower)], key=lambda x: x["name"])
            return json.dumps({"users": result})