# Name: Brian D. Yegerlehner
# Date: December 3rd, 2021
# Title: Removing Duplicates from an array

# begin here
num_list = [1, 3, 0, 1, 9, -1, 9, 8, 7]
new_list = []

for i in num_list:
    if i not in new_list:
        new_list.append(i)
        
print(str(num_list))
print(str(new_list))