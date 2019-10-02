# Code for Python Homework - PyBank data
# Read the csv
#Import modules
import os
import csv

#Define the path of the csv file
csvpath =os.path.join("..","/Users/lolitadias/desktop/PyBank","PyBank_Resources_budget_data.csv")
#Open csv file
with open(csvpath, newline="",errors='ignore') as csvfile:
    #CSV file specifies the delimeter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    #Define variables/lists; Initialize variables
    lmonths =[] # list to store data from column1 of csv file
    average_change=[] 
    month_count=[]
    var1=next(csvreader)
    tamount=int(var1[1]) #variable to count total amount of "Profit/Losses"(set the initital value to the value in Row1)
    var2 = int(var1[1]) #variable to store the value at row 1 to calculate revenue change -for the first iteration
    temp_increase=0 #temporary variable to store greatest increase in between iterations
    temp_decrease=0 #temporary variable to store greatest decrease in between iterations
    for row in csvreader:
        #The total number of months included in the dataset
        lmonths.append(row[0])
        tmonths=len(lmonths) +1

        #The net total amount of "Profit/Losses" over the entire period
        tamount=tamount+int(row[1])

        #The average of the changes in "Profit/Losses" over the entire period 
        revenue_change = int(row[1]) - var2
        average_change.append(revenue_change)
        var2 = int(row[1])
        month_count.append(row[0]) 
        avg_change = sum(average_change)/ len(average_change)
        
        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > temp_increase:
            temp_increase=int(row[1])
            temp_imonth=row[0]

        if int(row[1]) < temp_decrease:
            temp_decrease=int(row[1])
            temp_dmonth=row[0]

        high=max(average_change)
        low=min(average_change)

    #Print the result
    print('Financial Analysis')
    print('------------------------------------------------------')
    print(f'Total Months : {tmonths}')
    print(f'Total : ${tamount}')
    print(f'Average  Change:  ${avg_change:.2f}')
    print(f'Greatest Increase in Profits: {temp_imonth} (${high})')
    print(f'Greatest Decrease in Profits: {temp_dmonth} (${low})')

  
# Open the file using "write" mode. Specify the variable to hold the contents
file_path=open("Resources_Budget_Output.text","w")

# Write New Data
file_path.write(f'Financial Analysis\n')
file_path.write(f'-----------------------------------------------------\n')
file_path.write(f'Total Months: {tmonths}\n')
file_path.write(f'Total: ${tamount}\n')
file_path.write(f'Average Change: ${avg_change}\n')
file_path.write(f'Greatest Increase in Profits: {temp_imonth} (${high})\n')
file_path.write(f'Greatest Decrease in Profits: {temp_dmonth} (${low})')
    
    
    

