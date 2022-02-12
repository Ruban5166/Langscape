onehour = 100
above_40hours = 150 
normal_workhours = 40

max_hours = 60
monthly_salary = 0
bonabcehours = 0
worked_hours = 0
worked_hours = int(input('Enter the worked hours : '))

while worked_hours <= normal_workhours:
    monthly_salary = onehour * worked_hours
 
else:
    if worked_hours <= max_hours:
        bonabcehours = worked_hours  - normal_workhours
        monthly_salary = (bonabcehours * above_40hours) + ((normal_workhours) * onehour)
        
    elif worked_hours > max_hours:
        monthly_salary = (normal_workhours * onehour) + (20 * above_40hours)


print('monthly salary is : ', monthly_salary)