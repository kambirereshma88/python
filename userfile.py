
filename=input("Create file with your Name:- ")
f=open (f"{filename}.txt",'x')


name=input("Enter your Name :- ")
age=input("Enter your Age:-")
city=input("Enter your city:- ")

w=open(f'{filename}.txt','w')

w.write(f"\nName:{name}\nAge:{age}\ncity:{city}")




