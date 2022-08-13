import pytest
from employee_wage import Employee, Company, MultipleCompany


@pytest.fixture
def employee_object():
    return Employee({"employee_name": "Ela", "employee_wage_per_hour": 20, "max_working_days": 20,
                     "max_working_hours": 100})


@pytest.fixture
def company():
    return Company("Company")


@pytest.fixture
def multiple_company():
    return MultipleCompany()


def test_wage_computation(employee_object):
    employee_object.wage_computation()
    assert isinstance(employee_object.employee_wage_for_month, int)


def test_add_employee(employee_object, company):
    assert len(company.emp_dict) == 0
    company.add(employee_object)
    assert len(company.emp_dict) == 1


def test_get_employee(employee_object, company):
    assert len(company.emp_dict) == 0
    company.add(employee_object)
    actual = company.get_employee("Ela")
    assert actual == employee_object


def test_update_employee(employee_object, company):
    assert len(company.emp_dict) == 0
    company.add(employee_object)
    updated_dict = {"wage_per_month": 2000, "working_days": 15, "working_hours": 80}
    company.update(employee_object, updated_dict)
    assert employee_object.employee_wage_for_month == 2000
    assert employee_object.employee_working_days == 15
    assert employee_object.employee_working_hours == 80


def test_delete_employee(employee_object, company):
    company.add(employee_object)
    assert len(company.emp_dict) == 1
    company.delete("Ela")
    assert len(company.emp_dict) == 0


def test_add_company(employee_object, company, multiple_company):
    company.add(employee_object)
    assert len(multiple_company.comp_dict) == 0
    multiple_company.add_company(company)
    assert len(multiple_company.comp_dict) == 1
    company1 = Company("Company1")
    company1.add(employee_object)
    assert len(multiple_company.comp_dict) == 1
    multiple_company.add_company(company1)
    assert len(multiple_company.comp_dict) == 2


def test_get_company(employee_object, company, multiple_company):
    company.add(employee_object)
    multiple_company.add_company(company)
    actual = multiple_company.get_company("Company")
    assert actual == company


def test_delete_company(employee_object, company, multiple_company):
    company.add(employee_object)
    multiple_company.add_company(company)
    assert len(multiple_company.comp_dict) == 1
    multiple_company.delete_company("Company")
    assert len(multiple_company.comp_dict) == 0
