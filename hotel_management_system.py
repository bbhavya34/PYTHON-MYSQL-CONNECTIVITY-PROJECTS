import mysql.connector as a
con= a.connect(host="localhost",user="root",passwd="123456",database="hotel_management")

def add_customer():
    name=input("Enter Customer's Name: ")
    phone=input("Enter Phone Number: ")
    address=input("Enter Address: ")
    city=input("Enter City: ")
    zipcode=input("Enter ZIP Code: ")
    data=(name,phone,address,city,zipcode)
    sql='insert into customer values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Customer added successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

def remove_customer():
    phone=input("Enter Phone Number of Customer to be Removed: ")
    data=(phone,)
    sql='delete from customer where PHONE=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Customer Removed")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

def book_room():
    name=input("Enter Customer's Name: ")
    phone=input("Enter Phone Number: ")
    check_in=input("Enter Check-In Date (YYYY-MM-DD): ")
    check_out=input("Enter Check-Out Date (YYYY-MM-DD): ")
    room=input("Enter Room Type: ")
    data=(name,phone,check_in,check_out,room)
    sql='insert into booking values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Room Booked Successfully")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

def cancel_booking():
    name=input("Enter Customer's Name: ")
    phone=input("Enter Phone Number: ")
    check_in=input("Enter Check-In Date (YYYY-MM-DD): ")
    check_out=input("Enter Check-Out Date (YYYY-MM-DD): ")
    room=input("Enter Room Type: ")
    data=(name,phone,check_in,check_out,room)
    sql='delete from booking where NAME=%s and PHONE=%s and CHECK_IN=%s and CHECK_OUT=%s and ROOM=%s'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Booking Cancelled")
    print(">----------------------------------------------------------------------------------------------------------------------------------------")
    main()

def display_customers():
    sql="select*from customer"
    c=con.cursor()
    c.execute(sql)
    c=c.fetchall()
    print(c)
    for i in c:
        print("NAME:",i[0])
        print("PHONE:",i[1])
        print("ADDRESS:",i[2])
        print("CITY:",i[3])
        print("ZIP CODE:",i[4])
        print(">--------------------------------<")
    
    main()

def display_bookings():
    sql="select*from booking"
    c=con.cursor()
    c.execute(sql)
    c=c.fetchall()
    print(c)
    for i in c:
        print("NAME:",i[0])
        print("PHONE:",i[1])
        print("CHECK-IN:",i[2])
        print("CHECK-OUT:",i[3])
        print("ROOM TYPE:",i[4])
        print(">---------------------------------<")
    
    

def main():
    print("HOTEL MANAGEMENT SYSTEM")
    print("1. ADD CUSTOMER")
    print("2. REMOVE CUSTOMER")
    print("3. BOOK A ROOM")
    print("4. CANCEL A BOOKING")
    print("5. DISPLAY CUSTOMERS")
    print("6. DISPLAY BOOKINGS")
    choice=input("Enter The NO. :")
    print("<----------------------------------->")


    if(choice=='1'):
        add_customer()

    elif(choice=='2'):
        remove_customer()

    elif(choice=='3'):
        book_room()

    elif(choice=='4'):
        cancel_booking()

    elif(choice=='5'):
        display_customers()

    elif(choice=='6'):
        display_bookings()
        
    else:
        print("Wrong choice................")
        main()

main()