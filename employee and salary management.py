Employees = {
    "alice": 5000,
    "bob": 60000, "charlie": 55000
}
while True:
    action = input("add,remove,update,view,exit:")
    if action == ("add"):
        Employees[input("Name: ")] = int(input("Salary: "))
    elif action == ("remove"):
        Employees.pop(input("name:")), print("notfound")
    elif action == ("update"):
        name = input("name:")
        Employees[name] = int(input("salary:")) if name in Employees else print("not found")
    elif action == ("view"):
        print(Employees)
    elif action == ("exit"):
        break









