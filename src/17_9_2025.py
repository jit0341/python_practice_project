# --- Color Codes ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# --- Squares ---
def squares():
    print(f"{CYAN}----- 🔢 Squares 1 to 30 --------{RESET}")
    i = 1
    while i <= 30:
        print(f"Square of {i} is {i**2}")
        i += 1
    print("-" * 40)

# --- Table (user input) ---
def table():
    n = int(input(f"{YELLOW}Enter a number for its table: {RESET}"))
    print(f"{GREEN}------- 📊 Table of {n} -------{RESET}")
    for i in range(1, 11):
        print(f"{n} × {i} = {n * i}")
    print("-" * 40)

# --- Table of 25 ---
def table25():
    print(f"{BLUE}-------- 📘 Table of 25 --------{RESET}")
    i = 1
    while i <= 10:
        print(f"25 × {i} = {25 * i}")
        i += 1
    print("-" * 40)

# --- Fruits ---
def fruits():
    print(f"{GREEN}--- 🍎 Iterate Name of Fruits ---{RESET}")
    fruits = ["Apple 🍏", "Banana 🍌", "Orange 🍊", "Grapes 🍇", "Peach 🍑"]
    for fruit in fruits:
        print(f"I love {fruit}")
    print("-" * 40)

# --- Teachers ---
def teachers():
    print(f"{CYAN}---- 👨‍🏫 Teachers in RHS School ----{RESET}")
    teachers = [
        "Lakshman Sir", "Jitendra Bharti Sir", "Vinita Mam",
        "Nikki Soni Mam", "Jyoti Mam", "Pramila Mam",
        "Neeraj Sir", "Vikram Sir", "Pooja Mam"
    ]
    for t in teachers:
        print(f"{t} teaches in RHS Digital School Lanchi, Surajpur")
    print("-" * 40)


# ====== MENU ======
while True:
    print(f"""\n{YELLOW}📌 --- MENU ---{RESET}
1️⃣  Squares 1 to 30
2️⃣  Table (your choice)
3️⃣  Table of 25
4️⃣  Fruits
5️⃣  Teachers
6️⃣  Exit""")

    choice = input(f"{BLUE}👉 Enter your choice (1-6): {RESET}")

    if choice == "1":
        squares()
    elif choice == "2":
        table()
    elif choice == "3":
        table25()
    elif choice == "4":
        fruits()
    elif choice == "5":
        teachers()
    elif choice == "6":
        print(f"{RED}👋 Exiting program. Goodbye!{RESET}")
        break
    else:
        print(f"{RED}⚠️ Invalid choice, try again.{RESET}")