# Brute Force Simulator

## Short Description
Attack testing.

## Brief Description
This work models an automated credential brute force attack performed on a test login system to gain insight into account lockout functions.

It is meant for purely educational and authorized testing purposes only.

## Tools Used
- Python
- Flask
- Requests
- VS Code
- GitHub

## How to Implement
1. create a login server for testing using Flask
2. Now, define valid credentials and the maximum number of login attempts that 
3. Generate word list with several passwords.
4. Use a Python script to iterate over the word list.
5. Automate login requests to the test server.
6. Lock the account after multiple attempts.

## Project Structure
- test_login_server.py – Authorized test login server
- brute_force_simulator.py – Brute force attack simulation script
- wordlist.txt – Password list
- requirements.txt – Required Python libraries

## Output
After several unsuccessful login tries, the system locks the account and shows the following:: Account locked after multiple attempts

## Tips
You may only use this project for learning/ ethical security testing on approved testing platforms.

## Conclusion
 The Brute Force Simulator project effectively illustrates how brute force attacks function and how account lockout functionality protects against brute force attacks.