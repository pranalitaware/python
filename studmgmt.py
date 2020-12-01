import csv

class Student:
    def __init__(self,rollno,name,dob,cid):
        self.rollno=rollno
        self.name=name
        self.dob=dob
        self.cid=cid
        with open('stud.csv','a', newline='') as f:
            fieldnames = ['rollno','name','dob','cid']
            thewriter=csv.DictWriter(f, fieldnames=fieldnames)
            thewriter.writerow({'rollno':self.rollno, 'name':self.name,'dob':self.dob,'cid':self.cid})
            
    def viewstudent():
        with open('stud.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    def applycourse():
        c=0
        x=int(input("Select the course id you want to apply for:\n"))
        roll=int(input("Enter your roll no."))
        with open('stud.csv','r+',newline=None) as f:
            fieldnames = ['rollno','name','dob','cid']
            thewriter=csv.DictWriter(f, fieldnames=fieldnames)
            thereader=csv.DictReader(f, fieldnames=fieldnames)
            for row in thereader:
                if row['rollno'] == str(roll):
                    print("updating")
                    #thewriter.writerow({'cid':x})
                    print("Successfully applied for the course")
                    c=c+1
            if(c==0):
                print("not registered!!")

                
class Course:
    def __init__(self,cid,cname,duration,fees):
        self.cid=cid
        self.cname=cname
        self.duration=duration
        self.fees=fees
        with open('course.csv','a', newline='') as f:
            thewriter=csv.writer(f)
            thewriter.writerow([self.cid,self.cname,self.duration,self.fees])
        
    def viewcourses():
        with open('course.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

if __name__ == "__main__":
    
    while True:
        x=int(input("\nWelcome to the student management system \n Tell us who you are:\n 1.Student\n 2.Admin \n"))
        if(x==1):
            print("Welcome student:\n 1.Register\n 2.view course\n 3.Apply for a course\n 4.exit\n")
            choice=int(input())
            if(choice==1):
                rollno=int(input("enter roll no. : "))
                name=input("enter name : ")
                dob=input("enter dob : ")
                cid=int(input("enter cid : "))
                print("Successfully registered!!")
                obj=Student(rollno,name,dob,cid)
            elif(choice==2):
                Course.viewcourses()

            elif(choice==3):
                Course.viewcourses()
                Student.applycourse()

            elif(choice==4):
                break
   
        elif(x==2):
           print("\nWelcome admin:\n1.Add a new course\n2.View courses\n3.View student\n4.exit\n")
           choice=int(input())
           if(choice==1):
               cid=int(input("enter cid.: "))
               cname=input("enter course name: ")
               duration=int(input("enter course duration in years: "))
               fees=int(input("enter fees: "))
               print("Successfully added a course!!")
               obj=Course(cid,cname,duration,fees)
                
           elif(choice==2):
                Course.viewcourses()

           elif(choice==3):
                Student.viewstudent()

           elif(choice==4):
                break

        else:
            print("Enter a valid choice")
           
