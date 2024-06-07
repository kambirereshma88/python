try:
   a=[1,25,23,4,5,6,12,14]
   for i in range (len(a)):
        print(a[i])

    
except Exception as e:
    #print(f"Error :=> {e}")
    print("please check the code ..........line by line")


try:
    a='1'+1
    print(a)
except Exception as e:
    print(e)


def add(a,b):
    try:
        return a+b
    except:
        return f'please check the input'

