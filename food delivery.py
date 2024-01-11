import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Mohitha@2003',database='mohitha')
mycursor=mydb.cursor()

def validate(username,password):
    mycursor.execute("select * from user_info where name like %s",(username,))
    data=mycursor.fetchall()
    print(data,'data')
    name=data[0][0]
    passw=data[0][1]
    if name==username and passw==password:
        print("Welcome " + name)
    return 1
def order(username):
    print('1.BRIYANI\n 2.NOODLES\n 3.MEALS \n 4.DOSA')
    f={1:'briyani',2:'noodles',3:'meals',4:'dosa'}
    ord=int(input("Enter your option : "))
    if ord>=1 and ord<=5:
        det=f[ord]
        mycursor.execute('select cost from cost_table where f_name like %s',(det,))
        data=mycursor.fetchone()
        print(data,'cost')
        rs=int(data[0])
        print(rs)
        count=int(input("Enter the no of oredrs : "))
        #global total_rs
        total_rs=count*rs
        print(total_rs)
        mycursor.execute('insert into order_detail(username,food_ordered,total_cost) values (%s,%s,%s) ',(username,det,total_rs,))
        mydb.commit()
        mycursor.execute('select * from order_detail where username like %s',(username,))
        data=mycursor.fetchall()
        print(data,'data')
        name=data[0][0]
        food_name=data[0][1]
        cost=data[0][2]
        print("username : %s  "%name)
        print("food_ordered : %s"%food_name)
        print("cost : %s "%total_rs)
        return 1
    else:
        print("Invalid login")
        
def display(username):
    mycursor.execute('select * from order_detail where username like %s',(username,))
    data=mycursor.fetchall()
    if data:
        name=data[0][0]
        print("name : %s"%name)
        for i in range (len(data)):
            print("food : %s"%data[i][1])
            print("cost :%s"%data[i][2])
    else:
        print("No data found")
    return 1

def display_userinfo(uname):
    mycursor.execute('select * from user_info where name like %s',(uname,))
    data=mycursor.fetchone()
    name=data[0]
    passw=data[1]
    ph=data[2]
    add=data[3]
    print("NAME : %s"%name)
    print("password : %s"%passw)
    print("Phone : %s"%ph)
    print('address : %s'%add)
def display_food():
    mycursor.execute('select * from cost_table')
    data=mycursor.fetchall()
    for i in range(len(data)):
        print('food_name : %s'%data[i][0])
        print('cost : %s'%data[i][1])
def display_alluser():
    mycursor.execute('select * from user_info')
    data=mycursor.fetchall()
    for i in range(len(data)):
        print('username %s'%data[i][0])
        print('password : %s'%data[i][1])
        print('phone :%s'%data[i][2])
        print('address: %s'%data[i][3])

def user_order(user):
    mycursor.execute('select * from order_detail where username like %s',(user,))
    data = mycursor.fetchall()
    if data:
        print("User name : %s"%data[0][0])
        for i in range(len(data)):
            print("Food ordered : %s"%data[i][1])
            print("Totalcost : %s"%data[i][2])







if __name__=='__main__':
    a=input("enter your role new/login/admin: ")
    a=a.lower()
    if a=='new':
        username=input()
        password=input()
        phone=int(input())
        address=input()
        mycursor.execute("insert into user_info (name,password,phone,address) values (%s,%s,%s,%s)",(username,password,phone,address))
        mydb.commit()
        print("registration successfull")
        print('if u want to oredr press 1')
        inp=int(input("Enter your choice : "))
        if inp==1:
            order(username)
    elif a=='login':
        username=input("enter your name : ")
        password=input("enter your password : ")
        validate(username,password)
        if validate(username,password):
            print('1.order food')
            print('2.shoe menu')
            opt=int(input())
            if opt==1:
                if order(username):
                    print("Successfully ordered")
            elif opt==2:
                display(username)
            else:
                print("please enter Valid options ")
        else:
            print("invalid or user does not exsist")

    elif a=='admin':
        print('1.DIAPLAY a particular user detail \n 2.shoe food deails \n 3.show all the user informstion \n 4.display oreder details')
        opt=int(input("Enter your option : "))
        if opt==1:
            uname=input("Enter user name : ")
            display_userinfo(uname)
        elif opt==2:
            display_food()
        elif opt==3:
            display_alluser()
        elif opt==4:
            user=input("Enter username to get order info : ")
            user_order(user)

