data = input(" what are you looking for car/bike: ")

if data == 'bike':
    bike = input ("which company bike you are looking for ")
    if bike == 'honda':
      print('splender \n activa \n shine \n unicorn \n navi ')
      model = input("select any one bike to see detail : ")
      if model == "splender" :
          print("""actual-price:120000\n discount-price:100000
                 \n cc: 110 \n manufacturer:honda pune """)
      elif model == "activa":
              print('''actual-price:150000 \n dicsount-price:120000
                      \n cc:110 \n manufacturer: honda''')


elif data == 'car':
    car = input("which company car you are looking for : ")
    if car == 'tata':
        print("""indica \n nano \n safari \n harrier \n nexon""")
        model= input("select any one car to see details : ")
        if model == 'indica':
            print("""actual-price:150000\n discount-price:120000
                 \n cc: 110 \n manufacturer:honda pune """)
         
