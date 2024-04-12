class Employee:
    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """

    def __init__(self, emp_id: int, name: str, position: str, salary: float):
        self._emp_id = emp_id
        self._name = name
        self._position = position
        self._salary = salary
        self._tasks = []

    def get_emp_id(self) -> int:
        """Get the employee's ID.

        Returns
        -------
        int
            The employee's ID.
        """
        return self._emp_id

    def set_emp_id(self, emp_id: int):
        """Set the employee's ID.

        Parameters
        ----------
        emp_id : int
            The new employee ID.
        """
        self._emp_id = emp_id

    def get_name(self) -> str:
        """Get the employee's name.

        Returns
        -------
        str
            The employee's name.
        """
        return self._name

    def set_name(self, name: str):
        """Set the employee's name.

        Parameters
        ----------
        name : str
            The new employee name.
        """
        self._name = name

    def get_position(self) -> str:
        """Get the employee's position.

        Returns
        -------
        str
            The employee's position.
        """
        return self._position

    def set_position(self, position: str):
        """Set the employee's position.

        Parameters
        ----------
        position : str
            The new employee position.
        """
        self._position = position

    def get_salary(self) -> float:
        """Get the employee's salary.

        Returns
        -------
        float
            The employee's salary.
        """
        return self._salary

    def set_salary(self, salary: float):
        """Set the employee's salary.

        Parameters
        ----------
        salary : float
            The new employee salary.
        """
        self._salary = salary

    def get_tasks(self) -> list:
        """Get the list of tasks assigned to the employee.

        Returns
        -------
        list
            List of tasks assigned to the employee.
        """
        return self._tasks

    def add_task(self, task: str):
        """Add a task to the employee's task list.

        Parameters
        ----------
        task : str
            The task to be added.
        """
        self._tasks.append(task)

    def remove_task(self, task: str):
        """Remove a task from the employee's task list.

        Parameters
        ----------
        task : str
            The task to be removed.
        """
        if task in self._tasks:
            self._tasks.remove(task)
        else:
            print("Task not found in the employee's task list.")

def main():
    # TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for emp_id.")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for name.")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for position.")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for salary.")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

    # Task Management Test
    print("=================================================================")
    print("Test Case 3: Task Management.")
    print("=================================================================")
    employee1.add_task("Attend to guests at the reception")
    employee1.add_task("Manage bookings")
    tasks = employee1.get_tasks()
    if "Attend to guests at the reception" in tasks and "Manage bookings" in tasks:
        print("Test PASS. Tasks have been correctly added.")
    else:
        print("Test FAIL. Check the methods add_task() and get_tasks().")

    employee1.remove_task("Manage bookings")
    tasks = employee1.get_tasks()
    if "Manage bookings" not in tasks:
        print("Test PASS. Task has been correctly removed.")
    else:
        print("Test FAIL. Check the method remove_task().")

if __name__ == "__main__":
    main()
