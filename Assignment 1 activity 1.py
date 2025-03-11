# Accept marks from the user
marks = int(input("Enter marks(1-100): "))
#determine grades based on marks
if marks >90 and marks <=100:
    grades="A"
elif marks >80 and marks <=90:
    grades="B"
elif marks >80 and marks <70:
     grades="C"
elif marks >70 and marks< 60:
    grades="D"
elif marks >60 and marks <=50: 
    grades="E"
elif marks >=50:
    grades = "F"
else : 
    grades= "invalid markes"
print("Grades:",grades)