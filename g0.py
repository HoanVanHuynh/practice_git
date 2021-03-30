self_employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
        ]
   

def _create_employee( id, name, role): # This unpacks the Dict before sending it
    # so it can be received be the function as separate variables.
        address = id
        employee_role = name
        payroll_policy = role
        return address, employee_role, payroll_policy

def employees():
        return [_create_employee(**data) for data in self_employees]   
        
#print(employees())        

def unpack_it(x,y,z):
    print(x)
    print(y)
    print(z)
data = ['NoOneLikes', 'FeelingStupiderThanTheNextPerson']

print(unpack_it(*data))    