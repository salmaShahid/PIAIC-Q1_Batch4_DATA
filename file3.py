
#dic bnaye then list se access ki
students = []
student1={
    "name" : "salma",
    "class": "bscs 3b",
    "rollno" : 81
}

student2={
    "name" : "Aqsa",
    "class": "bscs 3b",
    "rollno" : 95
}
students.append(student1)
students.append(student2)
# print(students)

#to access multiple item in list
for student in students:
    print(student["class"])

#acess student1 data from list
index = 0
for student in students:
    if index == 1:
        print(student['class'])
    index=index+1

#take 2 option for user 1: for add user, 2: for display all user (mail,city, name),3: search if take user name and find it from dic and display, i
def getuser():
    name = input("enter name")
    email = input("enter email")
    city = input("enter city")

    dict= {
        'name':name,
        'email' : email,
        'city' : city
    }

    return dict

std = []
while True:
    print("1 : add user")
    print("2 : display all user")
    print("3 : search user")
    print("4 : end")

    choice = int(input("enter what operation you choose"))
    if choice == 1:
        my_user = getuser()
        std.append(my_user)
    elif choice == 2:
        print(std)
    elif choice == 3:
        s = input("enter key  you want to search from dictionary ")
        for i in std: #list with loop if multi entries
            if i['name'] == s:
                print(i['name'])
                break
    elif choice == 4:
        break


#4 is for edit user (key values se edit)
#5 is for del user (del,pop,remove)