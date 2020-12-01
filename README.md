# python
python applications 1:
Problem Statement:
XYZ College has come up with the requirement of developing a console based application to basically manage the details of all the students who register with the college.You need to develop a standalone console based application using Python which will be responsible for taking care of the above requirement. You can use any database of choice for this case study.
When the application is loaded, it will present the user with the following options:

Welcome to SMS (Student Management System)
Tell us who you are:
1.Student
2.Admin

If (1. i.e. student is selected) then the following options will be shown:
Welcome Student
1.Register
2.View Courses
3.Apply for a Course

If (2. i.e. admin is selected) then the following options will be shown:
Welcome Admin
1.Add a new Course
2.View Courses
3.View Student

Now what are the details we need to collect for registering a student, adding a course or applying for a course, refer to the suggested table structure below:

Student Table
ROLLNO (PK)
NAME
DATEOFBIRTH
COURSEID (FK)

Course Table
COURSEID (PK)
COURSENAME
DURATION
FEES
