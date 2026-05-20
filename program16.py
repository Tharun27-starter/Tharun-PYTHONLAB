
name = input(" Enter Student name : ")
dob = input(" Enter DOB : ")
reg_no = input(" Enter register number : ")
dept = input(" Enter department : ")


m1 = int(input(" Enter marks for Subject 1: "))
m2 = int(input(" Enter marks for Subject 2: "))
m3 = int(input(" Enter marks for Subject 3: "))
m4 = int(input(" Enter marks for Subject 4: "))
m5 = int(input(" Enter marks for Subject 5: "))


total = m1 + m2 + m3 + m4 + m5
percentage = total / 5


print("\n - - - Student details - - - ")
print(" Name : ", name)
print(" DOB : ", dob)
print(" Register NO : ", reg_no)
print(" Department : ", dept)
print(" Total marks : ", total)
print(" Percentage : ", percentage)


if percentage >= 75:
    print(" Result : Distinction ")
elif percentage >= 60:
    print(" Result : First Class ")
elif percentage >= 50:
    print(" Result : Second class ")
else:
    print(" Result : Fail ")