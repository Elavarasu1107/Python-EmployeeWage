import random


def wage_computation():
    """
    This function used to find employee status present or absent
    :return: None
    """
    employee_status = random.randint(0, 1)

    if employee_status == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")


if __name__ == '__main__':
    wage_computation()
