import overheads 
import cashonhand 
import csv 
from pathlib import Path 
 
csv_file_path = "overheadt.csv" 
coh_csv_file_path = "coh day 0-90.csv" 
 
# Read data from "coh day 0-90.csv" using the cashonhand module 
with open(coh_csv_file_path, newline="", encoding="UTF-8") as csvfile: 
    # Create a csv reader object 
    reader = csv.reader(csvfile) 
    # Skip header 
    next(reader) 
     
    # Call the cashonhand.coh() function with the reader object 
    cashonhand.coh(reader) 
 
# Read data from "overheadt.csv" using the overheads module 
with open(csv_file_path, newline="") as csvfile: 
    # Create a csv reader object 
    reader = csv.reader(csvfile) 
    # Skip header 
    next(reader) 
     
    # Call the overheads.overheads() function with the reader object and unpack the result 
    HAHA, LOL = overheads.overheads(reader)

