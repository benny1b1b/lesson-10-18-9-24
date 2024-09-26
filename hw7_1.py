positive: int = 0
negative: int = 0
division_by_7: int = 0
zero: int = 0
last_positive: int = None
last_negative: int = None
SENTINEL: int = -999

for _ in range(1, 11):
    num: int = int(input("enter number: "))
    if num <= -1000 or num >= 1000:
        continue

    if num == SENTINEL:
        break

    if num > 0:
        positive += 1
        last_positive = num

    if num % 7 == 0:

        division_by_7 += 1

    if num < 0:
        negative += 1
        last_negative = num

    if num == 0:
        zero += 1

else:
    print(f"the positive number appeared {positive} times")
    print(f"the negative number appeared {negative} times")
    print(f"zero appeared {zero} times")
    print(f"the number division by 7 appeared {division_by_7} times")
    print(f"last positive number is: {last_positive}")
    print(f"last negative number is: {last_negative}")