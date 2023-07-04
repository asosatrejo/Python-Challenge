#PyBank Challenge
import os
import csv
import pandas

budget_csv = '../Resources/budget_data.csv'

#Create lists to use
dateList = []
proLossList = []
changesList = []

#Create variables
monthCounter = 0
prevProLoss = 0
currProLoss = 0
change = 0

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        monthCounter += 1

        dateList.append(row[0])
        proLossList.append(int(row[1]))
        
        currProLoss = int(row[1])

        if monthCounter == 1: 
            prevProLoss = currProLoss
        else:
            change = currProLoss - prevProLoss
            changesList.append(change)
            prevProLoss = currProLoss
    
    #Store Values
    totalMonths = len(dateList)
    netTotal = sum(proLossList)
    avgChange = round(sum(changesList)/len(changesList),2)
    greatInc = max(changesList)
    greatIncMonth = dateList[changesList.index(greatInc)+1]
    greatDec = min(changesList)
    greatDecMonth = dateList[changesList.index(greatDec)+1]

#Print values
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${netTotal}')
print(f'Average Change: ${avgChange}')
print(f'Greatest Increase in Profits: {greatIncMonth} (${greatInc})')
print(f'Greatest Decrease in Profits: {greatDecMonth} (${greatDec})')

#Export to existing txt file 
#switch 'w' to 'x' to create new txt file
budget_txt = open('budget_data.txt','w')

#Overwite to print following text
budget_txt.write('Financial Analysis\n')
budget_txt.write('----------------------------\n')
budget_txt.write(f'Total Months: {totalMonths}\n')
budget_txt.write(f'Total: ${netTotal}\n')
budget_txt.write(f'Average Change: ${avgChange}\n')
budget_txt.write(f'Greatest Increase in Profits: {greatIncMonth} (${greatInc})\n')
budget_txt.write(f'Greatest Decrease in Profits: {greatDecMonth} (${greatDec})\n')

budget_txt.close()