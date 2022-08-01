import random
import logging

logging.basicConfig(filename='employee_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class Company:

    def __init__(self, comp_name):
        self.comp_name = comp_name
        self.emp_dict = {}

    def add(self, emp_object):
        """
        This function add employee data to the company
        :return: dict
        """
        try:
            self.emp_dict.update({emp_object.employee_name: emp_object})
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
                      f' {emp_data.employee_working_hours} {emp_data.day_with_wage}')
        except Exception as ex:
            logger.exception(ex)

    def update(self, name):
        """
        This function update the dictionary if key already exist
        :return: None
        """
        try:
            if name in self.emp_dict:
                for emp_name, emp_data in self.emp_dict.items():
                    if emp_name == name:
                        user_choice = int(input("Enter 1 to update salary\n2 to update working days\n"
                                                "3 to update working hours: "))
                        if user_choice == 1:
                            updated_sal = int(input("Enter new salary to update: "))
                            emp_data.employee_wage_for_month = updated_sal
                        elif user_choice == 2:
                            updated_days = int(input("Enter Number of working days to Update: "))
                            emp_data.employee_working_days = updated_days
                        elif user_choice == 3:
                            updated_hours = int(input("Enter Working hours to update:"))
                            emp_data.employee_working_hours = updated_hours
                        else:
                            print("Invalid Input")
            else:
                print("Employee Not Found!")
        except Exception as ex:
            logger.exception(ex)

    def delete(self, name):
        """
        This function delete the data in dictionary if key already exist
        :return:
        """
        try:
            if name in self.emp_dict:
                self.emp_dict.pop(name)
            else:
                print("Employee Not Found!")
        except Exception as ex:
            logger.exception(ex)


class Employee:

    def __init__(self, employee_name, employee_wage_per_hour=20, max_working_days=20, max_working_hours=100):
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
        :return: dict
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


if __name__ == '__main__':
    try:
        company_name = input("Enter company: ")
        status = True
        company = Company(company_name)
        while status:
            choice = int(input("Enter 1 to Add employee\n2 to Display\n3 to Update\n4 to Delete\n5 to exit: "))
            if choice == 1:
                user_name = input("Enter a Employee Name: ")
                wage_per_hour = int(input("Enter wage per hour: "))
                max_days = int(input("Enter max working days: "))
                max_hours = int(input("Enter max working hours: : "))
                ley_employee = Employee(user_name, wage_per_hour, max_days, max_hours)
                ley_employee.wage_computation()
                company.add(ley_employee)
            elif choice == 2:
                company.display()
            elif choice == 3:
                user_input = input("Enter a employee name to update: ")
                company.update(user_input)
            elif choice == 4:
                user_input = input("Enter a employee name to update: ")
                company.delete(user_input)
            else:
                status = False
    except Exception as e:
        logger.exception(e)
