# --------------list operations
# def create():
#     import csv 
#     f=open("results.csv","a",newline="")
#     a=csv.writer(f)
#     # a.writerow(["ID","name","rollno","emailid","address","mobileno","p1","p2","p3","p4","p5","total","percentage","result"])
#     loop=int(input("Enter the no. of rows :"))
#     i=1
#     while i<=loop:
#         print("------------------------")
#         print("Student",i, "details entry")
#         print("------------------------")
#         name=input("Enter Name :")
#         ID=int(input("Enter ID :"))
#         rollno=input("Enter Roll no. :")
#         emailid=input("Enter Email id :")
#         address=input("Enter Address :")
#         mobileno=int(input("Enter MobileNo. :"))
#         print("------------------------")
#         print("Student",i,"Marks entry")
#         print("------------------------")
#         p1=int(input("Enter Marks of P1:"))
#         p2=int(input("Enter Marks of P2:"))
#         p3=int(input("Enter Marks of P3:"))
#         p4=int(input("Enter Marks of P4:"))
#         p5=int(input("Enter Marks of P5:"))
#         total=p1+p2+p3+p4+p5
#         percentage=total/5
#         if percentage>40:
#             result="Pass"
#             print("------------------------")
#             print(name,"is Pass")
#         else:
#             result="Fail"
#             print("------------------------")
#             print(name,"is Fail")
#         a.writerow([ID,name,rollno,emailid,address,mobileno,p1,p2,p3,p4,p5,total,percentage,result])
#         print("------------------------")
#         print("Record",i,"saved successfully")
#         print("------------------------")
#         i+=1
#     print("Student record has been saved successfully")
#     print("------------------------------------------")

# def read():
#     f=open("results.csv","r")
#     print(f.read())
#     f.close()




# print("-------------MENU---------------")
# print("1. CREATE")
# print("2. READ")
# print("3. UPDATE")
# print("4. DELETE")
# print("5. EXIT")
# print("-------------------------------")
# choice=int(input("Enter your choice:"))
# print("-------------------------------")

# if choice==1:
#     create()
# elif choice==2:
#     read()
# elif choice==3:
#     update()
# elif choice==4:
#     delete()
# elif choice==5:
#     exit
# else:
#     print("Invalid input")


list=[]
class marksheet:
    def __init__(self,s_name,r_no,branch,c_name,tcs_total,wt_total,mca_total,aiml_total,ssic_total):
        self.s_name=s_name
        self.r_no=r_no
        self.branch=branch
        self.c_name=c_name
        self.tcs_total=tcs_total
        self.wt_total=wt_total
        self.mca_total=mca_total
        self.aiml_total=aiml_total
        self.ssic_total=ssic_total
    def display(self):
        print("==================================================================")
        print("||              Student Name  :    ", self.s_name,"                           ||")
        print("||              Roll Number   :    ", self.r_no,"                           ||")
        print("||              Branch        :    ",self.branch,"                           ||")
        print("||              Class Name    :    ",self.c_name,"                           ||")
        print("||===============================================================||")
        print("||Subject name      :       Total Marks      :     Obtained Marks||")
        print("||TCS               :         ",100,"                      ",self.tcs_total,"     ||") 
        print("||WT                :         ",100,"                      ",self.wt_total,"     ||") 
        print("||MCA               :         ",100,"                      ",self.mca_total,"     ||") 
        print("||AIML              :         ",100,"                      ",self.aiml_total,"     ||") 
        print("||SSIC              :         ",100,"                      ",self.ssic_total,"     ||") 
        print("==================================================================")

student_name = input("Enter Student's name: ")
classname = input("Enter class name: ")
college_name = input("Enter college name: ")
roll_no = input("Enter roll number: ")
Sub1 = input("Enter TCS Marks: ")
Sub2 = input("Enter AIML Marks: ")
Sub3 = input("Enter SSIC Marks: ")
Sub4 = input("Enter MCA Marks: ")
Sub5 = input("Enter WT Marks: ")

marksheet = marksheet(student_name,roll_no, classname, college_name, Sub1, Sub2, Sub3, Sub4, Sub5)
marksheet.display()