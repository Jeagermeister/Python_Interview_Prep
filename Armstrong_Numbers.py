# Name: Brian Yegerlehner
# Date: December 3rd, 2021
# Title: Finding Armstrong Numbers

#Function to analyze each number to check for THREE-DIGITS
def streamline():
    for i in num_list:
        if i > 99:
            #continue
            pass
        else:
            num_list.remove(i)
            
    #prints updated number list
    print("Updated List: " + str(num_list))
            
#Function to check each value if it is Armstrong Number\
def isArm():
    #for-loop
    for j in num_list:
        
        #converts integer into array of integers
        j_list = [int(x) for x in str(j)]
        
        #value to check against original number
        check_val = 0
        
        for x in j_list:
            check_val = check_val + x**3
            
        #checks if check_val is equal to j
        if(check_val == j):
            arm_list.append(j)
        else:
            pass
            
            
    print("Armstrong Number(s): " + str(arm_list))

        
    
#Number List
num_list = [12, 1987, 0, 839, 341, 244, 153, 769, 371]
#Armstrong Number List
arm_list = []
   
#calls function
streamline()

#calls check function
isArm()