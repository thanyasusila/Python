emp = {
    'EmpID': 'E102',
    'EmpName': 'Rahul',
    'EmpAge': 28,
    'EmpCity': 'Bangalore'
}

print("\nDictionary is:", emp)

print("\nEmployee Name is:", emp['EmpName'])
print("Employee City is:", emp['EmpCity'])

print("\nAll Keys in Dictionary")
for x in emp:
    print(x)

print("\nAll Values in Dictionary")
for x in emp:
    print(emp[x])

emp['EmpPhone'] = 9876543210

print("\nUpdated Dictionary is:", emp)

emp['EmpName'] = 'Karthik'

print("\nUpdated Dictionary is:", emp)

emp.pop('EmpAge')

print("\nUpdated Dictionary is:", emp)

print("\nLength of Dictionary is:", len(emp))

emp2 = emp.copy()

print("\nNew Dictionary is:", emp2)

emp.clear()
print("\nUpdated Dictionary is:", emp)
