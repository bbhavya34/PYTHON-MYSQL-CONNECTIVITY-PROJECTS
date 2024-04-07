import mysql.connector as a                                                           #Using a as alias
con= a.connect(host="localhost",user="root",passwd="123456",database="school")        #Creating a connection


# Function to add student
def add_student():
    n=input("ENTER THE NAME OF STUDENT: ")
    c=input("ENTER THE CLASS OF STUDENT: ")
    r=input("ENTER THE ROLL NUMBER: ")
    a=input("ENTER THE ADDRESS: ")
    p=input("ENTER THE PHONE NUMBER: ")
    data=(n,c,r,a,p)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entered successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Function to remove student
def remove_student():
    c=input("class name: ")
    r=input("Roll number: ")
    data=(c,r)
    sql='delete from student where CLASS =%s and ROLL=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Function to add teacher
def add_teacher():
    name=input("Teacher's name: ")
    post=input("post of the teacher: ")
    salary=input("salary of the teacher: ")
    phone=input("phone number of teacher: ")
    account=input("account of teacher: ")
    data=(name,post,salary,phone,account)
    sql='insert into teacher values(%s,%s,%s,%s,%s,)'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-----------------------------------------------------------------------------------------------------------------------------------------")
    main()
#Function to remove teacher
def remove_teacher():
    name=input("Teacher name: ")
    account=input("Account No: ")
    data=(name,account)
    sql='delete from teacher where  name =%s and account =%s'
    c= con.cursor()
    c.execute(sql,data)
    con.commit()
    print(" Data Updated")
    print(">------------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Function to add absentees 
def absentees():
    d=input("date:")
    cl=input("Class:")
    ab=input("Name Of Absent Student")
    data=(d,cl,ab)
    sql='insert into attendance values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">------------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Function to add absent teacher
def absent_teacher():
    d=input("data:")
    ab=input("Names Of Absent Teacher")
    data=(d,ab)
    sql='insert into tattendance  values(%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">------------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Function to add fees date wrt student
def submit_fees():
    n=input("student name: ")
    c=input("class name :   ")
    r=input("roll no.:  ")
    m=input("months and year: ")
    f=input("fess: ")
    d=input("date: ")
    data=(n,c,r,m,f,d)
    sql='insert  into fees values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-------------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Function to add salary data wrt teachers
def pays_Salary():
    n=input("Teacher name:")
    m=input("months:")
    p=input("Yes/No:")
    data=(n,m,p)
    sql='insert into salary values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-------------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Display all students of a class
def display_class():
    cl=input("class:")
    data=(cl,)
    sql="select * from student where class=%s"
    c=con.cursor()
    c.execute(sql,data)
    c=c.fetchall()
    print(c)
    for i in c:
        print("NAME:",i[0])
        print("CLASS:",i[1])
        print("ROLL:",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print(">--------------------------------<")
    print(">------------------------------------------------------------------------------------------------------------------------------------------------")
    main()
# Display all teachers
def display_teacher():
    sql="select * from teacher"
    c=con.cursor()
    c.execute(sql)
    c=c.fetchall()
    for  i in d:
        print("NMAE:",i[0])
        print("POST:",i[1])
        print("SALARY:",i[2])
        print("ADDRESS:",i[3])
        print("ACNO:",i[4])
        print(">---------------------------------<")
    print(">--------------------------------------------------------------------------------------------------------------------------------------------------")
    
# Main program starts here!!
def main():
    print("""                                               KENDRIYA VIDYALAYA PRAGATI VIHAR


                                           1.ADD STUDENT                                             2.REMOVE STUDENT
                                           3.ADD TEACHER                                             4.REMOVE TEACHER
                                           5.CLASS ATTENDANCE                                        6.TEACHER ATTENDANCE
                                           7.SUBMIT FEES                                             8.PAY SALARY
                                           9.DISPLAY CLASS                                           10.TEACHER LIST

""")
    choice=input("Enter The NO. :")
    print(">-----------------------------------<")
    if(choice=='1'):
        add_student()

    elif(choice=='2'):
        remove_student()

    elif(choice=='3'):
        add_teacher()

    elif(choice=='4'):
        remove_teacher()

    elif(choice=='5'):
        absentees()

    elif(choice=='6'):
        absent_teacher()

    elif(choice=='7'):
        submit_fees()

    elif(choice=='8'):
        pays_Salary()

    elif(choice=='9'):
        display_class()

    elif(choice=='10'):
        display_teacher()
        
    else:
        print("Wrong choice................")
        main()

main()