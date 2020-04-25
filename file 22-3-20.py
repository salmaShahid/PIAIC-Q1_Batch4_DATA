# #how to find folder path
# import  os
# # print(os.getcwd()) #to get folder current
#
# # folder_name = input("Enter folder name") #folder
# # os.mkdir(folder_name) #new folder create
#
# # folder_name = input("Enter folder path") #folder
# # #path have multiple folder
# # os.makedirs(folder_name)
# # os.makedirs(r'C:\Users\LeNoVo T430\PycharmProjects\piaic\virtualClass\salma\piaic') #to create nested folder
# #
# #
#
# user = input("enter name ") #path to del folder
# # os.remove(user) #file del
# # os.removedirs(user) #folder del
#
# # os.rename('data.txt','newdata.txt') #for rename (old,new)
# # os.rename('piaic','virtaulClassPiaic') # for rename folder
#
#
# try:
#
#     a = float(input("enter 1 name"))
#     b = float(input("enter 2 name"))
#     print(a + b) #if user enter wrong one
#
#
#     with open('newdatas.txt') as file:
#         c =file.read()
#         print(c)
#
# #error handling
# except ValueError:
#     print("cannot print")
#
# # print("this code will run normally")
#
# except FileNotFoundError:
#     print("file not found, plz add it")
#


#custom exception
class MyCustomException(Exception):
    pass

try:
    c_num = int(input("enter num"))
    if c_num> 80:
        raise MyCustomException() #if we want own generate exception

except MyCustomException:
    print("handle by our own handler")

