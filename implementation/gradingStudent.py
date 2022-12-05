# 1. Solution: count grading student

def gradingStudent(grades):
    response = []
    for i in grades:
        sub = i%5;
        if sub < 3 or i < 38 :
            number = i
        else:
            number = (i//5 + 1) * 5
        response.append(number)
        
    return response

# Input
grades = [4, 73, 44, 68, 14, 4, 36, 38]
output = gradingStudent(grades)

# Print output
print("==================")
print("Output: " + str(output))