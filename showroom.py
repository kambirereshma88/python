vehicle = input("what are you looking for bike/car:  ")
data = {"bike":['honda','hero','suzuki'],"car":['maruti-suzuki','tata','mahindra','toyota'],
         "company":{'honda':['shine','unicorn','yuva'],'hero':['splender','delux','extreme'],
          'suzuki':['access','burgman','gixxer']}}

cb ={"shine":{"price":120000,'d-date':"16/5/2024","loan":"yes,you do"},
    "unicorn":{"price":150000,'d-date':"20/5/2024","loan":"yes,you do"}}


print(data[vehicle])
select_veh = input(f"which company{vehicle} are you looking for:  ")
print(data["company"][select_veh])
model=input(f"which model do you like of {select_veh}: ")
print(cb[model])
