from functions import salary, hello_who

if hello_who('Max') != 'Hello, Max':
    print("Error")
elif hello_who('Max') == 'Hello, Max':
    print("Good")

if salary(4, 100) != 800:
    print("Error")
elif salary(4, 100) == 800:
    print("Good")

if hello_who('Den') != 'Hello, Den':
    print("Error")
elif hello_who('Den') == 'Hello, Den':
    print("Good")

if salary(2, 800) == 3200:
    print("Good")
elif salary(2, 800) != 3200:
    print("Error")
