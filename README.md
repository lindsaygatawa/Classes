# Classes
The main objective of this project is to learn how to create classes in python, to open and read files and store the contents in suitable data structures and use it accordingly.
Please feel free to commit and checkout instructions below of each class first😊

There are three classes in this project and each of them has seperate specifications:

#Department Class
You need to write a Department class that maintains the information about the university departments.
You need to write your code in the given Department class. It must contain the following:
1. There will be two static class variables dpID (int) and dpDict (dictionary). dpID will be used
to maintain an incremental department identifier (initialized to 0). dpDict will be used to
maintain an association between department identifiers (keys) and department names (values)
as a dictionary.
2. The getNextDepID method (a static method) will compute and return the incremental department id.
3. The class constructor will receive the department name and the appointment date and use them
to create an instance of the class. It will also add a department identifier to the instance. You
will hide all three instance variables (make them private by adding the double underscore
preceding the variable names). The constructor will check if the department name exists as a
value in the dictionary dpDict. If it does, use the respective key (existing id) as the department
id. Otherwise, use the getNextDepID method to generate a new incremental department id;
also add this department name-id pair to the dictionary dpDict.
4. There will be three accessor methods: get_dep_id, get_dep_name, and get_ join_date. These
methods will return the department id, department name, and joining date respectively.
5. The __str__ method will print the Department information

#Employee class
You need to write an Employee class that maintains the information about the university employees.
You need to write your code in the given Employee class. It must contain the following:
1. There will be one static class variables emID (int). emID will be used to maintain the
incremental employee id (initialized to 0).
2. The getNextEmpID method (a static method) will compute and return the incremental employee
id. The returned employee id will be a string derived from emID in the format EMPXXXX,
where XXXX is the incremental emID. Examples: This method will return EMP0001 for emID
1. This method will return EMP1000 for emID 1000.
3. The decrementEmpID method (a static method) will decrement the current value of the class
variable emID by 1.
4. The class constructor will receive the first name and the last name of the employee and use
them to create an instance of the class. In addition, the instance will store the incremental
employee id generated using the getNextEmpID method. It will also initialize an empty
department object list depLst. You will hide all four instance variables (make them private
by adding the double underscore preceding the variable names).
5. There will be four accessor methods: get_emp_id, get_ f Name, get_lName, and get_depLst.
These methods will return the employee id, first name, last name, and a list of department
objects respectively.
6. There will be two mutator methods: set_ f Name and set_lName. Each of these methods
receives a string and sets the first name and the last name respectively.
7. The add_dept receives a department object and adds it to the department object list depLst.
8. The __str__ method will print the Employee information

#EmployeeDB class
You need to write an EmployeeDB class that maintains the database of all university employees and
departments. As part of this assignment, you have been given an EmployeeDB class with driver code.
You need to write your code in the given EmployeeDB class. It must contain:
1. The class constructor will receive the filename and use it to create an instance of the class. It
will also initialize an empty employee dictionary emp_dict and an empty employee object list
emp_ob j_list. You will hide all three instance variables (make them private by adding the
double underscore preceding the variable names).
2. The read_file method will read the csv file (filename was passed to the constructor). It will
store the file contents in emp_dict. For each row of the csv file, cells in the first column
(SNo) will be added as keys. The cells from the remaining columns will be added as values
in the dictionary in the form of a list. In the end, this method will print ‘xx records added
to the dictionary.’, where xx is the length of the dictionary. Example: The first record of the
employeeInfo.csv file is “1, Will, Bradshaw, Biology, 2016-06-04”. The read_file will save
this record as emp_dict[‘1’] = [‘Will’, ‘Bradshaw’, ‘Biology’, ‘2016-06-04’].
3. There will be one accessor method: get_ob j_lst. It will return the employee object list
emp_ob j_list.
4. The emp_exists method will receive an employee object and check if the emp_obj_list contains
another employee object with identical attribute values (first name, and last name). It will
return the index of the identical employee object if found, otherwise, it will return -1.
5. The add_emp_data method will read the employee dictionary emp_dict and add the unique
employees to the employee object list emp_obj_list. Please note that for each record (value as
a list) in the dictionary, the first two attribute values (first name, and last name - all strings)
represent an employee object. The remaining two attribute values represent a department object
(department name - string, and joining date - string). This method will use the emp_exists
method to check if the employee object with identical values already exists in the emp_obj_list
or not. If the current record represents a unique employee not currently in the emp_obj_list,
then a new employee object will be added to the emp_obj_list. In addition, you will add the
department object to its respective employee object. To summarize, for each record in the
dictionary:
(a) You create a new employee object (this will generate a new incremental employee id).
(b) You add the newly created employee object to the emp_obj_list if it does not exist in the
list already.
(c) In case the employee object already exists in the list, the newly incremental employee id
should be decremented (because we never used the newly created employee object). You
use the decrementEmpID method of the Employee class to decrement the emID by 1.
(d) You create and add the department object to its respective employee object using the
add_dept method of the Employee class.
(e) In the end, this method will print ‘xx unique employees added to the database.’, where
xx is the number of unique employees added to the emp_obj_list.
6. The print_cross_emp method will print the information of employees who are cross−appointed
in more than one department. If such records are found in the emp_ob j_list, the method will
print Record XX found!, where XX is the number of such records found so far. Following
this print statement, the method will print the employee object. The method will then print
4
Appointments found: followed by the respective department objects. To print the employee
objects and department objects, the method should make use of their respective __str__
methods. The printing format can be seen in the included screenshots.
7. The remove_emp method will receive an employee id and remove the employee if it exists
in the emp_obj_list. If the employee is found, then it will remove the employee object and
print ‘Successfully removed employee with employee id: xx’, where xx is the input employee
id. Otherwise, it will print ‘Employee not found!’.
8. The date_diff method will receive an employee id and check if the employee is cross-appointed
or not i.e., the employee is appointed in more than one department or not. If the employee is
not cross-appointed, then the method will print Employee is not cross-appointed.. Otherwise,
the method will compute the maximum differences between the joining dates of the crossappointments. The maximum difference is defined as the number of days between the
first appointment and the most recent appointment of an employee. The method will print
Difference between cross-appointments (in days) is: XX, where XX is the maximum difference.
