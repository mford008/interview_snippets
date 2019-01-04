grades = [4, 73, 67, 38, 33]


def gradingStudents(grades):
    # Create new array
    final_grades = []
    for grade in grades:
        # Begin selection at value we know will be rounded up
        if grade >= 38:
            # Identify difference between grade and next multiple of 5
            if grade % 5 >= 3:
                # If so, add difference to grade to round up
                grade += (5 - grade % 5)
            final_grades.append(grade)
        else:
            final_grades.append(grade)
    print(final_grades)
    # return final_grades

gradingStudents(grades)
