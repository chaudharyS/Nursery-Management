'''
module name: purchase
function name: purchase
overview of this function:
1) Customer interaction for what and how many plants the want buy.
2) check the user interaction valid or not with exception handelling.
3) calculating the customer purchase product with discount(if discountable)
4) show the last update of the product
5) write the invoice for customer with unique naming
'''
def purchase(List):
    L=List #assign list with variable name 'L'.
    a_name=input("Please enter your name: ")
    print("\nHello "+a_name+"!\nWelcome to Green Zone Nursery.\nPlease have a look at the plants above and pick the plants of your choice.")
    q={}  #assign empty dictionary with variable name 'q'.
    flag="Y"
    plant_to_price_dict = {}
    plant_to_quantity_dict = {}
    for i in range(len(L)):
        plant_name = L[i][0].upper()
        plant_to_price_dict[plant_name] = int(L[i][2])
    for i in range(len(L)):
        plant_name = L[i][0].upper()
        plant_to_quantity_dict[plant_name] = int(L[i][3])
    while flag.upper()=="Y":  #check and go if flag is 'Y' or 'y'.
        product=input("\nWhich plant do you want to buy? ")  
        product_name=product.upper()    #change the string value in the upper case.
        
        if plant_to_price_dict.get(product_name) != None: #check the user entered plant name within stock of nursery 
            p=True
            while p==True:
                try:
                    p_quantity=int(input("How many "+product+" plants do you want to buy? "))
                    p=False
                except:                             #executes, if customer entered unexpected value.
                    print("\t\tError!!!\nPlease enter integer value!! ") 
            if plant_to_quantity_dict.get(product_name) != None and p_quantity<=(plant_to_quantity_dict[product_name]):       
                q[product_name]=p_quantity
            else:
                print("\nSorry "+a_name+"!,\nWe don't have enough "+product+" plants in our stock to fulfil your requirement.\nWe will add stock of "+product+" plant soon.\n")
                
            flag=(input(a_name+" do you want buy more plants?(Y/N)"))
        else:
            print("Sorry "+a_name+"! "+product+" plant is not available in our store.")
            print("\nChoose from following plants please!")
            print("--------------------------------------------")
            print("%20s"%"PLANT NAME","%15s"%"PLANT TYPE","%10s"%"PRICE","%10s"%"QUANTITY")
            print("---------------------------------------------------------------------")
            for i in range(len(L)):
                print("%20s"%L[i][0],"%15s"%L[i][1],"%10s"%L[i][2],"%10s"%L[i][3]) # prints the availabile plants, type, price and quantity
            print("---------------------------------------------------------------------")
                
    #print ("\nThe plants that you picked and their respective quantities are as follows:\n",q,"\n")
    '''
        In the following operation:
        1) change every string value in the upper case latter.
        2) check what is the product entered by customer.
        3) executes respective condition if product is phone or laptop or hdd entered by customer.
    '''
    f_amount=0  #final amount
    plant_to_amount = {}
    print("%20s"%"PLANT NAME","%15s"%"UNIT PRICE","%10s"%"QUANTITY","%10s"%"AMOUNT")
    print("----------------------------------------------------------------------------------------")
    for selected_plant in q.keys():
        p_price=int(plant_to_price_dict[selected_plant])
        p_num=int(q[selected_plant])
        p_amount=(p_price*p_num)
        f_amount+=(p_price*p_num)
        plant_to_amount[selected_plant] = p_amount
        print("%20s"%selected_plant,"%15s"%p_price,"%10s"%p_num,"%10s"%plant_to_amount[selected_plant])
    print("\nYour total bill amount is: ", f_amount)

    '''
        In the following operation:
        1) ask to customer if they want to make a donation.
        2) add the amount of donation to the total bill amount.
    '''
    print("\nGreen Zone Nursery is committed to plant trees across the state of Jharkhand.\nYou can be a part of this initiative by making a donation.\n")
    print("All the amount received through donation is used to make Jharkhand a greener state.")
    donate = input("\nDo you want to contribute? (Y/N)")
    if donate.upper() == "Y":
        donation_amount = float(input("\nPlease enter the amount you would like to donate."))
        total = float(f_amount + donation_amount)
        print("Thank you "+a_name+" for extending your help in achieveing our mission.\n")
    else:
        donation_amount = 0.0
        total = float(f_amount + donation_amount)
    print("Your payable amount is: ", total)

    '''
        In the following operation:
        1) write a each unique invoive name which includes current date and time with customer name as well.
        2) write a purchase product name and details in file (invoice).
        3) write a discounted amount and final payable amount in file (invoice).
    '''
    
    import datetime  #import system date and time for create a unique invoive name.
    dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    invoice=str(dt)    #unique invoice
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
    d=str(t)    #date
    u=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
    e=str(u)    #time
    
    file=open(invoice+" ("+a_name+").txt","w")      #generate a unique invoive name and open it in write mode.
    file.write("=============================================================")
    file.write("\n\t\t\t\t\tGREEN ZONE NURSERY\n\t\t\t\t\t\tINVOICE")
    file.write("\n\nInvoice: "+invoice+"\t\tDate: "+d+"\n\t\t\t\t\t\t\t\tTime: "+e+"")
    file.write("\n\nName of Customer: "+str(a_name)+"")
    file.write("\n=============================================================")
    file.write("\nPLANT NAME\t\tUNIT PRICE\t\tQUANTITY\t\tTOTAL")  
    file.write("\n-------------------------------------------------------------")
          
    for keys in q.keys():           #In this loop, write in a file only those plants which are bought by the user.
        file.write(str("\n"+str(keys)+" \t\t\t "+str(plant_to_price_dict[keys])+" \t\t\t "+str(q[keys])+" \t\t\t "+str(plant_to_amount[keys])))
       
    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\tYour total bill amount: "+str(f_amount))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t   Your donation amount:  "+str(donation_amount))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Your payable amount: "+str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You "+a_name+" for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q
    
