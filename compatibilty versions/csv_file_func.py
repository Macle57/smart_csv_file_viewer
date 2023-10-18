from statistics import mode
from csv import reader, writer

csvfile = "MOCK_DATA.csv"

_Sno_ = 0
_Name_ = 2
_DOB_ = 3
_Salary_ = 8
_Address_ = 6
_EmpID_ = 1
_Sector_ = 9
_Sex_ = 4
_email_ = 5
_DOJ_ = 10


# Used to print formatted records and automatically account for increased records.
def printer(i):
    try:
        print('{:<7}{:<10}{:<20}{:<12}{:<5}{:<35}{:<30}{:<15}{:<10}{:<25}{:<15}'.format(*i))
    except IndexError:
        print(('{:<15}' * len(i)).format(*i))


# Used to get the file as a list
def filelist(file):
    with open(file) as temp:
        return list(reader(temp, delimiter=','))


# Writes a list to the file as a new record
def writelist_to_file(cont, rd='w'):
    with open(csvfile, rd, newline='') as temp:
        writer(temp, delimiter=',').writerows(cont)


def display(file):  # Used to display the file
    for i in filelist(file):
        printer(i)


def displaylist(temp):  # Display list in file format.
    for i in temp:
        printer(i)


# Converts date to yyyy-mm-dd from string
def managedate(date):  # input date- mm/dd/yyyy
    date = list(int(j) for j in date.split('/', 2))
    return [date[2], date[0], date[1]]  # YYYY-MM-DD


# Correct serial number of the file in list format if needed
def modifysnolist(var):
    cnt = 0
    for i in var:
        cnt += 1
        i[_Sno_] = cnt
    return var


# Inserts a record at desired position, and at last if none mentioned
def insert(file, cont, ind=''):
    tempstor = filelist(file)
    if ind == '':
        index = int(tempstor[-1][_Sno_]) + 1
        writelist_to_file([[index, *cont]], 'a')
    else:
        try:
            tempstor.insert(int(ind), [ind] + cont)
            header = tempstor[0]
            tempstor = modifysnolist(tempstor[1::])
            writelist_to_file([header, *tempstor])
        except ValueError:
            print('Please enter a serial no. as a integer')


# Updates the desired record
def updateSNO(file, cont, sno):
    tempstor = filelist(file)
    record = tempstor[sno][1::]
    for i in range(len(cont)):
        if str(cont[i]) == '0':
            cont[i] = record[i]

    tempstor[sno] = [sno] + cont
    writelist_to_file(tempstor)


# Deletes a record
def deletion(file, ind=None):
    tempstor = filelist(file)
    header = tempstor[0]
    if ind is None:
        print("Successfully deleted record: ")
        printer(header)
        printer(tempstor.pop())
        tempstor.remove(header)
    else:
        flag = True
        for i in tempstor:
            if i[_Sno_] == str(ind):
                print("Successfully deleted record: ")
                printer(header)
                printer(i)
                tempstor.remove(i)
                tempstor = modifysnolist(tempstor[1::])
                flag = False
                break
        if flag:
            print(f'Cant find a record with mentioned serial number:{ind}')

    writelist_to_file([header, *tempstor])


# Searches a record with sno
def search_sno(file, sno, opr='1'):
    tempstor = filelist(file)
    header = tempstor[0]
    flag = True
    if opr == "1":
        for i in tempstor[1::]:
            if int(i[_Sno_]) == sno:
                printer(header)
                printer(i)
                return int(i[int(_Sno_)])
        return None

    elif opr == "2":
        for i in tempstor[1::]:
            if int(i[_Sno_]) > sno:
                if flag:
                    printer(header)
                    flag = False
                printer(i)

    elif opr == "3":
        for i in tempstor[1::]:
            if int(i[_Sno_]) < sno:
                if flag:
                    printer(header)
                    flag = False
                printer(i)
    else:
        print('Please enter a reasonable operator with respect to ur input.')


# Searches the record smartly with any last name or first name automatically
def better_srch_name(file, name):
    tempstor = filelist(file)
    names = []
    for i in tempstor:
        names.append(i[_Name_].lower().split())
    flag = False
    flag1 = True
    for i in names:
        if name.lower() in i or name.lower() == ' '.join(i):
            indx = names.index(i)
            if flag1:
                printer(tempstor[0])
                flag1 = False
            printer(tempstor[indx])
            flag = True
    if flag:
        return indx
    else:
        print('Check your spelling.')


# Searches with emp id
def search_empid(file, parameter_empid):
    tempstor = filelist(file)
    for i in tempstor[1::]:
        if int(i[_EmpID_]) == parameter_empid:
            printer(tempstor[0])
            printer(i)
            return int(i[_Sno_])
    print("\n Can't find a employee with mentioned employee id.")
    return None


# automatically detects input from name, Sno., empid and search.
def auto_search(file, inp):
    try:
        inp = int(inp)
        if len(str(inp)) <= 3:  # Sno. checker
            ind = search_sno(file, inp)
            if ind is None:
                print('Cant find someone with mentioned Sno.')
            return ind
        else:  # Emp ID assumer
            ind = search_empid(file, inp)
            if ind is None:
                print('Cant find someone with mentioned Employee ID.')
            return ind
    except ValueError:  # Name
        ind = better_srch_name(file, inp)
        if ind is None:
            print('Cant find someone with mentioned Name.')
        return ind


# Searches with given SEX of employee
def search_sex(file, sex):
    tempstor = filelist(file)
    flag = True
    for i in tempstor[1::]:
        if sex == i[_Sex_]:
            printer(i)
            flag = False
        elif sex == i[_Sex_]:
            printer(i)
            flag = False
        elif sex == i[_Sex_]:
            printer(i)
            flag = False
    if flag:
        print('Please enter a valid sex(M/F/O)')


# Searches with mentioned salary
def search_salary(file, parameter_salary, operator='1'):
    tempstor = filelist(file)
    header = tempstor[0]
    flag = True
    flag1 = True
    for i in tempstor[1::]:
        if operator == "1":
            if int(i[_Salary_]) == parameter_salary:
                if flag1:
                    printer(header)
                    flag1 = False
                printer(i)
                flag = False
        elif operator == "2":
            if int(i[_Salary_]) > parameter_salary:
                if flag1:
                    printer(header)
                    flag1 = False
                printer(i)
                flag = False
        elif operator == "3":
            if int(i[_Salary_]) < parameter_salary:
                if flag1:
                    printer(header)
                    flag1 = False
                printer(i)
                flag = False

    if flag:
        print('Please enter a reasonable operator.')


# Search with dates
def srch_date(file, inp_date, opr="1"):
    tempstor = filelist(file)
    header = tempstor[0]
    date = managedate(inp_date)
    flag = True
    flag1 = False
    for i in tempstor[1::]:
        srtdate = managedate(i[_DOJ_])
        if str(opr) == '1':
            if srtdate == date:
                if flag1:
                    printer(header)
                    flag1 = False
                printer(i)
                flag = False
        elif str(opr) == '2':
            if srtdate > date:
                if flag1:
                    printer(header)
                    flag1 = False
                printer(i)
                flag = False
        elif str(opr) == '3':
            if srtdate < date:
                if flag1:
                    printer(header)
                    flag1 = False
                printer(i)
                flag = False
    if flag:
        print('Enter a reasonable date and ensure its in correct format.')


# Search by division
def search_divion(file, parameter_division):
    tempstor = filelist(file)
    flag1 = True
    for row in tempstor:
        if row[_Sector_].lower() == parameter_division.lower().rstrip(' '):
            if flag1:
                printer(tempstor[0])
                flag1 = False
            printer(row)


# Sorts alphabetically
def sortalpha(file, desc=False):
    tempstor = filelist(file)

    def function(x):
        return x[_Name_]

    header = tempstor[0]
    tempstor.remove(header)
    tempstor = modifysnolist(sorted(tempstor, key=function, reverse=desc))
    sorteddata = [header, *tempstor]
    displaylist(sorteddata)
    return sorteddata


# Sorts by date
def sort_date(file, desc=False):
    tempstor = filelist(file)

    def function(x):
        return managedate(x[_DOJ_])

    header = tempstor[0]
    tempstor.remove(header)
    tempstor = modifysnolist(sorted(tempstor, key=function, reverse=desc))
    sorteddata = [header, *tempstor]
    displaylist(sorteddata)
    return sorteddata


# Sorts by salary
def sort_salary(file, desc=False):
    tempstor = filelist(file)

    header = tempstor[0]
    tempstor.remove(header)

    def function(x):
        return int(x[_Salary_])

    tempstor = modifysnolist(sorted(tempstor, key=function, reverse=desc))
    sorteddata = [header, *tempstor]
    displaylist(sorteddata)
    return sorteddata


# Sorts by employee ID
def sort_empid(file, desc=False):
    tempstor = filelist(file)

    header = tempstor[0]
    tempstor.remove(header)

    def function(x):
        return int(x[_EmpID_])

    tempstor = sorted(tempstor, key=function, reverse=desc)

    tempstor = modifysnolist(tempstor)
    sorteddata = [header, *tempstor]
    displaylist(sorteddata)
    return sorteddata


# Makes a salary report
def better_salary_report(file):
    tempstor = filelist(file)
    sal = []
    for i in tempstor[1::]:
        sal.append(int(i[_Salary_]))
    print("SALARY REPORT"
          "\n-------------\n"
          f"Total Paid Salary:  {sum(sal)}"
          "\n <Sal> (<Name>: <emp_id>)\n"
          f"Average Salary Paid:\t{sum(sal) // len(sal)}\n"
          f"Highest Salary:\t{max(sal)} ({tempstor[sal.index(max(sal))][_Name_]} :"
          f"{tempstor[sal.index(max(sal))][_EmpID_]} )\n"
          f"Lowest Salary:\t{min(sal)}({tempstor[sal.index(min(sal))][_Name_]}:"
          f"{tempstor[sal.index(min(sal))][_EmpID_]})")


# Makes a report that displays divisions and employees that work in it
def better_rep_div_cnt(file):
    print("WORK DIVISON REPORT")
    print("-------------\n")

    tempstor = filelist(file)
    tempstor.remove(tempstor[0])
    print(f"Total Employee Count:   {int(tempstor[-1][_Sno_])} \n")
    for i in tempstor:
        i[_Sector_] = i[_Sector_].rstrip(' ')
    div = []
    for i in tempstor:
        div.append(i[_Sector_])
    l = div.count(mode(div))
    div = sorted(list(set(div)))
    print(('{:<25}' * len(div)).format(*(list(i.upper() for i in div))))
    data = list([i[_Name_], i[_Sector_]] for i in tempstor)

    def function(x):
        return x[1]

    data = sorted(data, key=function)
    test = []
    for j in range(l):
        TEST = [""] * len(div)
        keye = []
        for i in range(len(data)):
            if data[i][1] not in keye and data[i][0] not in test:
                keye.append(data[i][1])
                TEST[div.index(data[i][1])] = data[i][0]
                test.append(data[i][0])
        print(('{:<25}' * len(div)).format(*TEST))
