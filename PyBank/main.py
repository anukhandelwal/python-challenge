
import os
import csv
csvpath = os.path.join('budget_data_2.csv')



with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    count = 0
    # Skip the first row of the csv
    next(csv_reader, None)
    
    months =[]
    revenue = []

    for row in csv_reader:
    	months.append(row[0])
    	revenue.append(int(row[1]))
   
    print(csv_reader)
    total_months = len(months)
    total_revenue = sum(revenue)
    print(total_months)
    print(total_revenue)

    total_diff_list = [j-i for i,j in zip(revenue[:-1], revenue[1:])]  
    print(total_diff_list)
