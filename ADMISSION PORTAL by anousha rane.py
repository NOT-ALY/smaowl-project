print("                   ===========W E L C O M E==========")
print("This is an admission portal designed by Anousha Rane for students enrolling                           themselves into college.")
firstname=input("First Name: ")
middlename=input("Middle Name: ")
surname=input("Surname: ")
dob=input("Date of Birth(dd/mm/yyyy): ")
yob=int(input("Enter Student's year of birth: "))
age=int(input("Enter Student's Age(in years): "))
pname=input("Parent's/Guardian's Name: ")
adress=input("Adress: ")
p=int(input("Enter Your Average Percentage from the Previous Year: "))

#GENERAL CONDITIONS
if(age<15):
    print("--------------NOT ELIGIBLE TO GO TO COLLEGE--------------")
    exit()
if(2020-yob<16):
    print("--------------NOT ELIGIBLE TO GO TO COLLEGE--------------")
    exit()
print("1.Arts")
print("2.Science")
print("3.Commerce")
ch=int(input("Enter Choice of Stream:"))

#ARTS

if(ch==1):
    print("")
    print("1.Event Management")
    print("2.Hotel Management")
    print("3.Fashion Designing")
    print("4.Journalism & Mass Communication")
    print("5.Bachelor of Fine Arts")
    print("6.Bachelor of Business Administration")
    c=int(input("ENTER THE COURSE OF YOUR CHOICE:"))
    if(p>=65):
        print("--------------ELIGIBLE--------------")
    else:
        print("--------------NOT ELIGIBLE--------------")

#SCIENCE

elif(ch==2):
    print("1.PCM")
    print("2.PCB")
    c=int(input("ENTER THE COURSE OF YOUR CHOICE:"))
    if(c==1):
         print("")
         print("1.Engineering")
         print("2.BMA")
         print("3.BCA")
         print("4.Merchant Navy Courses")
         print("5.Financial Markets")
         cc=int(input("ENTER THE COURSE OF YOUR CHOICE:"))
         if(p>=80):
            print("--------------ELIGIBLE--------------")
         else:
            print("--------------NOT ELIGIBLE--------------")
    elif(ch==2):
        print("1.MBBS")
        print("2.BAMS")
        print("3.BHMS")
        print("4.BUMS")
        print("5.BDS")
        cc=int(input("ENTER THE COURSE OF YOUR CHOICE:"))
        if(p>=80):
            print("--------------ELIGIBLE--------------")
        else:
            print("--------------NOT ELIGIBLE--------------")


#COMMERCE
elif(ch==3):
        print("")
        print("1.B.E/B.Tech")
        print("2.B.Des")
        print("3.Defence")
        print("4.BCOM")
        print("5.BCA")
        print("6.LLB")
        cc=int(input("ENTER THE COURSE OF YOUR CHOICE:"))
        if(p>=70):
            print("--------------ELIGIBLE--------------")
        else:
            print("--------------NOT ELIGIBLE--------------")

    

































