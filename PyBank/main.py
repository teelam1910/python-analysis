import csv
data = csv.DictReader(open('Resources/budget_data.csv'))
my_report = open('analysis/Budget_Report.txt','w')

total = 0
total_months = 0
pre_revenue = 0
total_change = 0
increase = ['',0]
decrease = ['',0]

for row in data:
    total_months += 1 # months = months + 1
    
    # total 
    revenue = int(row['Profit/Losses'])
    total += revenue
    
    # Average Chage
    change = revenue - pre_revenue
    if pre_revenue == 0:
        change= 0
    
    total_change += change
    
    # reset area
    pre_revenue = revenue
    
    # Greatest Increase 
    if change > increase[1]:
        increase[0] = row['Date']
        increase[1] = change
    
    # Greatest Increase 
    if change < decrease[1]:
        decrease[0] = row['Date']
        decrease[1] = change
    
output = f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total:,}
Average Change: ${total_change/(total_months-1):,.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,})
'''

print(output)
my_report.write(output)