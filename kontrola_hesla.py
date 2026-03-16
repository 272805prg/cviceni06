def analyze_password(
        password,
        min_length=8,
        require_digit=True,
        require_upper=True,
        require_symbol=False,
        banned_words=None
):
    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    missing_rules = []
    total_rules = 0
    passed_rules = 0

    total_rules += 1
    if len(password) >= min_length:
        passed_rules += 1
    else:
        missing_rules.append("min_length")

    if require_digit:
        total_rules += 1
        if any(char.isdigit() for char in password):
            passed_rules += 1
        else:
            missing_rules.append("digit")

    if require_upper:
        total_rules += 1
        if any(char.isupper() for char in password):
            passed_rules += 1
        else:
            missing_rules.append("upper")

    if require_symbol:
        total_rules += 1
        if any(char in symbols for char in password):
            passed_rules += 1
        else:
            missing_rules.append("symbol")

    total_rules += 1
    if not any(word.lower() in password.lower() for word in banned_words):
        passed_rules += 1
    else:
        missing_rules.append("banned_word")

    is_strong = len(missing_rules) == 0
    score_percent = int((passed_rules / total_rules) * 100)

    return is_strong, score_percent, missing_rules



print("Test:")
print(analyze_password("TajneHeslo1", 10, True, True, False, ["admin", "root"]))

