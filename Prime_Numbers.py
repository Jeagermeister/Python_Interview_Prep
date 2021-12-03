# Name: Brian D. Yegerlehner
# Date: December 3rd, 2021
# Title Finding the Prime Numbers

#funtion to find the prime numbers
def find_prime():
    
    for i in num_list:
        if i <= 1:
            pass
        else:
            if((i == 2) or (i == 3)):
                prime_list.append(i)
            elif (((i % 2) == 1) and ((i % 3) == 1)):
                prime_list.append(i)
                
    #prints final prime number list
    print(str(prime_list))

num_list = [-24, 199, 7, 0, -5, 21, -3, 3, 2, 231, 101]

prime_list = []

#calls function
find_prime()