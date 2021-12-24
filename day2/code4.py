#FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

#A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    i=0
    
    if(distance_in_kms>0 and quantity_ordered>=1):
        if(distance_in_kms>3):
            distance_in_kms=distance_in_kms-3
            
            while(distance_in_kms>0 and i<3):
                bill_amount=bill_amount+3
                distance_in_kms=distance_in_kms-1
                i=i+1
            
            while(distance_in_kms>0):
                bill_amount=bill_amount+6
                distance_in_kms=distance_in_kms-1
            
        if(food_type=="N"):
            bill_amount=bill_amount+(150*quantity_ordered)
        elif(food_type=="V"):
            bill_amount=bill_amount+(120*quantity_ordered)
        elif(food_type=="n" or food_type=="v" ):
             bill_amount=-1
    
    else:
        bill_amount=-1
        
                
    return bill_amount

bill_amount=calculate_bill_amount("N",3,7)
print(bill_amount)