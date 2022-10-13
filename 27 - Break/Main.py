# Break
number = 0
while number < 5:
    number += 1
    print(f"Number - {number}")

    if number == 3:
        print("Stop")
        break

print(f"Finish Number - {number}")
