name = "AbUbaKKar"

upper_count = 0

lower_count = 0

for ch in name:

    if ch == ch.upper():
        upper_count = upper_count + 1
    elif ch == ch.lower():
        lower_count = lower_count + 1

print(f"Upper Case In This Variable = {upper_count}")
print(f"Lower Case In This VAribale = {lower_count}")