# Code for Python Homework - PyPoll data
# Read the csv
#Import modules
import os
import csv

#Define the path of the csv file
csvpath=os.path.join('..','PyPoll','Resources','election_data.csv')
#csvpath =os.path.join("..","/Users/lolitadias/Desktop/PyPoll/election_data.csv")
#Open csv file
with open(csvpath, newline="",errors='ignore') as csvfile:
    #CSV file specifies the delimeter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    
    #Define variables/lists 
    #Initialize the variables
    tvotes=0
    vkhan=0
    vcorrey=0
    vli=0
    votooley=0
    kpercent=0
    cpercent=0
    lpercent=0
    opercent=0

    # Read rows from the csv file (excludes the Header)
    for row in csvreader:

        #The total number of votes cast
        tvotes=tvotes+1

        #A complete list of candidates who received votes
        if(row[2]=="Khan"):
            vkhan=vkhan+1
        elif(row[2]=="Correy"):
            vcorrey=vcorrey+1
        elif(row[2]=="Li"):
            vli=vli+1
        else:
            votooley=votooley+1
        
        #The percentage of votes each candidate won
        kpercent=(vkhan/tvotes)*100
        cpercent=(vcorrey/tvotes)*100
        lpercent=(vli/tvotes)*100
        opercent=(votooley/tvotes)*100

        #The winner of the election based on popular vote
        lwinner=[kpercent,cpercent,lpercent,opercent]
        if(kpercent>cpercent and kpercent>lpercent and kpercent>opercent):
            winner="Khan"
        elif(cpercent>kpercent and cpercent>lpercent and cpercent>opercent):
            winner="Correy"
        elif(lpercent>kpercent and lpercent>cpercent and lpercent >opercent):
            winner="Li"
        else:
            winner="O'Tooley"
        
#Print the result
print("Election Results")
print("----------------------------")
print(f"Total Votes : {tvotes}")
print("----------------------------")
print(f"Khan: {kpercent:.3f}% ({vkhan})")
print(f"Correy: {cpercent:.3f}% ({vcorrey})")
print(f"Li: {lpercent:.3f}% ({vli})")
print(f"O'Tooley: {opercent:.3f}% ({votooley})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Open the file using "write" mode. Specify the variable to hold the contents
file_path=open("Election_Data_Output.text","w")

# Write New Data
file_path.write("Election Results\n")
file_path.write("----------------------------\n")
file_path.write(f"Total Votes : {tvotes}\n")
file_path.write("----------------------------\n")
file_path.write(f"Khan: {kpercent:.3f}% ({vkhan})\n")
file_path.write(f"Correy: {cpercent:.3f}% ({vcorrey})\n")
file_path.write(f"Li: {lpercent:.3f}% ({vli})\n")
file_path.write(f"O'Tooley: {opercent:.3f}% ({votooley})\n")
file_path.write("----------------------------\n")
file_path.write(f"Winner: {winner}\n")
file_path.write("----------------------------\n")