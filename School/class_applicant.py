'''
Define a class "Applicant" specs -
Data members -
1. ano(Admission Number)
2.name
3.Marks of 5 subjects (PCM+CS+ENG)
4.Aggregate
5. Grade
Private member functions -
grademe() to find the grade as per aggregate marks. If 80 to 100 then A, btwn 80 and 65 then B,
btwn 65 and 50 then C, and D if less than 50.
Methods are -
Enter (to enter values for data members ) and call the func aggcalc and grademe()
Result def to show the output. '''

class applicant:
    def __init__(self):
        self.ano=''
        self.name=''
        self.marks_p=0.0
        self.marks_c=0.0
        self.marks_m=0.0
        self.marks_cs=0.0
        self.marks_eng=0.0
        self.agg=0.0
        self.grade=''

    def agg_calc(self):
        self.agg=(self.marks_p+self.marks_c+self.marks_m+self.marks_cs+self.marks_eng)/5

    def __grade_me(self):       #added 2 underscores before the def name so that it remains private
        if self.agg>=80:
            self.grade='A'
        elif self.agg>=65 and self.agg<80:
            self.grade='B'
        elif self.agg>=50 and self.agg<65:
            self.grade='C'
        elif self.agg<50:
            self.grade='D'

    def enter(self): 
        self.ano=raw_input("Enter Admission number : ")
        self.name=raw_input("Enter your name : ")
        self.marks_p=input("Enter Physics marks : ")
        self.marks_c=input("Enter Chemistry marks : ")
        self.marks_m=input("Enter Maths marks : ")
        self.marks_cs=input("Enter CS Marks : ")
        self.marks_eng=input("Enter english marks : ")
        self.agg_calc()
        self.__grade_me()

    def result(self):
        print "Admission No. is : ",self.ano
        print "Name is : ",self.name
        print "Aggregate (calculated by computer) is : ",self.agg
        print "You obtained the grade : ",self.grade

obj=applicant()
n=input("Enter number of students (if 5 is entered, program will run 5 times) : ")
for i in range(n):
    obj.enter()
    obj.result()
