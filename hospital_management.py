import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="123456", database="hospital")

# Function to add doctor
def add_doctor():
    n = input("ENTER THE NAME OF DOCTOR: ")
    s = input("ENTER THE SPECIALITY OF DOCTOR: ")
    d = input("ENTER THE DOCTOR'S DATE OF BIRTH: ")
    a = input("ENTER THE DOCTOR'S ADDRESS: ")
    p = input("ENTER THE DOCTOR'S PHONE NUMBER: ")
    data = (n, s, d, a, p)
    sql = 'insert into doctor values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Function to remove doctor
def remove_doctor():
    n = input("DOCTOR name: ")
    data = (n,)
    sql = 'delete from doctor where name =%s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Function to add patient
def add_patient():
    n = input("ENTER THE NAME OF PATIENT: ")
    a = input("ENTER THE AGE OF PATIENT: ")
    g = input("ENTER THE GENDER OF PATIENT: ")
    b = input("ENTER THE BLOOD GROUP OF PATIENT: ")
    p = input("ENTER THE PATIENT'S PHONE NUMBER: ")
    data = (n, a, g, b, p)
    sql = 'insert into patient values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Function to remove patient
def remove_patient():
    n = input("PATIENT name: ")
    data = (n,)
    sql = 'delete from patient where patient_name = %s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()


# Function to add appointment
def add_appointment():
    n = input("PATIENT name: ")
    d = input("DOCTOR name: ")
    a = input("ENTER THE APPOINTMENT DATE: ")
    t = input("ENTER THE APPOINTMENT TIME: ")
    data = (n, d, a, t)
    sql = 'insert into appointment values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Function to remove appointment
def remove_appointment():
    n = input("PATIENT name: ")
    d = input("DOCTOR name: ")
    a = input("ENTER THE APPOINTMENT DATE: ")
    t = input("ENTER THE APPOINTMENT TIME: ")
    data = (n, d, a, t)
    sql = 'delete from appointment where patient_name =%s and doctors_name =%s and appointment_date=%s and appointment_time=%s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Display all doctors
def display_doctor():
    sql = "select * from doctor"
    c = con.cursor()
    c.execute(sql)
    c = c.fetchall()
    print(c)
    for i in c:
        print("NAME:", i[0])
        print("SPECIALITY:", i[1])
        print("DATE OF BIRTH:", i[2])
        print("ADDRESS:", i[3])
        print("PHONE:", i[4])
        print(">--------------------------------<")
    print(">------------------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Display all patients
def display_patient():
    sql = "select * from patient"
    c = con.cursor()
    c.execute(sql)
    c = c.fetchall()
    print(c)
    for i in c:
        print("NAME:", i[0])
        print("AGE:", i[1])
        print("GENDER:", i[2])
        print("BLOOD GROUP:", i[3])
        print("PHONE:", i[4])
        print("<-------------------------------->")
    print(">------------------------------------------------------------------------------------------------------------------------------------------------")
    main()

# Main program starts here!!
def main():
    print(" WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
    print("1. Add Doctor")
    print("2. Remove Doctor")
    print("3. Add Patient")
    print("4. Remove Patient")
    print("5. Add Appointment")
    print("6. Remove Appointment")
    print("7. Display Doctor")
    print("8. Display Patient")
    
    choice = input("Enter The NO. :")
    
    print(">-----------------------------------<")
   
    if (choice == '1'):
        add_doctor()

    elif (choice == '2'):
        remove_doctor()

    elif (choice == '3'):
        add_patient()

    elif (choice == '4'):
        remove_patient()

    elif (choice == '5'):
        add_appointment()

    elif (choice == '6'):
        remove_appointment()

    elif (choice == '7'):
        display_doctor()

    elif (choice == '8'):
        display_patient()

    else:
        print("Wrong choice................")
        main()

main()