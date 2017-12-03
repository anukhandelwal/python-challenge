
# Dependencies
import os
import csv

# create path for file budget_data_2.csv
csvpath = os.path.join('budget_data_2.csv')

# open and read file
with open(csvpath, newline="") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")
       
    # Skip the first row of the csv
	next(csv_reader)
    
    # create empty list for months and revenue
	months =[]
	revenue = []
	
    # Iterate throught each row
	for row in csv_reader:
		months.append(row[0])
		revenue.append(int(row[1]))
	   
	#print(csv_reader)

#The total number of months included in the dataset
total_months = len(months)

#The total amount of revenue gained over the entire period
total_revenue = sum(revenue)

print("Financial Analysis")
print("----------------------------")

#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)
print("Total Months : "+ str(total_months))
print("Total Revenue : $ "+ str(total_revenue))

#Get the difference between two consecutive revenues in the list 
total_diff_list = [j-i for i,j in zip(revenue[:-1], revenue[1:])]  

#Calculate Average Revenue Change
average = sum(total_diff_list) / float(len(total_diff_list))

print(average_diff)
average = round(average, 2)
print("Average Revenue Change : $ " + str(average))

#find maximum in the list
greatest_revenue = max(total_diff_list)
max_month_index = total_diff_list.index(max(total_diff_list))

# if list is 1, 2, 3, 4, 5
# Then the list of differences is 2-1, 3-2, 4-3, 5-4
# Index for the list of differences are one shorter than the index of the resutant, 
# so we would add 1 to the index ofthe corresponding month 
#
max_month = months[max_month_index+1]
print("Greatest Increase in Revenue :  " + str(max_month) + "  ($ " + str(greatest_revenue) + " )")


#find miminum in the list
lowest_revenue = min(total_diff_list)
min_month_index = total_diff_list.index(min(total_diff_list))

# if list is 1, 2, 3, 4, 5
# Then the list of differences is 2-1, 3-2, 4-3, 5-4
# Index for the list of differences are one shorter than the index of the resutant, 
# so we would add 1 to the index ofthe corresponding month 
#
min_month = months[min_month_index+1]
print("Greatest Decrease in Revenue :  " + str(min_month) + "  ($ " + str(lowest_revenue) + " )")
