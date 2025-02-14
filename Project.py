def readData():

    #Students and admins will be stored as lists of dictionaries
    stdList = []
    admList = []

    #The files, in which data is stored, will be opened for reading
    studentsFile = open("Students.txt", "r")
    adminsFile = open("Admins.txt", "r")

    #Will loop through both files and record the data
    for i in studentsFile:
        i = i.rstrip().split(' ')
        st1 = {"id":i[0], "Name":i[2]+" "+i[3], "Q1":float(i[5]) , "Q2":float(i[6]), "Q3":float(i[7])}
        stdList.append(st1)

    for i in adminsFile:
        i = i.rstrip().split(' ')
        st1 = {"User":i[0], "Password":i[2]}
        admList.append(st1)

    studentsFile.close()
    adminsFile.close()

    return (stdList, admList) #Return the lists



def info4All(studentsList): #Option 1: Display Grade Info for all students
    print("%-20s %-20s %-20s %-20s %-20s" %("Student ID", "Name", "Quiz-1", "Quiz-2", "Quiz-3")) #Print the header

    #Print all students info
    for student in studentsList:
        print("%-20s %-20s %-20s %-20s %-20s" %(student["id"], student["Name"], student["Q1"], student["Q2"], student["Q3"]))



def info4One(studentsList, ID): #Option 2: Display Grade Info for a particular student
    for student in studentsList: #Linear search
        if student["id"] == ID: #if the student exist, display his info and termenaite
            print("%-20s %-20s %-20s %-20s %-20s" %("Student ID", "Name", "Quiz-1", "Quiz-2", "Quiz-3"))
            print("%-20s %-20s %-20s %-20s %-20s" %(student["id"], student["Name"], student["Q1"], student["Q2"], student["Q3"]))
            return 0

    print("Error: Invalid student ID") #If the student does not exist >> Error message



def average(studentsList): #Option 3: Display assessments average for all students
    print("%-20s %-20s %-20s" %("Student ID", "Name", "Average")) #Print the header

    #Print all students info, note that the average is calculated inside the "print" function
    for student in studentsList:
        print("%-20s %-20s %.2f" %(student["id"], student["Name"], ((student["Q1"]+student["Q2"]+ student["Q3"])/3)))



def adminAccess(adminsList):

    accessAllowed = False #This var will help chack if the user is an admin

    user = input("admin user: ")
    password = input("admin password: ")

    for i in adminsList: #Linear search through the admin list to check if the given ID and password exist
        if i["User"] == user and i["Password"] == password: #if it exist it will grant access
            accessAllowed = True
            return accessAllowed
    print('The admin username or password are wrong!')

    return accessAllowed #If it does not exist access will not be granted



def modAsses(studentsList, ID):#Option 4: Modify a particular assessment grade for a particular student
    #Using Try-except for input validation
    try:
        quizNum = input("Enter quiz number to modify: ") #After taking the id, enter which assesment
        if not 0<int(quizNum)<4: #Input validation, if wrong the program will break and an error message will be shown
            raise IOError

        newGrade = float(input("Enter new quiz "+quizNum+" grade: ")) #The new grade given
        if not 0<=newGrade<=100: #Input validation, if wrong the program will break and an error message will be shown
            raise ValueError

        for student in studentsList: #Linear search for the student
            if student["id"] == ID: #If found, show the old information, change it then show the new info and termenaite
                print("Before grade modification: %s   %s  %.2f  %.2f  %.2f" %(student["id"], student["Name"], student["Q1"], student["Q2"], student["Q3"]))
                student["Q"+quizNum] = newGrade
                print("After grade modification: %s   %s  %.2f  %.2f  %.2f" %(student["id"], student["Name"], student["Q1"], student["Q2"], student["Q3"]))

                return 0

        raise ImportError #if the program was not termenaited (i.e. the student was not found) error message will be shown


    #Error messages
    except IOError:
        print("Error: Invalid quiz number")

    except ValueError:
        print("Error: grade must be between 0 ~ 100")

    except ImportError:
        print("Error: Student is not in the list")



def addStd(studentsList): #Option 5: Add a new Student
    newStd = {} #Student info will be defiend as dic.
    newstdList = list(studentsList)

    newID = input("Enter the new student's ID: ")

    #Check if the student already in the list or not
    exist = False
    for student in studentsList:
        if student["id"] == newID:
            exist = True

    if exist:
        print("Error: the student already exist in the list")

    else: #If it does not exist the info will be assigned
        newStd["id"] = newID
        newStd["Name"] = input("Enter the student's name: ")
        try:
            newStd["Q1"] = float(input("Enter the student's quiz 1 score: "))
            newStd["Q2"] = float(input("Enter the student's quiz 2 score: "))
            newStd["Q3"] = float(input("Enter the student's quiz 3 score: "))
        except ValueError:
            print("Input should be a number")

    newstdList.append(newStd)

    return newstdList


def rank(studentsList): #Option 6: Rank Students
    gradesAveragesList = [] #This list will be used for sorting

    #Add Average to the list and as a key in the student dic. and assign its value
    for student in studentsList:
        student["AVG"] = (student["Q1"]+student["Q2"]+student["Q3"])/3
        gradesAveragesList.append(student["AVG"])

    gradesAveragesList.sort()

    print("%-20s %-20s %-20s" %("Student ID", "Name", "Average")) #Print the header

    #This function will use the sorted list of averages from before to print the students' info in an ascending order
    for grade in gradesAveragesList:
        for student in studentsList:
            if student["AVG"] == grade:
                 print("%-20s %-20s %.2f" %(student["id"], student["Name"], student["AVG"]))



def addAdm(adminsList):
    newAdm = {} #Admin info will be defiend as dic.
    newAdmList = list(adminsList)

    newID = input("Enter the new admin's ID: ")

    #Check if the admin already in the list or not
    exist = False
    for admin in adminsList:
        if admin["User"] == newID:
            exist = True

    if exist:
        print("Error: the admin already exist in the list")

    else: #If not exist the info will be assigned
        newAdm["User"] = newID
        newAdm["Password"] = input("Enter the admin's password: ")

    newAdmList.append(newAdm)

    return newAdmList



def saveAndExit(stdList, admList):

    #Will open both files for witing both the old data(taken by the read function), and the new data (Added by user)

    stdFile = open("Students.txt","w")
    for student in stdList:
        line1 = student["id"]+ " ## "+ student["Name"]+ " ### "+ str(student["Q1"])+ " "+ str(student["Q2"])+ " "+ str(student["Q3"])
        stdFile.write("%s\n" % (line1))
    stdFile.close()

    admFile = open("Admins.txt","w")
    for admin in admList:
        line1 = admin["User"]+" :: "+admin["Password"]
        admFile.write("%s\n" % (line1))
    admFile.close()

    print("Changes saved")

def main():

    stdList, admList = readData()

    menu = "1. Display Grade Info for all students\n2. Display Grade Info for a particular student\n3. Display assessments average for all students\n4. Modify a particular assessment grade for a particular student\n5. Add a new Student\n6. Rank students\n7. Add a new admin\n8. Save and Exit"
    print(menu)
    option = input("Please select your choice:")

    while option != "8":
        print()
        if option == "1":
            info4All(stdList)

        elif option == "2":
            info4One(stdList, input("Please enter the student ID: "))

        elif option == "3":
            average(stdList)

        elif option == "4":
            if adminAccess(admList):
                modAsses(stdList, input("Please enter the student ID: "))

        elif option == "5":
            if adminAccess(admList):
                stdList = list(addStd(stdList)) #The new list (with the new student) will replace the old one

        elif option == "6":
            rank(stdList)

        elif option == "7":
            if adminAccess(admList):
                admList = list(addAdm(admList)) #The new list (with the new admin) will replace the old one

        else:
            print("Error: Wrong input, please enter a number from 1 ~ 8")

        print()
        while input("Press Enter key to continue..."):
            print()
            #This will wait for the user to press enter, anything else given will repeat the requset
        print("\n\n")
        print(menu)
        option = input("Please select your choice:")

    saveAndExit(stdList, admList)

main()