settlement_amount = float(input("What is the gross settlement amount? "))
disbursements = float(input("What are the net disbursements on the case? "))

def balance(settlement_amount, disbursements):
        return(settlement_amount - disbursements)

settlement_less_disbursements = balance(settlement_amount, disbursements)

print(f"After deuducting disbursements, the balance is ${settlement_less_disbursements}")

def attys_fee(settlement_less_disbursements):
    if 0 < settlement_less_disbursements <= 250000:
        return round((settlement_less_disbursements * 0.3), 2)
    
    elif 250000 < settlement_less_disbursements <= 500000:
        return round((((settlement_less_disbursements - 250000) * 0.25) + 75000), 2)
        
    elif 500000 < settlement_less_disbursements <= 1000000:
        return round((((settlement_less_disbursements - 500000) * 0.2) + 137500), 2)          
           
    elif 1000000 < settlement_less_disbursements <= 1250000:
        return round((((settlement_less_disbursements - 500000) * 0.15) + 237500), 2)   
    
    elif settlement_less_disbursements > 1250000:
        return round((((settlement_less_disbursements - 1250000) * 0.1) + 275000), 2)   
    
    else:
        print("Negative value found. Are you sure you entered your data correctly?")
            
attys_fee = attys_fee(settlement_less_disbursements)

print(f"The attorneys' fee for this settlement is ${attys_fee}")
