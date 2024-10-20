# print all prime numbers between 1 and 250

lower = int(input("Enter lower number"))
upper = int(int("Enter upper number"))

file = open("results.txt", 'w')
file.write("The prime numbers between" + str(lower) + "and" + str(upper) + "are" + "\n")

for num in range (lower, upper + 1):
    # All prime numbers are greater than zero
    if num > 1:
        for i in range(2, num):
            # If num is divisible by any number between 2 and num-1, it is not prime
            if (num % i) == 0:
                break
        else:
            file.write(str(num) + "\n")
print ("The prime numbers are displayed in the results.txt file")
file.close()