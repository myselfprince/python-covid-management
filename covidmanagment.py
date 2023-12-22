'''
Please install the required modules for the program to run perfectly fine
1. mysql.connector and mysql-connector-python 
2. playsound 
'''
import datetime
import mysql.connector
import playsound

mydb = mysql.connector.connect(host="localhost", user="root", password="tciimp")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists cm")
mycursor.execute("use cm")
mycursor.execute("create table if not exists staffs(s_id int auto_increment primary key, name varchar(30), post varchar(30), salary int(10))")
mycursor.execute("create table if not exists patients(p_id int auto_increment primary key, name varchar(30),age int(3), address varchar(200), gender char(10))")
mycursor.execute("create table if not exists login(password varchar(200) not null primary key)")

playsound.playsound("audios/wtcms.mp3") 


menu = int()
while menu!=3:
    print("------------------------------------------------------\nWELCOME TO COVID MANAGMENT SYSTEM\n------------------------------------------------------")
    print("Slect From The Menu:-")
    print("1.Admin\n2.Patient\n3.exit")
    sum = 0
    menu = int(input("Please enter a number(1/2/3): "))
    if menu==2:
        test = input("Do you want to take a covid test(y/n): ").lower()
        if test=='y':
            playsound.playsound("audios/patf.mp3") 
            print("Please answer the following: ")
            t1 = input("Are you having dry cough(y/n): ").lower()
            if t1=='y':
                sum += 1
            t2 = input("Are you having fever(y/n): ").lower()
            if t2=='y':
                sum += 1
            t3 = input("Are you feeling tired and fatigue(y/n): ").lower()
            if t3=='y':
                sum += 1
            t4 = input("Are you having headche(y/n): ").lower()
            if t4=='y':
                sum += 1
            t5 = input("Are you having difficulty in breathing(y/n): ").lower()
            if t5=='y':
                sum += 1
            t6 = input("Are you having a loss of taste or smell(y/n): ").lower()
            if t6=='y':
                sum += 1
            if (t1==t2==t3==t4==t5==t6=='y'):
            #if (t1=='y' and t2=='y' and t3=='y' and t4=='y' and t5=='y' and t6=='y'):
                playsound.playsound("audios/sosorry.mp3")
                playsound.playsound("audios/yrcppftd.mp3")  
                print("you are covid positive. \nPlease Enter your details.")
                naam = input("Enter Your Full Name: ").upper()
                age = int(input("Enter your age"))
                pata = str(input("Enter your Address: "))
                sex = input("Enter your Gender(m/f): ")
                                
                sql = "INSERT INTO patients (name,age,address,gender) VALUES (%s,%s,%s,%s)"
                val = (naam, age, pata,sex)
                mycursor.execute(sql, val)

                mydb.commit()
                playsound.playsound("audios/ursrtc.mp3") 
                print("TEST COMPLETED \nThank You, You are registered. Take Care.\n------------------------------------------------------")


            elif (t1==t2==t4=="y") and (t3==t5==t6=='n'):
                playsound.playsound("audios/icbjcafbwrtcad.mp3") 
                print("Its can be just a cough and fever. but we recommend to consult a doctor. ")
            elif (t1==t2==t3==t4==t5==t6=='n'):
                playsound.playsound("audios/dwyas.mp3") 
                print("Don't worry you are safe")
            elif sum == 3:
                playsound.playsound("audios/itisnotcovid.mp3") 
                print("It is not Covid, You may be Suffering From another disease. Please Consult a doctor.")
            else:
                playsound.playsound("audios/umbsfad.mp3") 
                print("You may be Suffering From another disease. Please Consult a doctor.")
        if test=='n':
            playsound.playsound("audios/otyfj.mp3") 
            print("Ok! Thank You For Joining")
    elif menu==1:
        mycursor.execute("select count(*) from login")
        for i in mycursor:
            a = i
            if a[0] == 0:
                print("looks like a new user")
                no_exist_pass = input("Set new password: ")
                sql = "INSERT INTO login (password) VALUES (%s)"
                val = (no_exist_pass,)
                mycursor.execute(sql,val)

                mydb.commit()
            else:
                playsound.playsound("audios/enterpass.mp3") 
                psw = input("please enter admin password: ")
                mycursor.execute("select * from login")
                for i in mycursor:
                    real_psw = i[0]
                    
                if psw == real_psw:
                    playsound.playsound("audios/yasiaa.mp3") 
                    print("**************************\nYou are now Admin\n**************************")
                    admin_input = int()
                    while admin_input!=6:
                        print("Choose from the following \n1. Add patient \n2.Add Staff \n3.Remove Patient \n4.Remove Satff \n5.Change Password \n6.Logout")
                        admin_input = int(input("Enter your choice: "))
                        if admin_input == 1:
                            more_p_add = 'y'
                            while more_p_add == "y":
                                naam = input("Enter Patient's Full Name: ").upper()
                                age = int(input("Enter Patient's age: "))
                                pata = str(input("Enter Patient's Address: "))
                                sex = input("Enter Patient's Gender(m/f): ")
                                                
                                sql = "INSERT INTO patients (name,age,address,gender) VALUES (%s,%s,%s,%s)"
                                val = (naam, age, pata,sex)
                                mycursor.execute(sql, val)
                                mydb.commit()
                                playsound.playsound("audios/phbas.mp3") 
                                print("Patient Has Been Added Successfully.")
                                print()
                                playsound.playsound("audios/dywtamp.mp3") 
                                more_p_add = input("Do you want to add More Patient?(y/n) ").lower()
                                if more_p_add == 'n':
                                    break
                        elif admin_input==2:
                            more_staff_add = 'y'
                            while more_staff_add == 'y':
                                staff_name = input("Enter staff Name: ")
                                staff_post = input("Enter staff Post: ")
                                staff_salary = int(input("Enter staff Salary"))
                                sql = "INSERT INTO staffs (name,post,salary) VALUES (%s,%s,%s)"
                                val = (staff_name,staff_post,staff_salary)
                                mycursor.execute(sql, val)
                                mydb.commit()
                                playsound.playsound("audios/sa.mp3") 
                                print("Staff Added.")
                                playsound.playsound("audios/dywtams.mp3") 
                                more_staff_add = input("Do you want to add more staff?(y/n) ")
                                if more_staff_add == 'n':
                                    break
                        elif admin_input==3:
                            playsound.playsound("audios/epid.mp3") 
                            patient_id=input("Enter patient Unique ID: ")
                            mycursor.execute("delete from patients where p_id='"+patient_id+"'")
                            mydb.commit()
                            playsound.playsound("audios/pr.mp3")
                        elif admin_input==4:
                            playsound.playsound("audios/esid.mp3") 
                            staff_id=input("Enter staff Unique ID: ")
                            mycursor.execute("delete from staffs where s_id='"+staff_id+"'")
                            mydb.commit()
                            playsound.playsound("audios/sr.mp3")
                        elif admin_input==5:
                            playsound.playsound("audios/enp.mp3") 
                            npsw = input("Enter new Password: ")
                            mycursor.execute("UPDATE login SET password = '"+npsw+"'")
                            mydb.commit()
                        elif admin_input==6:
                            playsound.playsound("audios/tya.mp3") 
                            print("thanks admin bye.")
                            continue
                        else:
                            ("Wrong input by admin")
                else: 
                    print("wrong password")
    elif menu==3:
        playsound.playsound("audios/tyfj.mp3") 
        print("Thank you for joining")
        exit()
    else:
        print("wrong input")
