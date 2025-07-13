with open("myfile.txt", "w") as f:
    f.write("Hello Jitendra!\n")
    f.write("This file was created using Python.\n")
    
with open("write_test1.txt", "w") as f:
    f.write("Line 1: Hello from w mode\n")
    f.write("Line 2: This file will be overwritten if run again.\n")
    
with open("write_test_output.txt", "w") as f:
    f.write("Saved safely inside src/file_handling!\n")
    
    
    from project_utils.save_to_txt import save_to_txt

log = "This is a test write using the utility.\n"
save_to_txt("test_write.txt", log)