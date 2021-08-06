def over_write(List,Dictionary): #an overwrite function 
    L=List #assign list with variable name 'L'
    d=Dictionary #assign Dictionary with variable name 'd'
    '''
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    '''
    for selected_plant in d.keys():
        for i in range(len(L)):
            if L[i][0] == selected_plant:
                L[i][3] = str(int(L[i][3]) - int(d[selected_plant])) 
    
    files=open("products.txt","w")  #opens stock file (products.txt) file in write mode.     
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    print("Remaining stock of plants in the nursery\n")
    print("---------------------------------------------------------------------")
    print("%20s"%"PLANT NAME","%15s"%"PLANT TYPE","%10s"%"PRICE","%10s"%"QUANTITY")
    print("---------------------------------------------------------------------")
    for i in range(len(L)):
        print("%20s"%L[i][0],"%15s"%L[i][1],"%10s"%L[i][2],"%10s"%L[i][3]) # prints the availabile plants, type, price and quantity
    print("---------------------------------------------------------------------")
    return
