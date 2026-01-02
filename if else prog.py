hours = float(input("Enter total hours worked: "))
rate = float(input("Enter hourly pay rate: "))

if hours <= 40:
    pay = hours * rate
    print("Regular Pay")
    print("Total Pay:", pay)
else:
    overtime_hours = hours - 40
    regular_pay = 40 * rate
    overtime_pay = overtime_hours * rate * 1.5
    pay = regular_pay + overtime_pay

    print("Overtime Pay Applied")
    print("Overtime Hours:", overtime_hours)
    print("Total Pay:", pay)
