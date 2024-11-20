print("A - Add Record")
print("B - View Records")
print("C - Clear All Records")
print("D - Count All Records")
print("E - Exit")

choice = ""

while choice.upper() != 'D':
    choice = input("ENTER SELECTION [A, B, C, or D]: ")
    if choice.upper() == 'A':
        print("Add Record")
        addRec()
    elif choice.upper() == 'B':
        print("View Records")
        viewRec()
    elif choice.upper() == 'C':
        print("Clear All Records")
        clearRec()
    elif choice.upper() == 'D':
        print("Count All Records")
        countRec()
    elif choice.upper() == 'E':
        print("Thank you!")

def viewRec():
    file = open(filename, 'r')
    with open(filename, 'r') as read_file:
        print(read_file.read())
    read_file.close() 


