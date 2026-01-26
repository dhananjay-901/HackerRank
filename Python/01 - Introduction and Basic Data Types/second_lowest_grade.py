'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    # Get the number of students
    n = int(input())
    
    # Create a list to store student records
    students = []
    
    # Input student names and grades
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Find all unique grades and sort them
    unique_grades = sorted(set(student[1] for student in students))
    
    # Get the second lowest grade
    second_lowest = unique_grades[1] if len(unique_grades) > 1 else unique_grades[0]
    
    # Find all students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print each name on a new line
    for name in second_lowest_students:
        print(name)