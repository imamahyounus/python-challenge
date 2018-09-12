# Dependencies/file location/creating new variables
import os, csv
from pathlib import Path 
Using_path = Path("budget_data.csv")

total_months = []
total_profit = []
m_profit_change = []
 
# Open csv/Storing data/skipping the first line and repeating the steps 
with open(Using_path, newline="", encoding='utf-8') as budge:
    csvreader = csv.reader(budge,delimiter=",") 
    header = next(csvreader)  
    for row in csvreader: 

#Total months and Total profit to lists/ getting monthly profits/go through each to get monthly profits
        total_months.append(row[0])
        total_profit.append(int(row[1]))
for i in range(len(total_profit)-1):
        
# Difference btwn two months and getting monthly profit change/getting min and max monthly profit change/max min
    m_profit_change.append(total_profit[i+1]-total_profit[i])
    max_inc_value = max(m_profit_change)
    max_dec_value = min(m_profit_change)
    max_inc = m_profit_change.index(max(m_profit_change)) + 1
    max_dec = m_profit_change.index(min(m_profit_change)) + 1 

print("Financial Analysis")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(m_profit_change)/len(m_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_inc]} (${(str(max_inc_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_dec]} (${(str(max_dec_value))})")



