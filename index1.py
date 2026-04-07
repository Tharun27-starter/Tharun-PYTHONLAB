
usn = input("Enter USN: ")
name = input("Enter Name: ")
dob = input("Enter Date of Birth: ")


marks = []
for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5


print("\n--- Student Details ---")
print("USN:", usn)
print("Name:", name)
print("DOB:", dob)
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
