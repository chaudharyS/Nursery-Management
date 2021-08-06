#driver module
import read
import purchase
import write

again="Y"

while again.upper()=="Y":
    a=read.read_file()
    b=purchase.purchase(a)
    write.over_write(a,b)
    print("\nThank you for taking a step towards a greener planet. :)")
    print("Your invoice has been saved as a text file. \nPlease check your invoice for your order details.")
    again=input("\nDo we have another customer? (Y/N)")
