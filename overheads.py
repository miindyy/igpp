import csv
from pathlib import Path

fp = Path.cwd() / "OVERHEADS.csv"

# read data from the csv file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

    def overheads(reader):
        """
        - find the highest overhead category with percentage
        """
        # create an empty list to store the expenses
        overheads=[] 

        # append expenses and their respective percentage into the Overheads list
        for row in reader:
            #get the percentage for each expenses
            #and append the Overheads list
            overheads.append([row[0], row[1]])  

        highest_overhead = None 
        highest_overhead_amount = 0
        
        # Loop through the data to find the highest overhead expense 
        for item in overheads: 
            expense_name = item[0] 
            expense_amount = float(item[1]) 
            
            if expense_amount > highest_overhead_amount: 
                highest_overhead_amount = expense_amount 
                highest_overhead = expense_name 
        

        return highest_overhead, highest_overhead_amount

    expense, percentage = overheads(reader)
    print(f"[HIGHEST OVERHEAD]: {expense.upper()}: {percentage}%")
