def check_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check_number() -> None:
    num = int(input("Enter a number between 1 and 20: "))
    while num < 1 or num > 20:
        num = int(input("The number should be between 1 and 20: "))

    if check_prime(num):
        print(f"{num} is a prime number")

    if num % 2 == 0:
        print(f"{num} is an even number")

    if num % 2 != 0:
        print(f"{num} is an odd number")


check_number()
