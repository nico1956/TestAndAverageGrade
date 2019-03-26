#This program will ask the user to prompt 5 test scores and it will return the correspondent
#letter grade.
#
#Nico Busatto, 03/25/2019

import math
import array as arr

def main():
    iKeepGoing = 1       
    while iKeepGoing == 1:       #Program loop control.
        grade1, grade2, grade3, grade4, grade5 = inputData()
        avg = calcAverage(grade1, grade2, grade3, grade4, grade5)
        gradeLit, avgLit = determineGrade(grade1, grade2, grade3, grade4, grade5, avg)
        output(gradeLit, grade1, grade2, grade3, grade4, grade5, avg, avgLit)
        iKeepGoing = int(input("Enter 0 to exit, 1 to continue: "))

def inputData():

    grade1 = int(input("Enter the first grade: "))
    grade2 = int(input("Enter the second grade: "))
    grade3 = int(input("Enter the third grade: "))
    grade4 = int(input("Enter the fourth grade: "))
    grade5 = int(input("Enter the fifth grade: "))

    return grade1, grade2, grade3, grade4, grade5

def calcAverage(grade1,grade2,grade3,grade4,grade5):
    avg = (grade1 + grade2 + grade3 + grade4 + grade5) / 5

    return avg

def determineGrade(grade1, grade2, grade3, grade4, grade5, avg):
    i = 0
    grades = arr.array('i', [grade1, grade2, grade3, grade4, grade5])   #Grades array.
    gradeLit = [0, 1, 2, 3, 4]                                          #Grades literals array.
    avgLit = ""
  
    for grade in grades:       #Add grade to proper index position with for loop.
        if grade < 60.0:
            gradeLit[i] = "F"
        elif grade >= 60.0 and grade <= 69.9:
            gradeLit[i] = "D"
        elif grade >= 70.0 and grade <= 79.9:
            gradeLit[i] = "C"
        elif grade >= 80.0 and grade <= 89.9:
            gradeLit[i] = "B"
        else:
            gradeLit[i] = "A"
        i+=1

    if avg < 60:              #Assign avg grade to average Literal var.
        avgLit = "F"
    elif avg >= 60 and avg <= 69.9:
        avgLit = "D"
    elif avg >= 70 and avg <= 79.9:
        avgLit = "C"
    elif avg >= 80 and avg <= 89.9:
        avgLit = "B"
    else:
        avgLit = "A"
    
    return gradeLit, avgLit

def output(gradeLit, grade1, grade2, grade3, grade4, grade5, avg, avgLit):
    print("")
    print("Points\t\tGrade")                         #Print table with numeric and literal grade.
    print("---------------------")
    print(str(grade1) + "\t\t" + str(gradeLit[0]))
    print(str(grade2) + "\t\t" + str(gradeLit[1]))
    print(str(grade3) + "\t\t" + str(gradeLit[2]))
    print(str(grade4) + "\t\t" + str(gradeLit[3]))
    print(str(grade5) + "\t\t" + str(gradeLit[4]))
    print("")
    print("Average:")
    print(str(avg) + "\t\t" + str(avgLit))
    print("")
    
            
main()