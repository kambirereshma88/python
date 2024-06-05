
rfile=input("select file from you want to read data : ")


with open(f'IRA\\{rfile}.txt','r') as r:
    lines=r.readlines()

    c=0
    for i in lines:
        c=c+len(i.split())

    wfile=input("select file in which you want to write count from above file: ")


    with open(f'IRA\\newone.txt','w')as w:
        w.write(f"count of words from {rfile}.txt is {c}")