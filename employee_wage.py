import random
import logging

logging.basicConfig(filename='employee_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Employee:

    def __init__(self, data_dict):
        self.employee_name = data_dict.get("employee_name")
        self.employee_wage_per_hour = data_dict.get("employee_wage_per_hour")
        self.max_working_days = data_dict.get("max_working_days")
        self.max_working_hours = data_dict.get("max_working_hours")
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
                print(f'Name: {emp_name} \tMonthly Wage: {emp_data.employee_wage_for_month} \t'
                      f'No of Days Worked: {emp_data.employee_working_days} \t'
                      f'No of Hours Worked: {emp_data.employee_working_hours}')
        except Exception as ex:
            logger.exception(ex)

    def update(self, emp_obj, updated_data_dict):
        """
        This function update the dictionary if key already exist
        :return: None
        """
        try:
            emp_obj.employee_wage_for_month = updated_data_dict.get("wage_per_month")
            emp_obj.employee_working_days = updated_data_dict.get("working_days")
            emp_obj.employee_working_hours = updated_data_dict.get("working_hours")
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

    def update_employee(self, emp_obj, updated_data_dict):
        """
        This function updates the employee data of a company if exist
        :param emp_obj: object
        :param updated_data_dict: dict
        :return: None
        """
        try:
            emp_obj.employee_wage_for_month = updated_data_dict.get("wage_per_month")
            emp_obj.employee_working_days = updated_data_dict.get("working_days")
            emp_obj.employee_working_hours = updated_data_dict.get("working_hours")
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


def add_employee_function():
    """
    This function get user data to add employee
    :return: None
    """
    try:
        company_name = input("Enter Company Name: ")
        company = multiple_company.comp_dict.get(company_name)
        if company is None:
            company = Company(company_name)
            multiple_company.add_company(company)
        emp_name = input("Enter a Employee Name: ")
        wage_per_hour = int(input("Enter wage per hour: "))
        max_days = int(input("Enter max working days: "))
        max_hours = int(input("Enter max working hours: : "))
        data_dict = {"employee_name": emp_name, "employee_wage_per_hour": wage_per_hour, "max_working_days": max_days,
                     "max_working_hours": max_hours}
        employee = Employee(data_dict)
        employee.wage_computation()
        company.add(employee)
    except Exception as ex:
        logger.exception(ex)


def display_employee_function():
    """
    This function get user date to display employee data
    :return:
    """
    try:
        company_name = input("Enter Company Name: ")
        company = multiple_company.comp_dict.get(company_name)
        if company is not None:
            company.display()
    except Exception as ex:
        logger.exception(ex)


def update_employee_function():
    """
    This function gets user data to update an employee details
    :return: None
    """
    try:
        comp_name = input("Enter Company Name to update: ")
        comp_obj = multiple_company.get_company(comp_name)
        if comp_obj is None:
            print("Company not found")
        else:
            name = input("Enter employee name: ")
            employee_obj = comp_obj.get_employee(name)
            if employee_obj is None:
                print("Employee not found")
            else:
                wage_per_hour = int(input("Enter Employee Monthly Wage: "))
                working_days = int(input("Enter working days: "))
                working_hours = int(input("Enter working hours: : "))
                comp_obj.update(employee_obj, {"wage_per_month": wage_per_hour,
                                               "working_days": working_days, "working_hours": working_hours})
    except Exception as ex:
        logger.exception(ex)


def delete_employee_function():
    """
    This function get user data to delete an employee details
    :return: None
    """
    try:
        company_name = input("Enter Company Name: ")
        company = multiple_company.comp_dict.get(company_name)
        user_input = input("Enter a employee name to delete: ")
        company.delete(user_input)
    except Exception as ex:
        logger.exception(ex)


def display_company_function():
    """
    This function call the display company details function
    :return: None
    """
    try:
        multiple_company.display_company_details()
    except Exception as ex:
        logger.exception(ex)


def update_company_function():
    """
    This function gets user data to update employee of a company
    :return: None
    """
    try:
        comp_name = input("Enter Company Name to update: ")
        comp_obj = multiple_company.get_company(comp_name)
        if comp_obj is None:
            print("Company not found")
        else:
            name = input("Enter Employee name to update: ")
            employee_obj = comp_obj.get_employee(name)
            if employee_obj is None:
                print("Employee not found")
            else:
                wage_per_hour = int(input("Enter Employee Monthly Wage: "))
                working_days = int(input("Enter working days: "))
                working_hours = int(input("Enter working hours: : "))
                multiple_company.update_employee(employee_obj, {"wage_per_month": wage_per_hour,
                                                                "working_days": working_days,
                                                                "working_hours": working_hours})
    except Exception as ex:
        logger.exception(ex)


def delete_company_function():
    """
    This function get a user data to delete a company
    :return: None
    """
    try:
        company_name = input("Enter Company Name to delete: ")
        multiple_company.delete_company(company_name)
    except Exception as ex:
        logger.exception(ex)


if __name__ == '__main__':
    try:
        multiple_company = MultipleCompany()
        while True:
            choice = int(input("Enter 1 to Add employee\n2 to Display\n3 to Update Employee\n4 to Delete Employee\n"
                               "5 to display Company Data\n6 to Update Company Data\n7 to Delete Company Data\n"
                               "0 to exit: "))
            if choice == 0:
                break
            choice_dict = {1: add_employee_function, 2: display_employee_function, 3: update_employee_function,
                           4: delete_employee_function, 5: display_company_function, 6: update_company_function,
                           7: delete_company_function}
            choice_dict.get(choice)()
    except Exception as e:
        logger.exception(e)
