import csv
file_to_load = "./budget_data.csv"
file_to_output_="analysis/budget_analysis_1.txt"

total_months = 0
previous_revenue = 0
month_of_change_list = []
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",999999999999999]
total_revenue = 0

with open(file_to_load) as revenue_data:
    reader =csv.DictReader(revenue_data)

    for row in reader:

        total_months = total_months + 1
        #total_revenue = total_revenue + int(row["Revenue"])
        

        revenue_change = int(row["Revenue"]) - previous_revenue
        previous_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change = [row["Date"]]

        if (revenue_change_list > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change 

        if (revenue_change_list < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
revenue_ave = sum(revenue_change_list) / len(revenue_change_list)
output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Greatest Increase in Revenue:{greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue:{greatest_decrease[0]} (${greatest_decrease[1]})\n" 

)

print(output)
with open(file_to_output,"w") as txt_file:
    txt_file.write(output)


