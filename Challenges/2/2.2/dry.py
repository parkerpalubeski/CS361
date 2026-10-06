#CS 361
#Parker Palubeski
#In-class Challenge 2.2: DRY This Code

#Processes the data and assigns highest, lowest, total and average
def process_data(records, key): #not very happy with passing the key in
    total = 0
    count = 0
    highest = float('-inf')
    lowest = float('inf')
    for record in records:
        amount = record[key]
        total += amount
        count += 1
        if amount > highest:
            highest = amount
        if amount < lowest:
            lowest = amount
    average = total / count if count > 0 else 0
    return {"total": total, "average": average, "highest": highest, "lowest": lowest}

#Prints the data to the command line
def print_info(stats):
    print(f"  Total:   ${stats["total"]:.2f}")
    print(f"  Average: ${stats["average"]:.2f}")
    print(f"  Highest: ${stats["highest"]:.2f}")
    print(f"  Lowest:  ${stats["lowest"]:.2f}")


# For this challenge, do not change the following 3 lines:
sales = [{"amount": 100}, {"amount": 250}, {"amount": 75}]
marketing = [{"budget": 500}, {"budget": 300}, {"budget": 800}]
engineering = [{"hours": 40}, {"hours": 35}, {"hours": 45}]

sales_stats = process_data(sales, "amount")
print("Sales Report")
print_info(sales_stats)

marketing_stats = process_data(marketing, "budget")
print("Marketing Report")
print_info(marketing_stats)

engineering_stats = process_data(engineering, "hours")
print("Engineering Report")
print_info(engineering_stats)