def grep(pattern, flags, files):
    ignore_case = "-i" in flags
    invert = "-v" in flags
    line_number = "-n" in flags
    file_only = "-l" in flags
    whole_line = "-x" in flags

    pattern_cmp = pattern.lower() if ignore_case else pattern

    output = []

    for file in files:
        matches = []
        found = False

        with open(file) as f:
            for i, line in enumerate(f, start=1):
                text = line.rstrip("\n")
                check = text.lower() if ignore_case else text

                if whole_line:
                    matched = (check == pattern_cmp)
                else:
                    matched = (pattern_cmp in check)

                if invert:
                    matched = not matched

                if matched:
                    found = True
                    if not file_only:
                        prefix = ""

                        if len(files) > 1:
                            prefix += file + ":"

                        if line_number:
                            prefix += f"{i}:"

                        output.append(prefix + text + "\n")

        if file_only and found:
            output.append(file + "\n")

    return "".join(output)