'Hello World!'
print('Hello World!')
my_store_name = "Molnar's Goods"   
print('My store name is', my_store_name)
store_owner = "Andor"
print('Store owners name is', store_owner)
store_owner_age = 22
print('Store owners age is', store_owner_age)
me = "Andor Molnar"
print('My name is', me)
print('My favourite products are','apples','oranges','bananas')
cashier_name = "Sarah"
print('Cashier name is', cashier_name)
Cashier="Sarah"
print('Cashier is', Cashier)
cashier_age = 19
print('Cashier age is', cashier_age)
cashier_salary = 2000
print('Cashier salary is', cashier_salary)
print('That is 11.54 an hour')
cashier_hourly_wage = 11.54
print('Cashier hourly wage is', cashier_hourly_wage)
is_cashier_working_today = True
print('Is cashier working today?', is_cashier_working_today)
print(type(store_owner_age))
print(type(is_cashier_working_today))
print(type(cashier_hourly_wage))
print(isinstance(cashier_hourly_wage, (int, float)))



'My Student Report card'
print('My Student Report card')
student_name = "Andor Molnar"
print('Student name is', student_name)
student_id = ("AM1245",)
print(type(student_id), 'Student ID is', student_id)
school_name = "Greenwood High"
print('School name is', school_name)
school_address = "123 Main Street, Anytown"
print('School address is', school_address)
school_gps_coordinates = (40.7148, -74.0060)
print(type(school_gps_coordinates), 'School GPS coordinates are', school_gps_coordinates)
is_student_enrolled = True
print('Is student enrolled?', is_student_enrolled)
classes_enrolled = ("Math, Science, History, English'and Art")
print(type(classes_enrolled), 'Classes enrolled are', classes_enrolled)
student_gpa = 3.8
print(type(student_gpa), 'Student GPA is', student_gpa)

# Python remembers your exact line breaks and spacing!
store_menu = """
==============================
      MOLNAR'S SHOP MENU      
==============================
1. Check Product Stock
2. Process New Cashier Sale
3. Generate Daily Sales Report
4. Exit Program
==============================
"""

print(store_menu)

store_newsletter = """
==============================
    MOLNAR'S SHOP NEWSLETTER
==============================
Welcome to Molnar's Goods! We are excited to bring you the best products at unbeatable prices
"""
print(store_newsletter)
print('Andor' in store_owner)
print(len(store_owner))
print(store_owner[0])
print(store_owner[0:5])
print(store_owner[-1])
str_plus_str = store_owner + " " + my_store_name
print(str_plus_str)
word = "Yeah"
repeated_word = word * 3
print(repeated_word)
cashier_name_and_age = cashier_name + " is " + str(cashier_age) + " years old."
print(cashier_name_and_age)
message = "Wassup"
message += " bro"
print(message)
profile = f"Cashier {cashier_name} is {cashier_age} years old."
print(profile)
# Python executes the math inside the braces before printing!
print(f"Next year Sarah will be {cashier_age + 1} years old.") 


