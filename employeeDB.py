import csv
import copy
import datetime as dt

from employee import Employee
from department import Department

class EmployeeDB(object):

    def __init__(self, filename):
        self.__filename = filename
        self.__emp_dict = {}
        self.__emp_obj_lst = []


    def read_file(self):
      with open(self.__filename, "r") as file:
          reader = csv.reader(file)
          for row in reader:
              emp_id = row[0]
              emp_data = row[1:]

              self.__emp_dict[emp_id] = emp_data
      print(f'{len(self.__emp_dict)} records added to the dictionary.')

    def get_obj_lst(self):
        return self.__emp_obj_lst

    def emp_exists(self, emp_object):
        count = 0
        for obj in self.__emp_obj_lst:
            obj : Employee

            if obj.get_fName() == emp_object.get_fName() and obj.get_lName() == emp_object.get_lName():
                return count
            count += 1
        return -1

    def add_emp_data(self):
        """incremental employee id"""
        emp_id = 1
        for emp in self.__emp_dict.values():
            """new employee object"""
            print(emp)
            if emp[0] == "FirstName":
                continue
            emp_obj = Employee(emp[0], emp[1])
            """check if employee already exists in the list"""
            index = self.emp_exists(emp_obj)
            if index == -1:
                """if employee is unique as per the above method then append it to the list"""
                self.__emp_obj_lst.append(emp_obj)
                """adding a department object to its respective employee"""

                emp_dept = Department(emp[2], emp[3])
                emp_obj.add_dept(emp_dept)
                """adding 1 to emp_id since its unique"""
                emp_id += 1
            else:
                emp_obj = self.__emp_obj_lst[index]
                emp_dept = Department(emp[2], emp[3])
                emp_obj.add_dept(emp_dept)
                """remove 1 if obj already exists"""
                emp_obj.decrementEmpID()
        print(f"{emp_id -1} unique employees added to the database.")

    def print_cross_emp(self):
        count = 0
        for emp in self.__emp_obj_lst:
            emp : Employee

            if len(emp.get_depLst()) > 1:
                count += 1
                print(f"Record {count} found!")
                print(emp)
                print(f"{len(emp.get_depLst())} Appointments found:")
                for dept in emp.get_depLst():
                    print(dept)
        if count == 0:
            print("No cross_appointed employees found. ")


    def remove_emp(self,emp_id):
        emp_obj = None
        for obj in self.__emp_obj_lst:
            if obj.get_emp_id() == emp_id:
                emp_obj = obj
                print("Successfully removed employee with employee id: ", emp_id)
            else:
                print("Employee not found?")

    def date_diff(self, emp_id):
        emp_obj = None
        for obj in self.__emp_obj_lst:
            if obj.get_emp_id() == emp_id:
                emp_obj = obj
                break
            if emp_obj is None:
                print("Employee not found.")
            elif len(emp_obj.get_depts()) < 1:
                print("Employee is not cross-appointed.")
            else:
                dept_dates = [dept.get_join_date() for dept in emp_obj.get_depts()]
                dept_dates.sort()
                max_diff = (dept_dates[-1] - dept_dates[0]).days
                print(f"Maximum difference between joining dates:{max_diff} days.")

                
def main():
    comp = EmployeeDB("employeeInfo.csv")
    print("******************************************************************************")
    comp.read_file()
    print("******************************************************************************")
    comp.add_emp_data()
    print("******************************************************************************")
    comp.print_cross_emp()
    print("******************************************************************************")
    str_id = input(f"Enter an EMP ID to be removed from the available {len(comp.get_obj_lst())} records: ")
    comp.remove_emp(str_id)
    print(f"Total employee objects remaining in the list are: {len(comp.get_obj_lst())}")
    print("******************************************************************************")
    str_id = input(f"Enter an EMP ID to compute days between cross-appointments: ")
    comp.date_diff(str_id)
    print("******************************************************************************")


if __name__ == "__main__":
    main()
