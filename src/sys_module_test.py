import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if len(sys.argv) > 2:
    print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
else:
    print("Usage: python sys_module_test.py <your_name> <challenge_name>")

print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")
# sys.exit() # Uncomment to see it exit the script
