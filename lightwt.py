data = input(" what are you looking for light weight car/bike: ")

if data == 'bike':
    bike = input ("which company bike you are looking for: ")
    if bike == 'honda':
      print('splender \n activa \n shine \n unicorn \n navi ')
      model = input("select any one light weight bike to see detail : ")
      if model == "splender" :
          print(""" weight:99kg \n actual-price:120000\n discount-price:100000
                 \n cc: 110 \n manufacturer:honda pune """)
      elif model == "activa":
              print('''weight:86kg \n actual-price:150000 \n dicsount-price:120000
                      \n cc:110 \n manufacturer: honda''')


elif data == 'car':
    car = input("which company car you are looking for : ")
    if car == 'tata':
        print("""indica \n nano \n safari \n harrier \n nexon""")
        model= input("select any one car to see details : ")
        if model == 'indica':
            print("""weight:825-860kg \n actual-price:150000\n discount-price:120000
                 \n cc: 110 \n manufacturer:honda pune """)
        if model == "nano":
            print("""weight:750-800kg \n actual-price:400000 \n discount-price:350000 \n cc:110 \n manufacturer:hundai""")
        elif model == "safari":
            print("""weight:750-850kg \n actual-price:400000 \n discount-price:550000 \n cc:110 \n manufacturer:mahendra""")
        
         
