# Armstrong number
# Sum of cubes of digits = number
print("Enter the number you wanna check")
n = input()
temp = n
armstrong = 0
while n >= 0:
    armstrong += n%10 ** 3
    n /= 10

if armstrong == temp:
    print('Armstrong Number')
