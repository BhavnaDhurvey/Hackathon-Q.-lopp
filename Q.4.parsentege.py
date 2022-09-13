physics=int(input("enter the number"))
chemistry=int(input("enter the number"))
biology=int(input("enter the number"))
methematic=int(input("enter the number"))
computer=int(input("enter the number"))
percentege=physics+chemistry+biology+methematic+computer
percentege*100/500
if percentege>=90:
    print("Grade A")
if percentege>=80:
    print("Grede B")
if percentege>=70:
    print("Grede C")
if percentege>=60:
    print("Grede D")
if percentege>=40:
    print("Grede E")
else:
    print("Grede F")



