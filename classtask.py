#create an employee class and add details of employee  using three deferent variables and access that variables in all possible ways.
class employee:
    company_name="Marolix technology Pvt Ltd"#using static variable
    def __init__(self,name,id,domain,salary):
        self.name=name
        self.id=id
        self.domain=domain
        self.salary=salary
    def employee_details(self):#using instance variable
        print(self.name)
        print(self.id)
        print(self.domain)
        print(self.salary)
    def emp_credentials(self):#using local variable
        emp_surname="Shaik"
        Date_of_Birth="18 Oct 1998"
        print(emp_surname)
        print(Date_of_Birth)
ref_emp=employee(name="Azgar Ali",id="02068",domain="python",salary="25000")
print(employee.company_name)
ref_emp.employee_details()
ref_emp.emp_credentials()

