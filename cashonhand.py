from pathlib import Path
import csv

fp = Path.cwd() / "COH.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

def coh(reader):
    """
    - computes the difference of cash on hand if the current day is lower than the previous day
    - finds day and amount of the highest increment if cash on hand always increases
    """
    cashonhand = []
    cashonhand2 = []
    # initialise cashdeficit as a list
    cdeficit_list = []

    for row in reader:
        cashonhand.append(row)

    deficit_encountered = False
    prev_cash = int(cashonhand[0][1])
    highest_surplus = 0
    highest_surplus_day = None

    for x in cashonhand[1:]:
        cash = int(x[1])
        difference = cash - prev_cash

        if difference < 0:
            # print cash deficit and append it to the list (cdeficit_list)
            print(f"[CASH DEFICIT] DAY: {x[0]}, AMOUNT: USD{abs(difference)}")
            cdeficit_list.append(f"[CASH DEFICIT] DAY: {x[0]}, AMOUNT: USD{abs(difference)}")
            deficit_encountered = True
        else:
            if difference > highest_surplus:
                highest_surplus = difference
                highest_surplus_day = x[0]

        cashonhand2.append(abs(difference))
        prev_cash = cash

    if not deficit_encountered:
        print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    return highest_surplus, highest_surplus_day, cdeficit_list
         
