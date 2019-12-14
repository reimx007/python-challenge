# import modules
import os, csv
from statistics import mean

# define function for average, just for the heckuvit
def Average(l):
    avg = mean(l)
    return avg


# set up lists to store column Data
months = []
netProfit =  []

# open the csv data file
budget_path = os.path.join("budget_data.csv")

with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # find header, skip header
    header = next(csvreader)
    #print(f"Header: {header}") <= used in testing

    # loop through each row in table. Append values to months and netProfits lists
    # Set netProfits values to floats since some are negative and we need to do math with them
    for row in csvreader:
        months.append(row[0])
        numbers = float(row[1])
        netProfit.append(numbers)


    #print(total)
    # call the average function
    average = Average(netProfit)
    # return the index of the max and min values in netProfit
    maxIndex = netProfit.index(max(netProfit))
    minIndex = netProfit.index(min(netProfit))
    # print stuff
    print("Financial Analysis")
    print("------------------------")
    print(f'Total months: {len(months)}')
    print(f'Total: ${round((sum(netProfit)),0)}')
    print(f'Average change: ${round(average,2)}')
    print(f'Greatest increase in profit: {months[maxIndex]} | {round(max(netProfit),2)} | {maxIndex}')
    print(f'Greatest Decrease in profit: {months[minIndex]} | {round(min(netProfit),2)} | {maxIndex}')

    # open new txt file and write to it
    f = open("budget_summary.txt", "w+")

    f.write("Financial Analysis for county X\n")
    f.write("------------------------\n")
    f.write(f'Total months: {len(months)}\n')
    f.write(f'Total: ${(sum(netProfit))}\n')
    f.write(f'Average change: ${average}\n')
    f.write(f'Greatest increase in profit: {months[maxIndex]} | {max(netProfit)} | {maxIndex}\n')
    f.write(f'Greatest Decrease in profit: {months[minIndex]} | {min(netProfit)} | {maxIndex}')
