class Department(object):


    """two class static variables"""
    dpID = 0
    dpDict = {}

    """the static method will compute and return the incremental department id."""
    @staticmethod
    def getNextDepID():
        Department.dpID += 1
        return Department.dpID

    def __init__(self,department_name, appointment_date):
        self.__department_name = department_name
        self.__appointment_date = appointment_date

        """constructor checks if the department name exists as value in the dictionary dpDict """
        if department_name in Department.dpDict.values():
            self.__department_identifier = [key for key, value in Department.dpDict.items() if value == department_name][0]
        else:
            self.__department_identifier = Department.getNextDepID()
            Department.dpDict[self.__department_identifier] = department_name

    """accessor methods"""
    def get_dep_id(self):
        return self.__department_identifier


    def get_dep_name(self):
        return self.__department_name


    def get_join_date(self):
        return self.__appointment_date

    """str method that prints as required in the pictures"""
    def __str__(self):
         return "Department ID: " + str(self.__department_identifier) + "Department Name: " + self.__department_name + "Joining Date: " + self.__appointment_date

