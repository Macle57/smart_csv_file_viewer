# from __future__ import annotations                    #uncomment this line if you're between 3.7-3.10
from csv_file_func import *

print("You are now viewing the private database which keeps track of all the employees")
print("This program is going to help you navigate and work with this database")
print("x-------------------------------------------x\n")


# Used to get int input and filter out everything else
def getint(txt: str) -> int:
    while True:
        inte = ''.join(i for i in input(txt) if i.isdigit())
        if inte == '':
            print('Please enter valid integers i.e. 1 2 3 etc.')
        else:
            return int(inte)


# Used to get date in correct format and correct the mistakes of wrong format.
def getdate(DOB=True):
    global dob
    while True:
        if DOB:
            print("Enter employee's date of birth (MM/DD/YYYY):   ", end='')
        else:
            print("Enter employee's date of joining (MM/DD/YYYY):   ", end='')
        truedate = ''.join(i for i in input(':\t') if i == '/' or i.isdigit())
        if truedate == '0':
            return truedate
        try:
            date = managedate(truedate)
        except:
            print("Please ensure to use '/' between dates.")
            continue
        if len(truedate) != 10:
            print('Please ensure to add a 0 before a single digit entry, for eg: 11/03/2005')
        elif date[2] > 31:
            print('Please enter the date correctly, input the DOB again.')
        elif date[1] > 12:
            print('Please enter the month correctly, input the DOB again.')
        elif DOB:
            if 2022 - date[0] < 18:
                print('Please ensure employee is 18+')
            elif 2022 - date[0] > 60:
                print("Please ensure employee is less then 60 years old due to company's policy")
            else:
                dob = date
                return truedate
        else:
            try:
                age = date[0] - dob[0]
            except:
                age = date[0] - 1975
            if 2022 - date[0] < 0:
                print('Please enter a date in past.')
            elif 61 < age or age < 17:
                print('Please ensure employee is in between 18-60 years of age.')
            else:
                return truedate


# Used to get sex inputted and account for many possible answers.
def getsex():
    while True:
        sex = input("Enter employee's sex (M/F/O):   ").upper()
        i: str
        sex = ''.join(i for i in sex if not i.isspace() and i.isalpha() or i == '0')
        if sex == '0':
            return sex
        if sex in ['MALE', 'M', 'MAN', 'BOY']:
            return 'M'
        elif sex in ['FEMALE', 'F', 'WOMAN', 'GIRL']:
            return 'F'
        elif sex in ['O', 'OTHER', 'OTHERS']:
            return 'O'
        else:
            print('Please enter a valid sex and check your spellings.')


# Used to get the employee id in the correct format
def getemp():
    while True:
        emp = getint("Enter employee id:\t")
        if len(str(emp)) < 4 and emp != 0:
            print("Please enter employee id of atleast 4 numeric digits")
        else:
            return emp


# Used to get a record inputted from the user.
def getinput() -> list:
    while True:
        inp = [getemp(),  # Employee ID
               input("Enter employee's full Name:   "),  # Employee Name
               getdate(),  # DOB
               getsex(),  # Sex
               input("Enter employee's email id:   "),  # Email id
               input("Enter employee's address:   "),  # Address
               getint("Enter employee's phone number:   "),  # Phone Number
               getint("Enter employee's salary:   "),  # Employee Salary
               input("Enter employee's designation:   "),  # Designation
               getdate(False)]  # Date of joining
        print("Following entered values will be passed into database."
              "\n(Don't worry 0 will be replaced with original value)")
        printer(inp)
        print("Are you satisfied with entered data?")
        choice = getchoiceYorN()
        if choice:
            return inp
        else:
            continue

# Used to get simple yes/no inputs from user
def getchoiceYorN():
    while True:
        Choice = input(":    ")

        if Choice.lower() in ('y', 'yes', 'yup', 'oui', 'si'):
            return True
        elif Choice.lower() in ('n', 'no', 'nope', 'non'):
            return False
        else:
            print("\nEnter a valid response.\n")


# Used to sort the file in multiple ways
def choose_sort() -> bool | None:
    while True:
        print("How will you sort the data?"
              "\nType 1 for Sorting in ascending order or just leave blank."
              "\nType 2 for Sorting in descending order"
              "\nType 0 to go back to previous menu")
        choice = ''.join(i for i in input(":    ") if i.isdigit())
        if choice == '0':
            print("Going back.......\n")
            return None
        elif choice == '1' or choice == '':
            return False
        elif choice == '2':
            return True
        else:
            print("\nEnter a valid response.\n")


# Used to get a choice from the user.
def choose_opr() -> str:
    while True:
        opr = input("Choose the method of operation.\n"
                    "Type 0 to exit this menu\n"
                    "Type 1 for finding equal entries or just leave blank.\n"
                    "Type 2 for finding greater entries.\n"
                    "Type 3 for finding lesser entries.\n"
                    ":  ")
        opr = ''.join(i for i in opr if i.isdigit())
        if opr in ['0', '1', '2', '3']:
            return opr
        elif opr == '':
            return '1'
        else:
            print('Please enter a valid no. (1-3).')


# Used to get the index input from user withing range
def getind(txt: str, blank=False):
    file = filelist(csvfile)
    maxsno = file[-1][0]
    minsno = file[1][0]
    while True:
        ind = ''.join(i for i in input(txt) if i.isdigit())
        if ind == '' and blank:
            return ''
        elif ind == '' and not blank:
            return int(ind)
        elif int(minsno) <= int(ind) <= int(maxsno):
            return int(ind)
        else:
            print(f'Please enter a integer between {minsno}-{maxsno}')


# Used to update the records
def updateUI():
    print("Enter Serial No. or Employee ID or Name to update record off.")
    update_meth = input(":    ")

    print("Following entry is going to be updated.")
    ind: int = auto_search(csvfile, update_meth)
    if ind is None:
        return None
    print('\nAre you sure? (Y/N)')
    choice = getchoiceYorN()
    if choice:
        print("Enter 0 if you don't want to update certain field.")

        updateSNO(csvfile, getinput(), ind)
        print('\n')
        search_sno(csvfile, ind)
        print('\n')
    else:
        print('OK updation canceled.')


# Used to delete the records
def delUI():
    print("Enter Serial No. or Employee ID or Name to delete record off, leave blank to delete last record.")
    InpSno = input(":    ")
    if InpSno.strip(' ') == '':
        deletion(csvfile)
        return None
    print("Following entry/s are going to be deleted: ")
    ind = auto_search(csvfile, InpSno)
    if ind is None:
        return None
    print("\n Are you sure? (Y/N)")
    choice = getchoiceYorN()
    if choice:
        deletion(csvfile, ind)
        print("Entry/s has/have been successfully deleted.")
    else:
        print('OK deletion cancelled.')


# While loop for the menu
while True:
    print("\nWhat should I do for you?"
          "\nType 1 for Inserting data"
          "\nType 2 for Updating values of the data"
          "\nType 3 for Delete entries of the data"
          "\nType 4 for Searching the data"
          "\nType 5 for Viewing sorted data"
          "\nType 6 for Returning a report of the Company"
          "\nType 7 for Displaying the entire file at once."
          "\nType 0 for Exiting the program")
    MainInp = getint(":    ")
    if MainInp == 0:
        print("Exiting the program. Goodbye!")
        break
    if MainInp == 1:  # insertion
        print("Start entering the details of the employee one by one.")
        insert(csvfile,
               getinput(),
               getind('Enter the index no. u want to add the record to, '  # Index
                      'leave blank if you wish to add at the end: ', True))
        print('\nInsertion Complete\n')


    elif MainInp == 2:  # update
        updateUI()

    elif MainInp == 3:  # delete
        delUI()

    elif MainInp == 4:  # search
        while True:
            print("How would you like to search the data?"
                  "\nType 1 for Searching by Serial Number"
                  "\nType 2 for Searching by Employee's Name"
                  "\nType 3 for Searching by Employee ID"
                  "\nType 4 for Searching by Salary"
                  "\nType 5 for Searching by Designation"
                  "\nType 6 for Searching by Date of Joining"
                  "\nType 7 for Searching by Sex"
                  "\nType 8 to automatically detect Sno., Employee ID or Name."
                  "\nType 0 to go back to previous menu")
            SecInp = getint(":    ")

            if SecInp == 0:
                print("Going back.......\n")
                break

            elif SecInp == 1:
                opr = choose_opr()
                if opr == '0':
                    print("Going back.......\n")
                    break
                search_sno(csvfile,
                           getind("Enter a serial number or leave blank to check last entry:   "),
                           opr)
                break

            ###---------------------Name--------------------------
            elif SecInp == 2:
                better_srch_name(csvfile, input("Enter a first/last/full name:   "))
                break
            ###---------------------EmpId--------------------------
            elif SecInp == 3:
                search_empid(csvfile, getemp())
                break
            ###---------------------Salary--------------------------
            elif SecInp == 4:
                opr = choose_opr()
                if opr == '0':
                    print("Going back.......\n")
                    break
                search_salary(csvfile,
                              getint("Enter the Amount:   "), opr)
                break
            ###---------------------Designation--------------------------
            elif SecInp == 5:
                search_divion(csvfile, input('Enter the division:   '))
                break
            ###---------------------DOJ40--------------------------
            elif SecInp == 6:
                opr = choose_opr()
                if opr == '0':
                    print("Going back.......\n")
                    break
                srch_date(csvfile,
                          getdate(False), opr)
                break

            ###---------------------Sex--------------------------
            elif SecInp == 7:
                search_sex(csvfile, getsex())
                break
            elif SecInp == 8:
                auto_search(csvfile, input("Enter any Sno., Employee ID or Name\n"
                                           ":   "))
            ###---------------------Valid Respone--------------------------
            else:
                print("\nEnter a valid response.\n")

    ##--Sorted function Start, updates the file only if users wants to.
    elif MainInp == 5:
        while True:
            print("Choose your method of sorting\n"
                  "Type 1 for Sorting by employee id\n"
                  "Type 2 for Sorting by name\n"
                  "Type 3 for Sorting by salary\n"
                  "Type 4 for Sorting by date of joining\n"

                  "Type 0 to go back to previous menu")
            SecInp = getint(":    ")

            ###---------------------Going Back--------------------------
            if SecInp == 0:
                print("Going back.......\n")
                break
            ###---------------------EmpID--------------------------
            if SecInp in [1, 2, 3, 4]:
                choice = choose_sort()
                if choice is None:
                    break
            else:
                print("\nEnter a valid response.\n")
                continue

            ###---------------------Emp_ID--------------------------
            if SecInp == 1:
                data = sort_empid(csvfile, choice)

            ###---------------------Name--------------------------
            elif SecInp == 2:
                data = sortalpha(csvfile, choice)

            ###---------------------Salary--------------------------
            elif SecInp == 3:
                data = sort_salary(csvfile, choice)

            ###---------------------Date--------------------------
            elif SecInp == 4:
                data = sort_date(csvfile, choice)
            print("Would you like to update the file with the sorted data?")
            if getchoiceYorN():
                writelist_to_file(data)
                break
            else:
                break



    # --Report function Start
    elif MainInp == 6:
        print("\nWhich report should I present to you?\n"
              "Type 1 for getting a report on company's expenditure on Salary\n"
              "Type 2 for getting a report on company's work division\n"
              "Type 0 to go back to previous menu")
        while True:
            SecInp = getint(":    ")
            ###---------------------Going Back--------------------------
            if SecInp == 0:
                print("Going back.......\n")
                break

            elif SecInp == 1:
                better_salary_report(csvfile)
                break
            elif SecInp == 2:
                better_rep_div_cnt(csvfile)
                break
            else:
                print('Please enter a valid response')
    elif MainInp == 7:
        display(csvfile)

    else:
        print("\nEnter a valid response.\n")
