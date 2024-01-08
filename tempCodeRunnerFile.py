#-->File handling

# # Writing a file
# file = open("Testing.txt","w")
# # w stands for writing mode and will create a file if not exist
# file.write("Hello World \nHello Nepal \nHello Sir")
# #writes into a new file
# file.close()
#     #When a file is opened in write mode, exisiting the content is deleted

# # Reading a file
# file = open("Testing.txt","r")
# # r stands for reading mode
# print(file.read(2))
# # argument takes 1 character as 1 byte and prints it
# print(file.read())
# # after 2 characters are printed it prints the remaining characters


# # Reading each line in a file
# for line in file:
#     print(line)
#     #OR we can use file.readlines() function
# file.close()

# #Example:
# file1 = open("Testing.txt","r")
# n = int(input())
# results = file1.readlines()
# #reads all lines from file
# print(results[n])
# #prints only the line given as argument
