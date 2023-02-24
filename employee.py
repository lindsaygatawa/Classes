class Employee(object):

    """static variable"""
    emID = 0


    """a static method that will compute and return the incremental employee id"""
    @staticmethod
    def getNextEmpID():
        Employee.emID += 1
        idLength = len(str(Employee.emID))
        Zeros = "0"*(4-idLength)
        return "EMP" + Zeros + str(Employee.emID)

    """a static method that will decrement the value of emID"""
    @staticmethod
    def decrementEmpID():
        Employee.emID -= 1

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__getNextEmpID = self.getNextEmpID()
        self.__deplst = []

    """Accessor methods"""
    def get_emp_id(self):
        return self.__getNextEmpID

    def get_fName(self):
        return self.__first_name

    def get_lName(self):
        return self.__last_name

    def get_depLst(self):
        return self.__deplst

    """mutator methods"""
    def set_fName(self, first_name):
        self.__first_name = first_name

    def set_lName(self, last_name):
        self.__last_name = last_name

    """a method that will receive a department and add it to the deplst"""
    def add_dept(self, dept):
        self.__deplst.append(dept)

    def __str__(self):
        return f"EmpID: {self.__getNextEmpID} FirstName: {self.__first_name} LastName: {self.__last_name} NumberOfDepts: {len(self.__deplst)}"
