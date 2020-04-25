# #we dont need first parameter it generte tuple format so that no one change it
# def sum(*b):
#     # print(a) #first num a
#     print(b) #optional argumant
#     # return res
#     total = 0
#     # total += a
#     for items in b: #5,6,7 aik aik krke item nikle ga or total me jata jaye ga or add hojaye ga
#         total +=items
#     return total
#
# print(sum(3,5,6,7,1,1,3,2,4))
#
# #if we take user input
# data = input("enter num")
# data = "1,2,3,4,5,6"
#
# c = data.split(",") #set it in array
# t = 0
# for i in c:
#     t +=i
#
# print(t)
#
#



#
# #set default value of paramter
#
# def sum(a,b=0):
#     print(a+b)
#
# res = sum(2,5)
# print(res)
#



#T1:  user ne apni mrzi se num diye than uska commulative pass krna hay
#pehla num uthaya usme dosra add krdiya func user se input le or res me save krliya

#from geek for geeks
# def optional(lists):
#     list = sum(lists)
#     return list

# lists = [10,23,50]
#print(optional(lists))

# p = []
#
# q = 0
# while True:
#     s = int(input("enter num"))
#     a = p.append(s)
#
#     q +=1
def get(*n):
    t1 = n[1]+n[2]
    t2  = t1+n[3]
    t3 = t2+n[4]
    t4 = t3 +n[5]
    print(n[1],t1,t2,t3,t4)

print(get(5,10,2,4,6,8))

# lists = n

# print(optional(lists))



#[20,29,27] multiple muliple lliye or usse poocha knse digit k num chahiye



# def getnum():
#     s = int(input("enter num"))
#     d = int(input("enter num"))
#     p = int(input("enter num"))
#
#     dict= {
#         '1':s,
#         '2' : d,
#         '3' : p
#     }
#
#     return dict
#
# std = []
# while True:
#     print("1 : get num")
#     print("2 : display all num")
#     print("3 : search num")
#     print("4 : end")
#
#     choice = int(input("enter what operation you choose"))
#     if choice == 1:
#         my_num = getnum()
#         std.append(my_num)
#     elif choice == 2:
#         print(std)
#     elif choice == 3:
#         s = input("enter key  you want to search from dictionary ")
#         for i in std: #list with loop if multi entries
#             if i['1'] == s:
#                 print(i['num1'])
#                 break
#     elif choice == 4:
#         break
# l = []
# h = getuser()
# data = l.append(h)
# print(data)
# f = int(input("which num you want to get"))
# if data['num2'] == f:
#     print(data['num2'])



# #seconfd part  ["20","30","27"] serach
# list = []
# d = input("enter data")
# match = int(input("enter match character"))
# l = d.split(",") #split the number
# list.append(l)
# # print(list)
# for i in list: #i[0] if it is equal to 2
#     if i[0] == match: #if 2 match with match character
#         print(i[0])



#keyword argumnet
def printStudent(**nums): #keyword optional argument
    print(nums['b'])

printStudent(a="apple",b="banana",c ="cat")
