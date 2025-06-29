students = ["Akash“,"Ravi","Vinod", "Aditya", "Amit"] # --> Small Correction needed here!
print(f"First student: {students [0]}")
print(f"Last student: {students[-1]}")
print(f"First two students: {students[:2]}")
print(f"Last three students: {students[2:]}")
print(f"Last two students: {students[3:]}") # This correctly gets 'Aditya' and 'Amit'
print(f"Last second student:{students[-2]}")
print(f"Last student:{students [-1]}") # This is a duplicate of the earlier 'Last student' print
