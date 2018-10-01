
total = 0.0;
totalHours = 0.0;
while True:
    grade = float(input('GRADE: '))
    hours = float(input('CREDIT HOURS: '))

    if(grade == -1):
        break
    else:
        total += (grade * hours)
        totalHours += hours

print(total / totalHours)
