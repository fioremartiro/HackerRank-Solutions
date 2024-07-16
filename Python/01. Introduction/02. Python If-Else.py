# Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

if __name__ == '__main__':
    n = int(input().strip())
    
    if (n % 2) != 0:
        print("Weird")
    elif (n % 2) == 0 and n in range(2, 6):
        print("Not Weird")
    elif (n % 2) == 0 and n in range(6, 21):
        print("Weird")
    elif (n % 2) == 0 and n > 20:
        print("Not Weird")
    else:
        print("None of the above")
