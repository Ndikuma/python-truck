from datetime import datetime, timedelta

def is_workday(dt):
    return dt.weekday() < 5

def get_first_workday(year, month):
    dt = datetime(year, month, 1, 8, 0)
    while not is_workday(dt):
        dt += timedelta(days=1)
    return dt

def get_last_workday(year, month):
    if month == 12:
        next_month_start = datetime(year + 1, 1, 1)
    else:
        next_month_start = datetime(year, month + 1, 1)
        
    dt = next_month_start - timedelta(days=1)
    dt = dt.replace(hour=8, minute=0, second=0, microsecond=0)
    while not is_workday(dt):
        dt -= timedelta(days=1)
    return dt

def delivery_date(start, description: str):
    # 1. Handle Input Type (Convert ISO string to datetime if necessary)
    is_input_str = isinstance(start, str)
    if is_input_str:
        start = datetime.fromisoformat(start)

    result_dt = None

    # --- FIXED DESCRIPTIONS ---
    if description == "NOW":
        result_dt = start + timedelta(hours=2)
        
    elif description == "ASAP":
        if start.hour < 13:
            result_dt = start.replace(hour=17, minute=0, second=0, microsecond=0)
        else:
            tomorrow = start + timedelta(days=1)
            result_dt = tomorrow.replace(hour=13, minute=0, second=0, microsecond=0)
            
    elif description == "EOW":
        if start.weekday() in [0, 1, 2]:
            days_until_friday = 4 - start.weekday()
            friday = start + timedelta(days=days_until_friday)
            result_dt = friday.replace(hour=17, minute=0, second=0, microsecond=0)
        else:
            days_until_sunday = 6 - start.weekday()
            sunday = start + timedelta(days=days_until_sunday)
            result_dt = sunday.replace(hour=20, minute=0, second=0, microsecond=0)

    # --- VARIABLE DESCRIPTIONS ---
    elif description.endswith("M"):
        target_month = int(description[:-1])
        if start.month < target_month:
            result_dt = get_first_workday(start.year, target_month)
        else:
            result_dt = get_first_workday(start.year + 1, target_month)

    elif description.startswith("Q"):
        target_quarter = int(description[1:])
        last_month_of_quarter = target_quarter * 3
        current_quarter = (start.month - 1) // 3 + 1
        
        if current_quarter <= target_quarter:
            result_dt = get_last_workday(start.year, last_month_of_quarter)
        else:
            result_dt = get_last_workday(start.year + 1, last_month_of_quarter)
    else:
        raise ValueError(f"Unknown description format: {description}")

    # 2. Output Format (Match the input type)
    return result_dt.isoformat() if is_input_str else result_dt