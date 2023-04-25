import statistics


data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(',')
grades = list(map(int, grades))
print(min(grades))
print(max(grades))

def grade_average(grades):
    return round(sum(grades) /len(grades))

grades = [100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]
average = grade_average(grades)
print("Average of the list = ", round(average, 2))

def mean(value):
    return statistics.mean(value)
value = [100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]

answer = mean(value)
print("the mean is ", answer)

def median(value1):
    return statistics.median(value1)
value1 = [100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]

answer2 = median(value1)
print ("the median is ", answer2)


min = 14
max = 100
average1 = 53
mean1 = 53.18
median1 = 50
print("The minimum value is {}, the maximum value is {}, the average value is {}, the mean value is {}, the median value is {}".format(min, max, average1, mean1, median1))

