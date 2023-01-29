age=int(input("Enter your age(must be in between 18 to 40):"))
sex=input("Enter your sex (M or F):")
num_days=int(input("Enter number of days:"))
wage=""
if 18<= age <30  and sex == "M":
    wage = num_days * 700
    print("Your wage:",wage)

elif 18<= age <30  and sex == "F":
    wage = num_days * 750
    print("Your wage:",wage)

elif 30<= age <=40  and sex == "M":
    wage = num_days * 800
    print("Your wage:",wage)

elif  30<= age <=40  and sex == "F":
    wage = num_days * 850
    print("Your wage:",wage)

else:
    print("Enter appropriate age")




    


