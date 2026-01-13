# Brute Force simulator

## Brief Description

Attack Testing.

## Brief Description

This paper models an automated attack by Credential Bruteforce on a test login web application in order to understand lock out mechanisms on user accounts.
It is intended exclusively for educational testing by authorized personnel.
# Tools Used
    Python
- Python
- Flask

- Requests
- VS Code
- GitHub
## How To Do
1. create login server for testing using Flask
2. Now, define valid credentials and the maximum number of attempts allowed to login

3. Produce the word list with several passwords.
4. Use a Python script to iterate through the list of words.
5. Automate login to the testing environment.
6. Lock the account after multiple attempts.

## Project Structure
First,

- test_login_server.py – Authorized test login server
- brute_force_simulator.py – Brute force simulation script - wordlist.txt – password list - requirements.txt – The required Python libraries

 ## Output 
 When the user fails several times when trying to log into the system, the system locks the account and displays the following:     
 Account locked after multiple attempts 
     
 ## Tips
  This project is for educational/ethical security testing purposes only and can only be used on approved testing platforms.

## Conclusion
 The Brute Force Simulator project exemplifies the process of brute force attacks and the protection mechanisms for brute force attacks offered by the account lockout feature.