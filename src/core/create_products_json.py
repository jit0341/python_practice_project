# create_products_json.py

# 1. Define your JSON content as a multi-line string variable
#    Use triple quotes ("""...""") for multi-line strings.
json_content = """
[
  {
    "id": "P001",
    "name": "Laptop Pro",
    "category": "Electronics",
    "price": 1200.00,
    "in_stock": true
  },
  {
    "id": "P002",
    "name": "Mechanical Keyboard",
    "category": "Electronics",
    "price": 95.50,
    "in_stock": true
  },
  {
    "id": "P003",
    "name": "Wireless Mouse",
    "category": "Electronics",
    "price": 25.00,
    "in_stock": false
  },
  {
    "id": "P004",
    "name": "Desk Chair Ergonomic",
    "category": "Furniture",
    "price": 350.00,
    "in_stock": true
  },
  {
    "id": "P005",
    "name": "USB-C Hub",
    "category": "Accessories",
    "price": 40.00,
    "in_stock": true
  }
]
"""

# 2. Open the file in write mode ('w')
try:
    with open("products.json", "w") as f:
        # 3. Pass the string variable to f.write()
        f.write(json_content)
    print("products.json created successfully!")
except IOError as e:
    print(f"Error creating products.json: {e}")





