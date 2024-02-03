has_good_credit = True
has_good_income = True
has_criminal_record = False

if has_good_income and has_good_credit:
    print("Eligible for loan")

if has_good_income or has_good_credit:
    print("can buy things")

if has_good_income and not has_criminal_record:
    print("Not a criminal")