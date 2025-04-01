# Dictionaries

employee = {
    'name': 'Chirag',
    'org':'PyNet Labs',
    'role':'Instructor',
    'domain':'CISCO',
    'courses':['CCNA', 'CCNP', 'CCIE']
}

print(employee['name'])
print(employee['courses'][1])
print(employee)
employee.update({'location':'Delhi'})
employee['domain'] = 'Juniper'
print(employee)
employee.pop('domain')
print(employee)