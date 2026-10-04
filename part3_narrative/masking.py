def alias_for(reseller_id):
    number = reseller_id[-2:]
    return f"ALIAS-{number}"


def assert_no_raw_names_leak(text, raw_names):
    for name in raw_names:
        if name in text:
            return False

    return True