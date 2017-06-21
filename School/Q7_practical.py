'''
Define a class student in Python with following specs -
Instance Variables :
Roll number, name
Methods:
Getdata() - to input roll number and name
Printdata()- to display roll number and name

Define another class marks which is derived from student class
Instance vairable
Marks in 5 subjects
Methods:
Inputdata() to call Getdata() and input 5 subject marks.
Outdata()- To call printdata() and to display 5 subject marks.
'''

class student:
    def __init__(self):
        self.roll=0.0
        self.name=''

    def Getdata(self):
        self.roll=input("Enter your roll no. : ")
        self.name=raw_input("Enter your name : ")
        self.marks_p=input("Enter your physics marks : ")
        self.marks_c=input("Enter your chemistry marks : ")
        self.marks_m=input("Enter your maths marks : ")
        self.marks_cs=input("Enter your cs marks : ")
        self.marks_english=input("Enter your english marks : ")        

    def Printdata(self):
        print "Roll Number is : ",self.roll
        print "Name is : ",self.name
        
obj=student()
obj.Getdata()
obj.Printdata()

#first part of question is complete.

class marks:
    def __init__(self):
        self.marks_p=0.0
        self.marks_c=0.0
        self.marks_m=0.0
        self.marks_cs=0.0
        self.marks_english=0.0
