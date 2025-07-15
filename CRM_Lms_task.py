print("=======customer discount calculation========")

#get customer input 

customer_id=input("enter customer_id")
customer_name=input("enter name")
is_premium_customer_input=input("are you premium customer? (yes/no)")
is_premium_customer=is_premium_customer_input=="yes"
years_partnership=int(input("enter partnership years") )
deal_stage=input("enter deal stage?(proposal/negotiation/closed)")
deal_value=int(input("enter deal value"))

# applying discount and conditional statements:
discount=0.00
print(f"Processing discount for {customer_name}")

if is_premium_customer:
    discount=0.10
    print("premium customer discount applied")
elif years_partnership>=3:
    discount=0.05
    print("non permium customer discount applied")
else:
    discount=0.00
    
   


  #match statements 
extradiscount=0.0
match deal_stage:
   
     case "proposal":
         extradiscount +=0.10  
     case "negotiation":
        extradiscount +=0.03
     case "closed":
          extradiscount +=0.05


#calculation of final discount and deal value

total_discount= discount + extradiscount         
final_discount_amount= deal_value*total_discount 
final_value=deal_value - final_discount_amount

#display the details
print(f"customer id {customer_id}")
print(f"customer name {customer_name}")
print(f"customer id {customer_id}")
print(f"premium customer status {is_premium_customer}")
print(f"deal value {deal_value}")
print(f"no of years in partnership {years_partnership}")
print(f"deal stage {deal_stage}")
print(f"customer id {discount}")
print(f"customer id {extradiscount}")
print(f"customer id {total_discount}")
print(f"customer id {final_value}")
