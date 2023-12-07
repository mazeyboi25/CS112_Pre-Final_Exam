print("CS112: Computer Programming 1 - PRE-FINAL EXAM")
print("Created by: Ochavillo, Kyle Benedict T.")
print("----------------------------------------------")
def optimus_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def sentinel_prime(start, end):
    optimum = [num for num in range(start, end + 1) if optimus_prime(num)]
    return optimum

while True:
    sugod = int(input("Enter a number (enter 0 to terminate): "))

    if sugod == 0:
        print("Program terminated.")
        break

    if sugod < 0:
        print("Enter a non-negative number.")
        continue

    while True:
        undang = int(input("Enter a number: "))
        if undang > sugod:
            break
        print("Enter a number greater than", sugod)

    optimum = sentinel_prime(sugod, undang)

    print(f"Prime numbers between {sugod} and {undang} are: ", end="")
    for i in range(len(optimum)):
        print(optimum[i], end="")
        if i < len(optimum) - 1:
            print(", ", end="")
    print()
