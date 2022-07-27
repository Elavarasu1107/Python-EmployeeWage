import random


def wage_computation():
    """
    This function computes wage of an employee
    :return: None
    """
    employee_wage_per_hour = 20
    is_full_time = 1
    full_time_hour = 8
    employee_status = random.randint(0, 1)
    if employee_status == is_full_time:
        print("Employee is Present")
        employee_wage = full_time_hour * employee_wage_per_hour
        print("Employee Wage for a Day: ", employee_wage)
    else:
        print("Employee is Absent")


if __name__ == '__main__':
    wage_computation()
