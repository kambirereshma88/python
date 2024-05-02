food = input("What are you looking for veg/nonveg:  ")

if food == 'veg':
    veg = input("what are you looking for breakfast/dinner: ")
    if veg == "breakfast":
         print("idli,dosa,meduvada,uttapa,masaladosa,poha,upma,paratha")
         breakfast = input("select aas per your choice :")
    elif veg == 'dinner':
        print('mutterpaneer \n vegkolhapuri \n rajmamasla \n pannertikka \n dalmakhani \n palakpaneer')
        vegcurry = input("select as per your choice:")
        if vegcurry == "vegkolhapuri":
           print('with double roti,jeerarice,masaalapapaad,salad')
        elif vegcurry == "mutterpaneer":
            print('with double roti,rice,papad,salad')

elif food == 'nonveg':
    nonvegfood = input("Are you looking for chinese or indian food:")
    if nonvegfood == 'indian':
        print('chicken tikka,chicken curry,butterchicken,chickenkadai,chickenmoglai')
        indianfood = input("select as per your choice:")
        if indianfood == "butterchicken":
            print('with double roti,jeera rice,salad')
    elif nonvegfood == "chinese":
                print('friedrice,chillchicken,schezwan_noddles,manchurian,chicken_soup')
                chinesefood = input("select as per your choice:")
                print("with chicken soup and gravy")
        
            
