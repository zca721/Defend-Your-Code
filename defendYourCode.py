# Team 3: Zach Anderson, Nathaniel Roy, Jennifer Huynh
# TCSS 483 - team assignment - defend your code

# imports regular expressions, hash and salt libraries
import re, hashlib, os

class Verification:
    # Constructor for Verification class
    def __init__(self):
        self.salt = os.urandom(32)
        self.stringMax = 50
        self.maxInteger = 2147483647
        self.minInteger = -2147483648

    # Checks if first name entered by user is a valid input
    def verifyFirstName(self, string):
        # ^                     -> Start of the string.
        # [A-Z]{1}              -> Must have 1 uppercase letter
        # [a-z]*                -> Can have any number of lowercase letters
        # $                     -> End of the string.
        pattern = "^[A-Z]{1}[a-z]*$"
        # Checks regex pattern with input string and returns true if valid input
        valid = re.search(pattern, string)

        # Checks if valid is true and the string is less than or equal to 50 characters
        if valid and (len(string) <= self.stringMax):
            text = open("pythonOutput.txt", "a")
            text.write("First Name: " + string + "\n")
            text.close()
            print("verifyFirstName: " + string + " Valid input")
            return True
        else:
            print("verifyFirstName: " + string + " Invalid input, try again")
            return False

    # Checks if last name entered by user is a valid input
    def verifyLastName(self, string):
        # ^                     -> Start of the string.
        # [A-Z]{1}              -> Must have 1 uppercase letter
        # [a-z]*                -> Can have any number of lowercase letters
        # $                     -> End of the string.
        pattern = "^[A-Z]{1}[a-z]*$"
        # Checks regex pattern with input string and returns true if valid input
        valid = re.search(pattern, string)

        # Checks if valid is true and the string is less than or equal to 50 characters
        if valid and (len(string) <= self.stringMax):
            text = open("pythonOutput.txt", "a")
            text.write("Last Name: " + string + "\n")
            text.close()
            print("verifyLastName: " + string + " Valid input")
            return True
        else:
            print("verifyLastName: " + string + " Invalid input, try again")
            return False

    # Checks if both numbers entered by user are valid inputs
    def verifyTwoIntegers(self, stringOne, stringTwo):
        # ^                     -> Start of the string.
        # \\-?                  -> Optional -
        # [0-9]+                -> Must have at least 1 number
        # $                     -> End of the string.
        pattern = "^\\-?[0-9]+$"
        # Checks regex pattern with input string and returns true if valid input
        validOne = re.search(pattern, stringOne)
        validTwo = re.search(pattern, stringTwo)

        # Checks if validOne and validTwo are both true and both stringOne and stringTwo are not -0
        if validOne and validTwo and stringOne != "-0" and stringTwo != "-0":
            # Assigns stringOne and stringTwo to an integer value
            integerOne = int(stringOne)
            integerTwo = int(stringTwo)
            # Checks if both integerOne and integerTwo are within the range of a 4 btye integer
            if integerOne <= self.maxInteger and integerOne >= self.minInteger and integerTwo <= self.maxInteger and integerTwo >= self.minInteger:
                # Adds the two integers together
                addedInteger = integerOne + integerTwo
                # Multiples the two integers together
                multipliedInteger = integerOne * integerTwo
                # Checks if addedInteger and multipledInterger are within the range of a 4 byte integer
                if addedInteger <= self.maxInteger and addedInteger >= self.minInteger and multipliedInteger <= self.maxInteger and multipliedInteger >= self.minInteger:
                    text = open("pythonOutput.txt", "a")
                    text.write("First Integer: " + str(integerOne) + "\n")
                    text.write("Second Integer: " + str(integerTwo) + "\n")
                    text.write("Added Integer: " + str(addedInteger) + "\n")
                    text.write("Multiplied Integer: " + str(multipliedInteger) + "\n")
                    text.close()
                    print("verifyTwoIntegers: " + stringOne + " and " + stringTwo + " Valid input")
                    return True
                else:
                    print("verifyTwoIntegers: " + stringOne + " and " + stringTwo + " Invalid input, try again")
                    return False
            else:
                print("verifyTwoIntegers: " + stringOne + " and " + stringTwo + " Invalid input, try again")
                return False
        else:
            print("verifyTwoIntegers: " + stringOne + " and " + stringTwo + " Invalid input, try again")
            return False

    # Checks if input text file entered by user is a valid input
    def verifyInputFile(self, string):
        # ^                     -> Start of the string.
        # pythonInput.txt       -> Allows only one input text file by the name pythonInput.txt
        # $                     -> End of the string.
        pattern = "^pythonInput.txt$"
        # Checks regex pattern with input string and returns true if valid input
        valid = re.search(pattern, string)

        # Checks if valid is true
        if valid:
            text = open("pythonOutput.txt", "a")
            text.write("Input File Name: " + string + "\n")
            text.close()
            with open("pythonInput.txt", "r") as file:
                # Read all content from input text file
                content = file.read()
                text = open("pythonOutput.txt", "a")
                # Writes all content from input text file
                text.write(content + "\n")
                text.close()
            print("verifyInputFile: " + string + " Valid input")
            return True
        else:
            print("verifyInputFile: " + string + " Invalid input, try again")
            return False

    # Checks if output text file entered by user is a valid input
    def verifyOutputFile(self, string):
        # ^                     -> Start of the string.
        # pythonOutput.txt      -> Allows only one input text file by the name pythonOutput.txt
        # $                     -> End of the string.
        pattern = "^pythonOutput.txt$"
        # Checks regex pattern with input string and returns true if valid input
        valid = re.search(pattern, string)

        # Checks if valid is true
        if valid:
            print("verifyOutputFile: " + string + " Valid input")
            return True
        else:
            print("verifyOutputFile: " + string + " Invalid input, try again")
            return False

    # Checks if password entered by user is a valid input
    def verifyInputPassword(self, string):
        # ^                     -> Start of the string.
        # (?=(.*[A-Z]))         -> Ensures at least one uppercase letter
        # (?=(.*[a-z]))         -> Ensures at least one lowercase letter
        # (?=(.*\d))            -> Ensures at least one digit
        # (?=(.*[\W_]))         -> Ensures at least one special character
        # (?!.*[a-z]{4,})       -> Negative lookahead: Prevents four or more consecutive lowercase letters
        # \S{10,}               -> Ensures a minimum length of 10 characters, where \S matches any non-whitespace character
        # $                     -> End of the string
        pattern = "^(?=(.*[A-Z]))(?=(.*[a-z]))(?=(.*\\d))(?=(.*[\\W_]))(?!.*[a-z]{4,})\\S{10,}$"
        # Checks regex pattern with input string and returns true if valid input
        valid = re.search(pattern, string)

        # Checks if valid is true
        if valid:
            # Salts and hashes password
            hashedPassword = hashlib.pbkdf2_hmac('sha256', string.encode('utf-8'), self.salt, 100000)

            text = open("pythonDatabase.txt", "a")
            # Stores salt and hashed password in database
            text.write(str(hashedPassword) + "\n")
            text.write("----------------------------------------------------------------------------------------- " + "\n")
            text.close()
            print("verifyInputPassword: " + string + " Valid input")
            return True
        else:
            print("verifyInputPassword: " + string + " Invalid input, try again")
            return False

    # Checks if re-entered password matches with salt and hashed password stored in database matches
    def verifyDatabasePassword(self, string):
        # Salts and hashes password
        hashedPassword = hashlib.pbkdf2_hmac('sha256', string.encode('utf-8'), self.salt, 100000)

        with open("pythonDatabase.txt", "r") as file:
            # Read all content from database text file
            content = file.read()
            # Checks if salt and hashed password matches previously stored salt and hashed password
            if str(hashedPassword) in content:
                print("verifyDatabasePassword: " + string + " Valid input")
                return True
            else:
                print("verifyDatabasePassword: " + string + " Invalid input, try again")
                return False

class Main:
    # Constructor for Main class
    def __init__(self):
        self.repeat = True
        self.question = 0
        self.verification = Verification()

    # Main runs continuously until valid input is entered by user for all questions
    def main(self):

        # Display for valid user input in pythonOutput.txt
        text = open("pythonOutput.txt", "a")
        text.write("Valid User Input:------------------------------------------------------------------------ " + "\n")
        text.close()

        # While repeat is true continue to ask questions
        while self.repeat:
            if self.question == 0:
                print("Only first letter can be capitalized, 50 characters max")
                # Gets console input from user
                userFirstName = input("Enter First Name: ")
                # If valid input then return true and move onto the next question
                if self.verification.verifyFirstName(userFirstName):
                    self.question = 1
                    print("---------------------------------------------------------------")

            elif self.question == 1:
                print("Only first letter can be capitalized, 50 characters max")
                # Gets console input from user
                userLastName = input("Enter Last Name: ")
                # If valid input then return true and move onto the next question
                if self.verification.verifyLastName(userLastName):
                    self.question = 2
                    print("---------------------------------------------------------------")

            elif self.question == 2:
                print("2 ints between -2147483648 and 2147483647")
                print("Space in between")
                print("Allows leading zeros")
                print("If the two ints adds or multiples to a number greater than the range, it will reprompt")
                # Gets console input from user
                twoIntegers = input("Enter two numbers with single space inbetween: ")
                # User enters two numbers seperated by a single space and splits them and stores each number in a list
                splitString = twoIntegers.split(" ")
                # If the list has two numbers then assign them to inputOne and inputTwo and send them to verifyInt()
                if len(splitString) == 2:
                    inputOne = splitString[0]
                    inputTwo = splitString[1]
                    # If valid input then return true and move onto the next question
                    if self.verification.verifyTwoIntegers(inputOne, inputTwo):
                        self.question = 3
                        print("---------------------------------------------------------------")
                else:
                    print("verifyTwoIntegers: Invalid input, try again")

            elif self.question == 3:
                print("Python only accepts pythonInput.txt")
                # Gets console input from user
                textFile = input("Enter input text file: ")
                # If valid input then return true and move onto the next question
                if self.verification.verifyInputFile(textFile):
                    self.question = 4
                    print("---------------------------------------------------------------")

            elif self.question == 4:
                print("Python only accepts pythonOutput.txt")
                # Gets console input from user
                textFile = input("Enter output text file: ")
                # If valid input then return true and move onto the next question
                if self.verification.verifyOutputFile(textFile):
                    self.question = 5
                    print("---------------------------------------------------------------")

            elif self.question == 5:
                print("One capital letter, one special character, one number, at least 10 characters") 
                print("One lowercase letter and no more than three consecutive lowercase letters")
                # Gets console input from user
                userPassword = input("Enter valid password: ")
                # If valid input then return true and move onto the next question
                if self.verification.verifyInputPassword(userPassword):
                    self.question = 6
                    print("---------------------------------------------------------------")

            elif self.question == 6:
                print("One capital letter, one special character, one number") 
                print("One lowercase letter and no more than three consecutive lowercase letters")
                # Gets console input from user
                userPasswordVerified = input("Enter password again: ")
                # If valid input then return true and end the while loop
                if self.verification.verifyDatabasePassword(userPasswordVerified):
                    self.repeat = False
                    print("---------------------------------------------------------------")

        text = open("pythonOutput.txt", "a")
        text.write("----------------------------------------------------------------------------------------- " + "\n")
        text.close()

# Runs main
if __name__ == '__main__':
   main = Main()
   main.main()