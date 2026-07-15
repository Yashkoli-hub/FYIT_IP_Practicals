basic = float(input("Enter your basic salary:"))

hra = basic * 0.20
da  = basic * 0.10
net = basic + hra + da

print("\nSalary Breakdown")
print("Basic Salary:", basic)
print("HRA :", hra)
print("DA:", da)
print("Net Salary:", net)
