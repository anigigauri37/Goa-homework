#for loop-ის საშუალებით ტერმინალში გამოიტანეთ 30-ჯერ "GOA IS THE BEST"

for i in range(30):
    print("GOA IS THE BEST")

#for loop-ის საშუალებით ტერმინალში 5-დან 150-ის ჩათვლით ნომრები

for i in range(5,150):
    print(i)

#for loop-ის საშუალებით ტერმინალში გამოიტანეთ 2-დან 50-ის ჩათვლით ნომრები ოღონდ ნაბიჯი იყოს 4 ანუ ყოველ i-ს თითეულ ნაბიჯზე დაემატოს 4

for i in range(2,50):
    i += 4
    print(i)

# for loop-ის საშუალებით ტერმინალში გამოიტანეთ  10-ჯერ ყოველი ( i ელემენტი და გვერდით მიუწერეთ, "GOA")

for i in range(10):
    print('GOA')

#დაწერეთ პროგრამა for loop-ის გამოყენებით, რომელიც გამოგვიტანს ჯერ ლუწს და შემდეგ კენტს.

for i in range(10):
    if i % 2 == 0:
        print(i)

for i in range(10):
    if i % 2 != 0:
        print(i)

#შექმენით პროგრამა სადაც გამოიყენებთ While loop - ს. თქვენი დავალება იქნება ის, რომ მომხამრებელს შემოატანინოთ რიცხვი და თქვენ უნდა გამოიცნოთ ეს რიცხვი, ხოლო ყოველ არ გამოცნობილ რიცხვზე ისევ თავიდან უნდა შეგეკითხოთ და შეიყვანოთ რიცხვი.

num1 = int(input("shemoitanet ricxvi"))
num2 = 5

while num1 == num2:
    print("yochag shen moige")
    break
else:
    print("waage")

