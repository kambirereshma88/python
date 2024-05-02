fashion=input("what are you looking for saree/dresses : ")
if fashion == "saree":
    brand = input('For which brand are you looking for divastri/janasya: ')
    if brand == 'divastri':
        print('banarsi-silk,kanjivaram,chiffon,bandhani,jacquard,cotton')
        pattern= input('select pattern as per your choice:  ')
        if pattern == "banarsi-silk":
            print("""colour-darkgreen \n actual-price:Rs3500 \n discount price:Rs699
                      \n fabric-silk blend \n blousepiece-unstitched \n sareestyle-regularsaree""")    
        elif pattern == 'chiffon':
                print("""colour-darkred \n actual-price:Rs3500 \n discount price:Rs699
                      \n fabric-silk blend \n blousepiece-unstitched \n sareestyle-regularsaree""")
        elif pattern == "kanjivaram":
                 print("""colour-bottlegreen \n actual-price:Rs3000 \n discount price:Rs599
                         \n fabric-silk blend \n blousepiece-unstitched \n sareestyle-regularsaree""")
    elif brand =='janasya':
        print('banarsi-silk,kanjivaram,chiffon,bandhani,jacquard,cotton')
        pattern = input('select pattern as per your choice:  ')
        if pattern == "banarsi-silk":
            print("""colour-yellow \n actual-price:Rs3900 \n discount price:Rs799
                  \n fabric-silk blend \n blousepiece-unstitched \n sareestyle-regularsaree""")

elif fashion == "dresses":
    brand = input('for which brand are you looking for libas/biba: ')
    if brand == 'libas':
        print('stripped \n geometric print \n selfdesign \n embroidery \n cotton-blend \n floralprinted')
        pattern = input('select pattern as per your choice:  ')
        if pattern == 'embroidery':
            print("""colour:blue \n kurta pant set \n actual-price:Rs1500 \n discount-price:799 \n all size available""")
        elif pattern == 'floralprinted':
            print("""color:yellow \n kurta pant dupatta set \n actual-price:Rs 2000
                      \n discount-price:Rs1399 \n all size available""")
        elif pattern == 'cotton-blend':
            print("""colour:red \n kurta plaazo set \n actual-price:Rs2500 \n discount-price:Rs1500 \n all size available""")


    elif brand == 'biba':
        print('stripped \n geometric print \n selfdesign \n embroidery \n cotton-blend \n floralprinted')
        pattern = input('select pattern as per your choice : ')
        if pattern == "selfdesign":
            print("""colour-orange \n kurta pant dupatta set \n actual-price:Rs3000 \n discount-price:Rs2000 \n all size available""")


    else:
        print("unknown brand")
            
                    
            
                  
                  


        
        
        
                 

                     
                 



