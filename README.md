# Brute-Force-Password-Cracker
This Python script demonstrates a brute force attack to crack passwords by systematically trying every possible combination of characters until it finds a match.
How It Works:

Takes a target password as input from the user
Defines a character set containing lowercase letters, numbers, and special symbols
Generates all possible combinations starting from length 1 up to the target password's length
Tests each combination against the target password
Tracks the number of attempts, time elapsed, and displays the cracked password when found

Key Features:

Uses itertools.product() to generate character combinations efficiently
Provides real-time feedback by printing each guess
Measures performance metrics (attempts and execution time)
Demonstrates the computational intensity of brute force attacks

Educational Purpose:
This project illustrates why strong, long passwords are crucial for security—the longer and more complex a password, the exponentially more time it takes to crack through brute force. It's a practical demonstration of password vulnerability and the importance of cybersecurity best practices.
