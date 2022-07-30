import random
import logging

logging.basicConfig(filename='employee_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class Company:
    # company_wage_data = {}

    def __init__(self, comp_name, employee_data):
        self.comp_name = comp_name
        self.employee_data = employee_data
        # self.company_wage_data = {}

    def company_dict(self):
        """
        This function add employee data to the company
        :return: dict
        """
        try:
            company_wage_data = {}
            company_wage_data.update({self.comp_name: self.employee_data})
            return company_wage_data
        except Exception as ex:
            logging.exception("Exception: ", ex)


class Employee:

    def __init__(self, employee_name, employee_wage_per_hour, max_working_days, max_working_hours,
                 salary_details_dict, company_name):
        self.employee_name = employee_name
        self.employee_wage_per_hour = employee_wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.salary_details_dict = salary_details_dict
        self.company_name = company_name

    def salary_dict(self, employee_name, emp_wage):
        """
        This function adds company name and employee's monthly wage to dictionary
        :param employee_name: string value
        :param emp_wage: integer value
        :return: dict
        """
        try:
            self.salary_details_dict.update({employee_name: emp_wage})
            return self.salary_details_dict
        except Exception as ex:
            logging.exception("Exception: ", ex)

    def to_print(self, days, hours, wage_for_month):
        """
        This function print the output generated in wage_computation function
        :param days: integer
        :param hours: integer
        :param wage_for_month: integer
        :return: None
        """
        print("\nEmployee Name: ", self.employee_name)
        print("Number of Days Employee Worked: ", days)
        print("Number of Hours Employee Worked: ", hours)
        print("Employee wage for a Month: ", wage_for_month)

    def wage_computation(self):
        """
        This function computes wage of an employee
        :return: dict
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
                elif employee_status == is_part_time:
                    employee_hours = part_time_hour
                else:
                    employee_hours = is_absent

                employee_wage = employee_hours * self.employee_wage_per_hour
                employee_wage_for_month += employee_wage
                employee_working_hours += employee_hours
                employee_working_days += 1

            salary_data = self.salary_dict(self.employee_name, employee_wage_for_month)
            self.to_print(employee_working_days, employee_working_hours, employee_wage_for_month)
            return salary_data
        except Exception as ex:
            logging.error("Exception: ", ex)


if __name__ == '__main__':
    try:
        leyland_emp_one = Employee("Elavarasu", 20, 20, 100, {}, "Leyland").wage_computation()
        leyland_emp_two = Employee("Nantha", 20, 20, 100, {}, "Leyland").wage_computation()
        tata_emp_one = Employee("Senthil", 25, 20, 105, {}, "Tata").wage_computation()
        tata_emp_two = Employee("Prithiv", 25, 20, 105, {}, "Tata").wage_computation()
        leyland_emp_one.update(leyland_emp_two)
        tata_emp_one.update(tata_emp_two)
        leyland = Company("Leyland", leyland_emp_one).company_dict()
        tata = Company("Tata", tata_emp_one).company_dict()
        print(leyland, tata)
    except Exception as e:
        logging.error("Exception: ", e)
