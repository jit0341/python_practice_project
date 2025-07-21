import json

products_data = [] # Initialize an empty list to hold your Python data

try:
    with open("products.json", "r") as json_file:
        products_data = json.load(json_file) # This is the magical part for reading JSON!
    print("Products data loaded successfully!")
    # print(products_data) # Uncomment this line temporarily to see the loaded data
except FileNotFoundError:
    print("Error: products.json not found. Please ensure it's in the same directory.")
    exit()
except json.JSONDecodeError:
    print("Error: Could not decode JSON from products.json. Check file format.")
    exit()
except IOError as e:
    print(f"An I/O error occurred: {e}")
    exit()

# --- Now, let's do the next steps: Average, Out of Stock, etc. ---

# 1. Calculate the total number of products
total_products = len(products_data)

# 2. Calculate the average price of all products
total_price = 0
for product in products_data:
    # Each 'product' here is a dictionary, e.g., {'id': 'P001', 'name': 'Laptop Pro', ...}
    total_price += product["price"] # Access the 'price' value from each product dictionary

average_price = 0
if total_products > 0: # Avoid division by zero if products_data is empty
    average_price = total_price / total_products

# 3. Identify all products that are currently out of stock
out_of_stock_list = []
for product in products_data:
    if product["in_stock"] is False: # Check if the 'in_stock' key's value is False
        out_of_stock_list.append(product) # Add the entire product dictionary to the list

# --- Generate a Summary and Out-of-Stock Report ---

# Print summary to console
print(f"Total products: {total_products}")
# Using :.2f for floating-point numbers formats to 2 decimal places
print(f"Average product price: ${average_price:.2f}")

# Create a new JSON file named out_of_stock_products.json
# Write only the details of the products that are out of stock into this new JSON file.
try:
    with open("out_of_stock_products.json", "w") as outfile:
        # json.dump() converts Python list/dict to JSON and writes it to the file
        # indent=4 makes the output JSON file nicely formatted and readable
        json.dump(out_of_stock_list, outfile, indent=4)
    print("Out-of-stock products report generated: out_of_stock_products.json")
except IOError as e:
    print(f"An I/O error occurred while writing out_of_stock_products.json: {e}")
except Exception as e: # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")







