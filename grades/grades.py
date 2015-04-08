def grade_average(grade1,grade2,grade3) :
    """(num,num,num) -> num
    >>>grade_average(10,20,30)
    20
    >>>grade_average(70,40,60)
    56.6666666
    
    Returns the average of grade1, grade2, grade3
    grade1, grade2, grade3 are a number in the range 0-100
    """
    grade_list = (grade1, grade2, grade3)
    return sum(grade_list)/3


def top_grade_average(grade1, grade2, grade3, grade4) :
    """(num,num,num,num) -> num
    >>> top_grade_average(10,20,30,40)
    30
    >>> top_grade_average(70,10,50,40)
    43.33333333336

    Returns the average of the top 3 grades

    grade1, grade2, grade3, grade4 are a number in the range 0-100
    """
    grade_list = (grade1, grade2, grade3, grade4)
    sorted_grades_list = sorted(grade_list)
    return grade_average(sorted_grades_list[1],sorted_grades_list[2],sorted_grades_list[3])
