import random
import logging

logging.basicConfig(filename='employee_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class Employee:
    def __init__(self, company_name, employee_wage_per_hour, max_working_days, max_working_hours):
        self.company_name = company_name
        self.employee_wage_per_hour = employee_wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours

    def wage_computation(self):
        """
        This function computes wage of an employee
        :return: None
        """
        try:
            is_absent = 0
            is_full_time = 1
            is_part_time = 2
            full_time_hour = 8
            part_time_hour = 4
            employee_wage_for_month = 0
            employee_working_days = 0
            employee_working_hours = 0
            while employee_working_days < self.max_working_days and employee_working_hours < self.max_working_hours:
                employee_status = random.randint(0, 2)

                if employee_status == is_full_time:
                    employee_hours = full_time_hour
                    print("Employee Worked Hours: ", employee_hours)
                elif employee_status == is_part_time:
                    employee_hours = part_time_hour
                    print("Employee Worked Hours: ", employee_hours)
                else:
                    employee_hours = is_absent
                    print("Employee is Absent")

                employee_wage = employee_hours * self.employee_wage_per_hour
                employee_wage_for_month += employee_wage
                employee_working_hours += employee_hours
                employee_working_days += 1
            print("\nCompany Name: ", self.company_name)
            print("Number of Days Employee Worked: ", employee_working_days)
            print("Number of Hours Employee Worked: ", employee_working_hours)
            print("Employee wage for a Month: ", employee_wage_for_month)
        except Exception as ex:
            logging.error("Exception: ", ex)


if __name__ == '__main__':
    employee_one_wage = Employee("Tata", 20, 20, 100)
    employee_one_wage.wage_computation()
    print()
    employee_two_wage = Employee("Leyland", 20, 25, 105)
    employee_two_wage.wage_computation()