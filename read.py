def read_file(): #Function is defined with name : 'read_file'
    file=open("products.txt","r") #open stock file (products.txt) in read mode. 
    lines=file.readlines() 
    L=[] # assign empty list with name 'L'
    for line in lines:
        L.append(line.replace("\n","").split(","))
    file.close()
    print("\n\n\t\t\t\t\t\t  GREEN ZONE NURSERY\n")
    print("\t\t\t\t\tTo plant a garden is to believe in tomorrow.\n")
    print("Following plants are avilable in our nursery\n")
    print("---------------------------------------------------------------------")
    print("%20s"%"PLANT NAME","%15s"%"PLANT TYPE","%10s"%"PRICE","%10s"%"QUANTITY")
    print("---------------------------------------------------------------------")
    for i in range(len(L)):
        print("%20s"%L[i][0],"%15s"%L[i][1],"%10s"%L[i][2],"%10s"%L[i][3]) # prints the availabile plants, type, price and quantity
    print("---------------------------------------------------------------------")
    return L
    
