from pathlib import Path
import csv

fp = Path.cwd() / "PNL.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)


def pnl(reader):
    """
    - computes the difference of net profit if the current day is lower than the previous day
    - finds day and amount of the highest increment if net profit always increases
    """
    profitandloss = []
    profitandloss2 = []

    for row in reader:
        profitandloss.append(row)

    deficit_encountered = False
    prev_profit = int(profitandloss[0][4])
    highest_surplus = 0
    highest_surplus_day = None
    # initialise profitdeficit as a list
    pdeficit_list = []

    for x in profitandloss[1:]:
        profit = int(x[4])
        difference = profit - prev_profit

        if difference < 0:
            # print profit deficit and append it to the list (pdeficit_list)
            print(f"[PROFIT DEFICIT] DAY: {x[0]}, AMOUNT: USD{abs(difference)}")
            pdeficit_list.append(f"[PROFIT DEFICIT] DAY: {x[0]}, AMOUNT: USD{abs(difference)}")
            deficit_encountered = True
        else:
            if difference > highest_surplus:
                highest_surplus = difference
                highest_surplus_day = x[0]

        profitandloss2.append(abs(difference))
        prev_profit = profit
    
    if not deficit_encountered:
        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS")
    return highest_surplus_day, highest_surplus, pdeficit_list

