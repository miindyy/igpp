from pathlib import Path 
import csv 
 
fp = Path.cwd() / "cash-on-hand-usd.csv" 
 
with fp.open(mode="r", encoding="UTF-8", newline="") as file: 
    reader = csv.reader(file) 
    next(reader)  # skip header 
 
    def coh(reader): 
        # create an empty lists to store cash on hand difference 
        cashonhand = [] 
        cashonhand2 = [] 
 
        # append day and cash on hand into the cash on hand difference list 
        for row in reader: 
            cashonhand.append(row) 
 
        deficit_encountered = False  # Boolean flag to track if a deficit is encountered 
        prev_cash = int(cashonhand[0][1]) 
 
        for x in cashonhand[1:]: 
            cash = int(x[1]) 
 
            difference = cash - prev_cash 
 
            if difference < 0: 
                # Print the cash deficit day and amount 
                print(f"[CASH DEFICIT] DAY: {x[0]}, AMOUNT: USD{abs(difference)}") 
                deficit_encountered = True  # Set the flag to True if a deficit is encountered 
 
            cashonhand2.append(abs(difference)) 
            prev_cash = cash 
 
        # Check if there is any cash deficit 
        if not deficit_encountered: 
            # If there is no cash deficit, print the highest cash surplus and find the corresponding day 
            highest_surplus = max(cashonhand2) 
            highest_surplus_day = cashonhand[cashonhand2.index(highest_surplus)][0] 
            print("[HIGHEST CASH SURPLUS] DAY:", highest_surplus_day, "AMOUNT:", "USD", highest_surplus) 
        return  
    coh(reader)

