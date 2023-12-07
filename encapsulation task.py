#encapsulation task
class Parent:
    child_age=15 #public attribute
    _child_age=15 #protected attribute
    __child_age=15 #private attribute
    def meth_1(self):
        print(self.child_age) #accessing public attribute inside the class
        print(self._child_age) #accessing protected attribute inside the class
        print(self.__child_age) #accessing private attribute inside the class
class Child(Parent):
    def meth_2(self):
        print(self.child_age) #accessing public attribute using inheritance method
        print(self._child_age) #accessing protected attribute using inheritance method
        print(self._Parent__child_age) #accessing private attribute using inheritance method                    
obj_1=Parent()
obj_1.meth_1()
print(obj_1.child_age) #accessing public attribute outside the class
print(obj_1._child_age) #we can also access protected attribute outside of the class but we should not
#print(obj_1.__child_age) --- we should not access the private attribute outise the class
obj_2=Child()
obj_2.meth_2()
print(obj_2.child_age) #accessing public attribute outside the class by referring to another object
print(obj_2._child_age) #we can also access protected attribute outside of the class by referring to another object but we should not
#print(obj_2.__child_age) --- we should not access the private attribute outise the class
