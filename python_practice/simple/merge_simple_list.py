files = [
    ("01_check_even_odd.py", "Check Even or Odd",
     "Modulus operator (%) and if-else",
     "An integer number from the user",
     "Check remainder when divided by 2",
     "Print Even or Odd"),

    ("02_count_items.py", "Count Items in List",
     "len() function",
     "A predefined list",
     "Count total elements using len()",
     "Print total number of items"),

    ("03_check_banana.py", "Check Banana in List",
     "Membership operator (in)",
     "A list of fruits",
     "Check if 'banana' exists in list",
     "Print found or not found"),

    ("04_first_last_item.py", "First and Last Item",
     "List indexing",
     "A list",
     "Access first and last index",
     "Print first and last item"),

    ("05_print_positive_numbers.py", "Print Positive Numbers",
     "Loops and conditions",
     "A list of numbers",
     "Check numbers greater than zero",
     "Print positive numbers"),

    ("06_biggest_of_three.py", "Biggest of Three Numbers",
     "Comparison and if-elif",
     "Three numbers",
     "Compare numbers",
     "Print largest number"),

    ("07_sum_without_sum_function.py", "Sum Without sum()",
     "Loop and accumulator",
     "A list of numbers",
     "Add numbers one by one",
     "Print total sum"),

    ("08_second_largest.py", "Second Largest Number",
     "Sorting / logic",
     "A list of numbers",
     "Find second maximum",
     "Print second largest"),

    ("09_check_name.py", "Check Name in List",
     "String comparison",
     "Name and list",
     "Compare input name with list",
     "Print match result"),

    ("10_temperature_above_40.py", "Temperature Check",
     "Conditional check",
     "Temperature value",
     "Check if temperature > 40",
     "Print warning message")
]

with open("simple_list.py", "w", encoding="utf-8") as out:
    out.write("# ==============================================\n")
    out.write("# PYTHON BASIC PROGRAMS – STUDY & REVISION FILE\n")
    out.write("# Teacher Style Explanation Included\n")
    out.write("# ==============================================\n\n")

    for i, (fname, title, concept, inp, logic, output) in enumerate(files, 1):
        out.write(f"\n\n# ------------------------------------------\n")
        out.write(f"# Program {i}: {title}\n")
        out.write(f"# File: {fname}\n")
        out.write("# ------------------------------------------\n\n")

        out.write("# 🔑 Key Concept:\n")
        out.write(f"# {concept}\n\n")

        out.write("# 📥 Input:\n")
        out.write(f"# {inp}\n\n")

        out.write("# 🧠 Logic:\n")
        out.write(f"# {logic}\n\n")

        out.write("# 📤 Output:\n")
        out.write(f"# {output}\n\n")

        out.write("# 👨‍🏫 Teacher Explanation:\n")
        out.write("# This program demonstrates the basic use of Python logic.\n")
        out.write("# It helps beginners understand how input, logic, and output\n")
        out.write("# are connected in a simple program.\n\n")

        out.write("# ===== Code Starts Here =====\n")
        with open(fname, "r", encoding="utf-8") as f:
            out.write(f.read())
        out.write("\n# ===== Code Ends Here =====\n")
