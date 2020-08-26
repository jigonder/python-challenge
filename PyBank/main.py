#import module
import os
import csv

#read/open csv file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',' )
    header = next(csvreader)

#define the variables/lists
    total_months = 0
    total_profit_loss = 0
    change_list = []
    firstRow = next(csvreader)
    previousRow = firstRow[1]

#create loop
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        change = int(row[1]) - int(previousRow)
        previousRow = row[1]
        change_list.append(change)

    avg_change = sum(change_list) / len(change_list)   
    total_months += 1 
    total_profit_loss += int(firstRow[1])
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)
    
#print text
    output_text = (f"Financial Analysis\n"
                 f"------------------------\n"
                 f"Total Months: {total_months}\n"
                 f"Total: ${total_profit_loss}\n"
                 f"Average Change: ${avg_change}\n"
                 f"Greatest Increase in Profits: (${greatest_increase})\n"
                 f"Greatest Decrease in Profits: (${greatest_decrease})\n"
                 f"--------------------------")
    print(output_text)

#output path to file
outputPath = os.path.join("PyBank", "Analysis", "PyBank-output.txt")
with open(outputPath, 'w') as writerfile: 
    
    textWriter = writerfile.write(output_text)
    
    
    