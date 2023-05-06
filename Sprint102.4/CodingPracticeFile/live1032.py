def top_five_grades(grades):

    top_five = []
    for student_grades in grades:
        # sort the grades in descending order
        sorted_grades = sorted(student_grades, reverse=True)
        # get the top five grades
        top_five_grades = sorted_grades[:5]
        # add the top five grades to the list
        top_five.append(top_five_grades)
    return top_five
grades =  [80, 70, 90, 85, 95, 60, 75, 85, 90, 100]


top_five = top_five_grades(grades)
print(top_five)