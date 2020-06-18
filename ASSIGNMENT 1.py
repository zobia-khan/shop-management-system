#functions for object food
def showItems():
    '''displays no of items in stock'''
    print('samosas in stock:',samosas_in_stock,'rolls in stock:',rolls_in_stock)

def addItems():
    '''takes input of no. of items to be added in stock and returns stock'''
    global samosas_in_stock,rolls_in_stock
    
    add_samosas=int(input('Add samosas '))
    add_rolls=int(input('Add rolls   '))
    
    samosas_in_stock+=add_samosas
    rolls_in_stock+=add_rolls
    
    return samosas_in_stock,rolls_in_stock

def take_order():
    '''takes order,checks the stock for ordered items and returns ordered items'''
    
    samosas_in=int(input('How many samosas would you like? ')) 
    while samosas_in > samosas_in_stock:
        samosas_in=int(input('Out of stock enter within '+str(samosas_in_stock)+':'))#variable is type cast to string because it would result to error which is input takes 1 to 2 argumnets not 3
    rolls_in=int(input('How many rolls would you like?' ))
    while rolls_in > rolls_in_stock:
        rolls_in=int(input('Out of stock enter within '+str(rolls_in_stock)+':'))
    
    return samosas_in,rolls_in

def order_and_bill():
    '''takes order by calling function take_order() and calculates bill returns total_items and total_bill_food
    
       unit prices for samosa and roll are Rs.12 and Rs.20 respectively'''
    global samosas_in_stock ,rolls_in_stock,total_bill_food,total_items,total_sales
    samosas_unit_price,rolls_unit_price=12,20
    if samosas_in_stock != 0 or rolls_in_stock != 0:
        samosas_in,rolls_in=take_order()
        #bill calculations
        total_bill_food=samosas_in*samosas_unit_price + rolls_in*rolls_unit_price
        #adding items for an individual and total sales for a day
        total_items = samosas_in + rolls_in
        total_sales+=total_items#value of total_items added to global variable 'total_sales' each time the funtion is executed
        #stock adjustion
        samosas_in_stock-= samosas_in
        rolls_in_stock-= rolls_in
        print('\nYour total items are',total_items,',and total amount is Rs.', total_bill_food)
    else:
        print("\nSorry can't take any order , we are out of stock :(")
        
#functions for object employee
def set_wage_rates():
    '''function that takes wage rates from user and returns each employee wage rates'''
    global emp_A_wage_rates,emp_B_wage_rates
    emp_A_wage_rates=int(input("Enter wage rates for employee A per day"))
    emp_B_wage_rates=int(input("Enter wage rates for employee B per day"))
    return emp_A_wage_rates,emp_B_wage_rates

def add_hours_worked():
    '''function that adds and returns working hours of each employee'''
    global emp_A_hours,emp_B_hours
    #adding working hours
    emp_A_hours+=int(input("Add working hours of employee A per day"))
    emp_B_hours+=int(input("Add working hours of emmployee B per day"))
    return emp_A_hours,emp_B_hours

def payments():
    '''function that checks working hours of employee ,calculate and returns payments'''
    global emp_A_payment,emp_B_payment,emp_A_wage_rates,emp_B_wage_rates,emp_A_hours,emp_B_hours
    if emp_A_hours==0 or emp_B_hours==0:
        print('Add employees working hours first for the calculation of payments')
    else:
        #calculating payments
        emp_A_payment=(emp_A_wage_rates*emp_A_hours)
        emp_B_payment=(emp_B_wage_rates*emp_B_hours)
        print("Employee A has earned Rs.",emp_A_payment,"Employee B has earned Rs.",emp_B_payment)

def bonus():
    '''function that checks total sales of food items and returns added bonus to payments'''
    global total_sales,emp_A_payment,emp_B_payment
    if total_sales >= 200: 
        emp_A_payment+=5 #Rs.5 bonus per day
        emp_B_payment+=5
        print( "Employee A payments after bonus Rs.",emp_A_payment,"Employee B payments after bonus Rs.",emp_B_payment)
    else:
        print("no bonus added because sales do not exceed 150 items per day")


# boutique functions
def items_details():
    '''displays details of items available'''
    print('number of stiched dresses and unstiched dresses are',stiched_in_stock,unstiched_in_stock)

def boutique_operating_system():
    '''function that takes user input as order, deducts ordered items from stock,calculates amount and returns total bill'''
    global stiched_in_stock,unstiched_in_stock
    
    stiched_unit_price,unstiched_unit_price=4000,2600
    #taking order
    stiched_in=int(input("how many stiched dresses would you like?"))
    unstiched_in=int(input("how many unstiched dresses would you like?"))
    #adjusting stock
    stiched_in_stock-=stiched_in
    unstiched_in_stock-unstiched_in
    #calculating amount
    total_amount=stiched_in*stiched_unit_price+unstiched_in*unstiched_unit_price
    return total_amount

def costumer_gift():
    '''function that checks the total amount from food items for gift voucher of boutique items
    and returns total amount after deducting 300 from total amount of function boutique_operating_system  '''
    
    global total_bill_food,total_amount
    
    if total_bill_food>=1500:
        choice_purchase_dress=input('''CONGRATULATIONS!you have won Rs300 voucher for boutique items.
                 Would you like to purchase dress?(Press 'y' or 'Y')''')
        
        if choice_purchase_dress == 'Y' or choice_purchase_dress == 'y':
            total_amount=boutique_operating_system()-300
            print("Your total bill is Rs.",total_amount)
        else:
            print('voucher expires after 10 days')
    else:
        print('~Get discount voucher on purchasing of Rs.700 or above~')
    
    
def days_of_sale():
    '''function that checks the weekday for special offer of the day and
    returns half value of total amount or print staement'''
    
    global weekday,stiched_in_stock,unstiched_in_stock
    
    if weekday == 'Friday' or weekday=='Monday' or weekday=='Wednesday':
        print('''           Special Offer of the day
                  ~BUY ONE GET ONE FREE!~''' )
        total_amount=boutique_operating_system()/2
        print("Your total bill is Rs.",total_amount)
    else:
        print("         No Sale Offer Today      ")

          #main code
from datetime import datetime

samosas_in_stock = 250
rolls_in_stock = 250
total_items=0
total_bill_food=0
total_sales = 0

emp_A_wage_rates=50
emp_B_wage_rates=40
emp_A_hours=0
emp_B_hours=0
emp_A_payment=0
emp_B_payment=0

stiched_in_stock=15
unstiched_in_stock=15
weekday=datetime.today().strftime('%A')
total_amount=0

#main menu print statement
print('''           ******** MY BAKE SHOP MANAGEMENT SYSTEM ***********   
                     

      
                       ***FOOD OPERATIONS***
                  1.Show items in stock 
                  2.Add items in stock
                  3.Take order and calculate bill
                  
                       ***EMPLOYEE OPERATIONS***
                  4.Set wage rates for employee
                  5.Add working hours of employee
                  6.Calculate payments
                  7.Add bonus to payments
                  
                       ***BOUTIQUE OPERATIONS***
                  8.Show items in stock
                  9.Take order and calculate bill
                  10.Gift voucher
                  11.Sale weekdays
                  12.Exit''')

# an infinite loop that takes user input as integer and breaks when user enters integer '12'
while True:
    choice=input('\nChoose an operation_')
    if choice == '12':
        break
    elif choice=='1':
        print()
        showItems()
    elif choice=='2':
        print()
        addItems()
    elif choice=='3':
        print()
        order_and_bill()  
    elif choice=='4':
        print()
        set_wage_rates()
    elif choice=='5':
        print()
        add_hours_worked()
    elif choice=='6':
        print()
        payments()
    elif choice=='7':
        print()
        bonus()
    elif choice=='8':
        print()
        items_details()
    elif choice=='9':
        print("\nyour total bill is Rs.",boutique_operating_system())
    elif choice=='10':
        print()
        costumer_gift()   
    elif choice=='11':
        print()
        days_of_sale()
    else:
        print('Enter your choice in numbers only')

