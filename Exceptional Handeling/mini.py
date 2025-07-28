'''
You had saved the items and their price details in the text file which you purchased yesterday from a nearby supermarket.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount you paid after the discount?
Help yourself by writing a Python code to do this. Include necessary code to handle the possible exceptions.
Note: Data is stored in a text file named Purchase-1.txt.
Each line contains one item's details. Item name and price are separated by a space.
You have to enter the file name during runtime.
'''

try:
    filename = input("Enter the file name: ").strip() + ".txt"

    with open(filename, 'r') as file:
        lines = file.readlines()

    total_items = 0
    free_items = 0
    amount_to_pay = 0
    discount = 0

    for line in lines:
        line = line.strip()

        if not line:
            continue
        parts = line.split()

        if len(parts) != 2:
            continue
        item, price_str = parts[0], parts[1]

        if item.lower() == "discount":
            try:
                discount = int(price_str)
            except ValueError:
                print(f"Invalid discount value: {price_str}")
                discount = 0
        elif price_str.lower() == "free":
            free_items += 1
        else:
            try:
                price = int(price_str)
                amount_to_pay += price
                total_items += 1
            except ValueError:
                print(f"Invalid price for item '{item}': {price_str}")

    final_amount = amount_to_pay - discount

    print("Number of items purchased", total_items)
    print("Number of free items", free_items)
    print("Amount to pay", amount_to_pay)
    print("Discount given", discount)
    print("Final amount paid", final_amount)

except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
