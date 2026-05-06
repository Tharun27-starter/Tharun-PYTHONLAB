import os.path
import sys


fname = input("Enter the filename to sort: ")


if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)


infile = open(fname, "r")


lines = infile.readlines()


infile.close()


lineList = []


for line in lines:
    lineList.append(line.strip())

# Sort the list
lineList.sort()


print("\nSorted Lines:")
for line in lineList:
    print(line)


outfile = open("sorted_" + fname, "w")

for line in lineList:
    outfile.write(line + "\n")

outfile.close()

print("\nSorted content written to file:", "sorted_" + fname)