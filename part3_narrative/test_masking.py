from part3_narrative.masking import alias_for, assert_no_raw_names_leak


print("RS019 ->", alias_for("RS019"))
print("RS006 ->", alias_for("RS006"))

raw_names = [
    "Mumbai Reseller 1",
    "Lucknow Reseller 6"
]

safe_text = "ALIAS-19 and ALIAS-06 were reviewed."

assert assert_no_raw_names_leak(safe_text, raw_names) is True

unsafe_text = "Mumbai Reseller 1 was reviewed."

assert assert_no_raw_names_leak(unsafe_text, raw_names) is False

print("Part 3 masking test passed.")