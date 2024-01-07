count = 0
count_limit = 3
secret_number = 5

while count<count_limit:
    if secret_number == int(input("guess: ")):
        print("congrats")
        break
    else:
        print("try again")
    count +=1
else:
    print("sorry you failed")
