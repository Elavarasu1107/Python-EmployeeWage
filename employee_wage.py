import random
import logging

logging.basicConfig(filename='employee_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Employee:

    def __init__(self, employee_name, employee_wage_per_hour=20, max_working_days=20,
                 max_working_hours=100):
        self.employee_name = employee_name
        self.employee_wage_per_hour = employee_wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.employee_wage_for_month = 0
        self.employee_working_days = 0
        self.employee_working_hours = 0
        self.day_with_wage = {}

    def to_print(self, days, hours, wage_for_month, wage_dict):
        """
        This function print the output generated in wage_computation function
        :param days: integer
        :param hours: integer
        :param wage_for_month: integer
        :param wage_dict: dict
        :return: None
        """
        print("\nEmployee Name: ", self.employee_name)
        print("Number of Days Employee Worked: ", days)
        print("Number of Hours Employee Worked: ", hours)
        print("Employee wage for a Month: ", wage_for_month)
        print("Day with wage: ", wage_dict, "\n")

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
            while self.employee_working_days < self.max_working_days and \
                    self.employee_working_hours < self.max_working_hours:
                employee_status = random.randint(0, 2)

                if employee_status == is_full_time:
                    employee_hours = full_time_hour
                elif employee_status == is_part_time:
                    employee_hours = part_time_hour
                else:
                    employee_hours = is_absent

                employee_wage = employee_hours * self.employee_wage_per_hour
                self.employee_wage_for_month += employee_wage
                self.employee_working_hours += employee_hours
                self.employee_working_days += 1
                self.day_with_wage.update({self.employee_working_days: employee_wage})
        except Exception as ex:
            logger.exception(ex)


class Company:

    def __init__(self, comp_name):
        self.comp_name = comp_name
        self.emp_dict = {}

    def add(self, emp_object):
        """
        This function add employee data to the company
        :return: None
        """
        try:
            self.emp_dict.update({emp_object.employee_name: emp_object})
        except Exception as ex:
            logger.exception(ex)

    def get_employee(self, emp_name):
        """
        This function retrieve the employee from the dictionary
        :param emp_name: string
        :return:
        """
        try:
            return self.emp_dict.get(emp_name)
        except Exception as ex:
            logger.exception(ex)

    def display(self):
        """
        This function display the data entered by the user if present
        :return: None
        """
        try:
            for emp_name, emp_data in self.emp_dict.items():
                print(f'{emp_name} {emp_data.employee_wage_for_month} {emp_data.employee_working_days}'
                      f' {emp_data.employee_working_hours}')
        except Exception as ex:
            logger.exception(ex)

    def update(self, name):
        """
        This function update the dictionary if key already exist
        :return: None
        """
        try:
            if name in self.emp_dict:
                wage_per_hour = int(input("Enter wage per hour: "))
                max_days = int(input("Enter max working days: "))
                max_hours = int(input("Enter max working hours: : "))
                updated_data = Employee(name, wage_per_hour, max_days, max_hours)
                updated_data.wage_computation()
                self.emp_dict.update({name: updated_data})
            else:
                print("Employee Not Found!")
        except Exception as ex:
            logger.exception(ex)

    def delete(self, name):
        """
        This function delete the data of an employee if exist
        :return: None
        """
        try:
            if name in self.emp_dict:
                self.emp_dict.pop(name)
            else:
                print("Employee Not Found!")
        except Exception as ex:
            logger.exception(ex)


class MultipleCompany:

    def __init__(self):
        self.comp_dict = {}

    def add_company(self, comp_obj):
        """
        This function add company object to company dictionary
        :param comp_obj: Type
        :return: None
        """
        try:
            self.comp_dict.update({comp_obj.comp_name: comp_obj})
        except Exception as ex:
            logger.exception(ex)

    def display_company_details(self):
        """
        his function display the employee data of a company
        :return: None
        """
        try:
            for comp_name, comp_data in self.comp_dict.items():
                print(f'Company Name:{comp_name}, Object:{comp_data.emp_dict}')
        except Exception as ex:
            logger.exception(ex)

    def get_company(self, company_name):
        """
        This function retrieve data of a Company
        :param company_name: string
        :return:
        """
        return self.comp_dict.get(company_name)

    def update_employee(self, company_name):
        """
        This function updates the employee data of a company if exist
        :param company_name: string
        :return: None
        """
        try:
            company = self.get_company(company_name)
            if company is None:
                print("Company not found")
            else:
                emp_name = input("Enter Employee Name: ")
                employee = company.emp_dict.get(emp_name)
                if employee is None:
                    print("Employee Not Found")
                else:
                    wage_per_month = int(input("Enter wage per month: "))
                    working_days = int(input("Enter working days: "))
                    working_hours = int(input("Enter working hours: : "))
                    employee.employee_wage_for_month = wage_per_month
                    employee.employee_working_days = working_days
                    employee.employee_working_hours = working_hours
        except Exception as ex:
            logger.exception(ex)

    def delete_company(self, company_name):
        """
        This function deletes the company from the dictionary
        :param company_name: string
        :return: None
        """
        try:
            if company_name in self.comp_dict:
                self.comp_dict.pop(company_name)
            else:
                print("Company Not Found")
        except Exception as ex:
            logger.exception(ex)


if __name__ == '__main__':
    try:
        company = ""
        multiple_company = MultipleCompany()
        while True:
            choice = int(input("Enter 1 to Add employee\n2 to Display\n3 to Update\n4 to Delete\n"
                               "5 to display Company Data\n6 to Update Company Data\n7 to Delete Company Data\n"
                               "0 to exit: "))
            if choice == 1:
                company_name = input("Enter Company Name: ")
                company = multiple_company.comp_dict.get(company_name)
                if company is None:
                    company = Company(company_name)
                    multiple_company.add_company(company)
                emp_name = input("Enter a Employee Name: ")
                wage_per_hour = int(input("Enter wage per hour: "))
                max_days = int(input("Enter max working days: "))
                max_hours = int(input("Enter max working hours: : "))
                employee = Employee(emp_name, wage_per_hour, max_days, max_hours)
                employee.wage_computation()
                company.add(employee)
                multiple_company.add_company(company)
            elif choice == 2:
                company.display()
            elif choice == 3:
                comp_name = input("Enter Company Name: ")
                company.update(comp_name)
            elif choice == 4:
                comp_name = input("Enter Company Name: ")
                company.delete(comp_name)
            elif choice == 5:
                multiple_company.display_company_details()
            elif choice == 6:
                comp_name = input("Enter Company Name to update: ")
                multiple_company.update_employee(comp_name)
            elif choice == 7:
                company_name = input("Enter Company Name to delete: ")
                multiple_company.delete_company(company_name)
            else:
                break
    except Exception as e:
        logger.exception(e)
