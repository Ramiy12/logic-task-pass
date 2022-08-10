# Q1/write a method that will remove any given character from a string ?
# the answer is by using using replace()
# for example

s = 'rami'

print(s.replace('r', ''))
# Q2/ WRITE A PROGRAM TO FIND ALL PRIME NUMBERS UP TO A GIVEN RANGE OF NUMBERS?
# the answer to find the prime numbers which they are greater than 1  and has no other factors except 1 and the number itself .
# for a example
first = 9
last = 20

print("Prime numbers between", first, "and", last, "are:")

for num in range(first, last + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Q3/ WRITE A FUNCTION THAT COUNT HOW MANY THE GIVEN CHARACTER REPEATED IN A GIVEN STRING ?
# the answer is by first Count variable than we have to check the character in string and also i used the for loop here.
# for example


def count(a, b):

    res = 0

    for i in range(len(a)):

        # Checking character in string
        if (a[i] == b):
            res = res + 1
    return res


str = "rami farqad yousif "
b = 'r'
print(count(str, b))
