import random


def wage_computation():
    """
    This function computes wage of an employee
    :return: None
    """
    employee_wage_per_hour = 20
    is_full_time = 1
    is_part_time = 2
    full_time_hour = 8
    part_time_hour = 4
    employee_status = random.randint(0, 2)

    if employee_status == is_full_time:
        print("Employee is Present for a Full Day")
        employee_wage = full_time_hour * employee_wage_per_hour
        print("Employee Wage for a Day: ", employee_wage)
    elif employee_status == is_part_time:
        print("Employee is Present for a Half Day")
        employee_wage = part_time_hour * employee_wage_per_hour
        print("Employee Wage for a Day: ", employee_wage)
    else:
        print("Employee is Absent")


if __name__ == '__main__':
    wage_computation()
