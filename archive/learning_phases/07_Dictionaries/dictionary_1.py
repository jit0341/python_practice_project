book = {
    "title": "Secret Advisory",
    "author": "Agatha Christae",
    "year": 1860
}

book["price"] = 10
book["year"] = 1870
del book["price"]

print(book.items())

if "author" in book:
    book["publisher"] = {
        "name": "Penguin",
        "location": "Mumbai"
    }
    print(book["publisher"]["location"])
    
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        check_even_odd(4)  # Output: Even
        check_even_odd(9)  # Output: Odd