#!/bin/bash

# Variables
name="Jitendra"
echo "Hi, $name! Welcome to Bash scripting."

# User input
echo "What is your name?"
read user_name
echo "Welcome, $user_name!"

# If-else
num=10
if [ $num -gt 5 ]; then
  echo "Greater than 5"
else
  echo "Not greater than 5"
fi

# For loop
for i in 1 2 3 4 5
do
  echo "Number: $i"
done

