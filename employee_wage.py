import random
import logging

logging.basicConfig(filename='employee_log.log', encoding='utf-8', level=logging.DEBUG)


class Employee:
    def __init__(self, part_time_hour, full_time_hour, employee_wage_per_hour, max_working_days, max_working_hours):
        self.part_time_hour = part_time_hour
        self.full_time_hour = full_time_hour
        self.employee_wage_per_hour = employee_wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def wage_computation(self):
        """
        This function computes wage of an employee
        :return: None
        """
        is_absent = 0
        is_full_time = 1
        is_part_time = 2
        employee_wage_for_month = 0
        employee_working_days = 0
        employee_working_hours = 0
        try:
            while employee_working_days < self.max_working_days and employee_working_hours < self.max_working_hours:
                employee_status = random.randint(0, 2)

                if employee_status == is_full_time:
                    employee_wage = self.full_time_hour * self.employee_wage_per_hour
                    employee_hours = self.full_time_hour
                    print("Employee Worked Full Day: ", employee_wage)
                elif employee_status == is_part_time:
                    employee_wage = self.part_time_hour * self.employee_wage_per_hour
                    employee_hours = self.part_time_hour
                    print("Employee Worked Half Day: ", employee_wage)
                else:
                    print("Employee is Absent")
                    employee_wage = is_absent * self.employee_wage_per_hour
                    employee_hours = is_absent

                employee_wage_for_month += employee_wage
                employee_working_hours += employee_hours
                employee_working_days += 1
            print("\nNumber of Days Employee Worked: ", employee_working_days)
            print("Number of Hours Employee Worked: ", employee_working_hours)
            print("Employee wage for a Month: ", employee_wage_for_month)
        except Exception as ex:
            logging.exception("Exception: ", ex)


if __name__ == '__main__':
    full_time_hour = 8
    part_time_hour = 4
    employee_wage_per_hour = 20
    max_working_days = 20
    max_working_hours = 100
    emp_wage = Employee(part_time_hour, full_time_hour, employee_wage_per_hour, max_working_days, max_working_hours)
    emp_wage.wage_computation()
