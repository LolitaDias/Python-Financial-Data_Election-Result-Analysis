# Code for Python Homework - PyBank data
# Read the csv
#Import modules
import os
import csv

#Define the path of the csv file
csvpath =os.path.join("..","/Users/lolitadias/desktop/Python-challenge/PyBank","PyBank_Resources_budget_data.csv")
#Open csv file
with open(csvpath, newline="",errors='ignore') as csvfile:

    #CSV file specifies the delimeter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)

    #Define variables/lists; Initialize variables
    lmonths =[] # list to store data from column1 of csv file
    lamount=[] # list to store data from column1 of csv file
    vamount=0 #variable to count total amount of "Profit/Losses"(set the initital value to zero)
    lavg_change=[] # list to store average change (the result of subtractions)
    temp_increase=0 #temporary variable to store greatest increase in between iterations
    temp_decrease=0 #temporary variable to store greatest decrease in between iterations
    vrow=next(csvreader) # Read the line 2 of csv file, The next() function returns the next item in an iterator
    vtemp = int(vrow[1]) 
    vamount=int(vrow[1])
  
    for row in csvreader:

            #create lists using data from the csv file
            lmonths.append(row[0])
            lamount.append(row[1])
     
            #The net total amount of "Profit/Losses" over the entire period --Correct code
            vamount= vamount + int(row[1]) 
            
            #The total number of months included in the dataset -Correct code
            vmonths=len(lmonths) +1

            #The average of the changes in "Profit/Losses" over the entire period  --correct code
            #First find the changes in consecutive rows ( subtract next value from previous values and store the result in a new list(lavg_change))
            tavg_change = int(row[1]) - vtemp
            lavg_change.append(tavg_change) # Storing the result in the list --correct code
            vtemp= int(row[1])
            avg_change = sum(lavg_change)/ len(lavg_change)

            #The greatest increase in profits (date and amount) over the entire period --correct code
            if int(row[1]) > temp_increase:
                    temp_increase=int(row[1])
                    temp_imonth=row[0]

            if int(row[1]) < temp_decrease:
                    temp_decrease=int(row[1])
                    temp_dmonth=row[0]

            high=max(lavg_change)
            low=min(lavg_change)

    #Checking the output of lavg_change list     
    #for x in lavg_change:
        #print (x)
    #print(len(lavg_change))


    
    #Print the result
    print('Financial Analysis')
    print('------------------------------------------------------')
    print(f'Total Months : {vmonths}')
    print(f'Total : ${vamount}')
    print(f'Average  Change:  ${avg_change:.2f}')
    print(f'Greatest Increase in Profits: {temp_imonth} (${high})')
    print(f'Greatest Decrease in Profits: {temp_dmonth} (${low})')

# Open the file using "write" mode. Specify the variable to hold the contents
file_path=open("Resources_Budget_Output.text","w")

# Write New Data to a text file
file_path.write(f'Financial Analysis\n')
file_path.write(f'-----------------------------------------------------\n')
file_path.write(f'Total Months: {vmonths}\n')
file_path.write(f'Total: ${vamount}\n')
file_path.write(f'Average Change: ${avg_change:.2f}\n')
file_path.write(f'Greatest Increase in Profits: {temp_imonth} (${high})\n')
file_path.write(f'Greatest Decrease in Profits: {temp_dmonth} (${low})')
    
    
    

