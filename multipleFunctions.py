class multipleFunctions:
    def Subfields():
        list1 = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for itemdata in list1:
            print(itemdata)

    def OddEven():
        num = int(input("Enter a number:"))
        if((num%2) == 0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")

    def Eligible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        
        if (gender == "Male" and age >= 21) or (gender == "Female" and age >= 18):
            print("Eligible")
        else:
            print("Not Eligible")
        
    def Percentage():
        subject1 = int(input("Subject1:"))
        subject2 = int(input("Subject2:"))
        subject3 = int(input("Subject3:"))
        subject4 = int(input("Subject4:"))
        subject5 = int(input("Subject5:"))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = total/5
        print("Total:",total)
        print("Percentage:",percentage)

    def Triangle():
        height = int(input("height:"))
        breadth = int(input("breadth:"))
        areaoftriangle = (height * breadth)/2
        print("Area of Triangle:", areaoftriangle)
        height1 = int(input("height1:"))
        height2 = int(input("height2:"))
        breadth1 = int(input("breadth1:"))
        perimeteroftriangle = height1 + height2 +  breadth1
        print("Perimeter of Triangle:", perimeteroftriangle)







    

    