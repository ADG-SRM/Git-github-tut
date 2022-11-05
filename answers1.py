# 1. Check Even or odd
def checkEvenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 2. Check Prime number
def isPrime(num):
    if num != 2:
        if num % 2 != 0 and num > 2:
            print("Prime number")
        else:
            print("Not a prime number")
    else:
        print("Prime number")


# 3. Check for automorphic 2 digit number
def isAutomorphic(num):
    if (num * num) % 10 == num % 10:
        print("Automorphic number")
    else:
        print("Not Automorphic number")


# 4. Print all the characters in a string in descending order of their occurence
def printInReverse(string):
    print(string[::-1])


# 5. Calculator
def calculator():
    print("The answer is: ", eval(input("Enter an experssion: ")))
