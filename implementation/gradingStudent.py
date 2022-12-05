# 1. Solution: count grading student

def gradingStudent(grades):
    response = []
    for i in grades:
        sub = i%5;
        print(sub)
        if sub <= 2:
            number = i
        elif sub > 2:
            number = (i//5 + 1) * 5
            if number < 40:
                number = i
        response.append(number)
        
    return response

# Input
grades = [4, 73, 44, 68, 14, 4, 36, 38]
output = gradingStudent(grades)

# Print output
print("==================")
print("Output: " + str(output))