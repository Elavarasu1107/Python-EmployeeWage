import random


def wage_computation():
    """
    This function computes wage of an employee
    :return: None
    """
    is_absent = 0
    is_full_time = 1
    is_part_time = 2
    full_time_hour = 8
    part_time_hour = 4
    employee_wage_per_hour = 20
    max_working_days = 20
    max_working_hours = 100
    employee_wage_for_month = 0
    employee_working_days = 0
    employee_working_hours = 0

    while employee_working_days < max_working_days and employee_working_hours <= max_working_hours:
        employee_status = random.randint(0, 2)

        if employee_status == is_full_time:
            employee_wage = full_time_hour * employee_wage_per_hour
            employee_hours = full_time_hour
            print("Employee Worked Full Day: ", employee_wage)
        elif employee_status == is_part_time:
            employee_wage = part_time_hour * employee_wage_per_hour
            employee_hours = part_time_hour
            print("Employee Worked Half Day: ", employee_wage)
        else:
            print("Employee is Absent")
            employee_wage = is_absent * employee_wage_per_hour
            employee_hours = is_absent

        employee_wage_for_month += employee_wage
        employee_working_hours += employee_hours
        employee_working_days += 1
    print("\nNumber of Days Employee Worked: ", employee_working_days)
    print("Number of Hours Employee Worked: ", employee_working_hours)
    print("Employee wage for a Month: ", employee_wage_for_month)


if __name__ == '__main__':
    wage_computation()
