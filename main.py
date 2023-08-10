import overheads
import cashonhand 
import pnl
import csv
from pathlib import Path

oh_csv_file_path = Path.cwd() / "OVERHEADS.csv"
coh_csv_file_path = Path.cwd() / "COH.csv"
pnl_csv_file_path = Path.cwd() / "PNL.csv"

# Read data from "OVERHEADS.csv" using the overheads module
with oh_csv_file_path.open(mode="r", encoding="UTF-8", newline="") as csvfile: 
    reader = csv.reader(csvfile) 
    a = overheads.overheads(reader)
        

# Read data from "COH.csv" using the cashonhand module 
with coh_csv_file_path.open(mode="r", encoding="UTF-8", newline="") as csvfile: 
    reader = csv.reader(csvfile) 
    b = cashonhand.coh(reader)  # Extract the desired value from the tuple

# Read data from "PNL.csv" using the pnl module 
with pnl_csv_file_path.open(mode="r", encoding="UTF-8", newline="") as csvfile: 
    reader = csv.reader(csvfile) 
    c = pnl.pnl(reader)  # Extract the desired value from the tuple

# Write data to a text file
with open("summary.txt", "w") as file:
# Write data to a text file
    file.write("Highest Overhead:\n")
    file.write(f"[HIGHEST OVERHEAD]: {a[0].upper()}: {a[1]}%\n")
    
    file.write("Cash Deficit:\n")
    for c_deficit in b[2]: # third item in b is list
        file.write(f"{c_deficit}\n")
    
    file.write("Profit Deficit:\n")
    for p_deficit in c[2]: # third item in c is list
        file.write(f"{p_deficit}\n")
    
