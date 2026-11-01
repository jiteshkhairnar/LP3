print("1. Non-Recursive (Iterative)")
print("2. Recursive")

choice = int(input("Enter your choice (1 or 2): "))
n = int(input("Enter the number of terms: "))

if choice == 1:
    a = 0
    b=1
    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

elif choice == 2:
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("Fibonacci Series:")

    for i in range(n):
        print(fibonacci(i), end=" ")

else:
    print("Invalid choice!")