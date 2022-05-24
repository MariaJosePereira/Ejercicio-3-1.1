
# Online Python - IDE, Editor, Compiler, Interpreter

money = float(input("how much money you want to deposit:  "))

remain = money // 500
money = money % 500

if money >= 500: 
    remain = money // 500
    print("There are"  +str (remain) +  "500 dollar bills")
    money = money % 500
if money >= 200:
    remain = money // 200
    print("There are"  +str  (remain) +  "200 dollar bills")
    money = money % 200
    
if money >= 100:
    remain = money // 100
    print("There are" +str (remain)  + "100 dollar bills")
    money = money % 100

if money >= 50:
    remain = money // 50
    print("There are"  +str (remain)  + "50 dollar bills")
    money = money % 50
    
if money >= 20:
    remain = money // 20
    print("There are" +str (remain) + "20 dollar bills")
    money = money % 20
    
if money >= 10:
    remain = money // 10
    print("There are" +str (remain) + "10 dollar bills")
    money = money % 10
    
if money >= 5:
    remain = money // 5
    print("There are" +str (remain) + "5 dollar bills")
    money = money % 5
    

