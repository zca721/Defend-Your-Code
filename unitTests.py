# Team 3: Zach Anderson, Nathaniel Roy, Jennifer Huynh
# TCSS 483 - team assignment - defend your code

# Imports Verification class from defendYourCode file
from defendYourCode import Verification

class UnitTests:
    # Constructor for UnitTests class
    def __init__(self):
        self.verification = Verification()

    # Function for unit tests of verifyFirstName
    def firstNameUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        firstName = ["Z", "Abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx", "A", "Za",
                     "z", "Abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy", "", " ", "ZA", "1", "!", "aZ"]
        
        # Each index of firstName is iterated through and input as an argument
        for string in firstName:
            self.verification.verifyFirstName(string)

    # Function for unit tests of verifyLastName
    def lastNameUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        lastName = ["Z", "Abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx", "A", "Za",
                     "z", "Abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy", "", " ", "ZA", "1", "!", "aZ"]
        
        # Each index of lastName is iterated through and input as an argument
        for string in lastName:
            self.verification.verifyLastName(string)

    # Function for unit tests of verifyTwoIntegers
    def twoIntegersUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        firstInteger = ["100", "0", "0", "0", "1", "-1", "-1", "1", "9", "-9", "01",
                        "1", "-1", "1.0", " ", "a", "-", "-0", "2147483647", "-2147483648"]
        # Top row in list is valid input and bottom row in list is invalid input
        secondInteger = ["100", "2147483647", "-2147483648", "0", "2147483646", "-2147483647", "2147483647", "-2147483648", "238609294", "238609294", "01",
                         "2147483647", "-2147483648", "1.0", " ", "z", "-", "-0", "2147483647", "-2147483648"]

        # Each index of firstInteger and secondInteger are iterated through simultaneously and input as pair arguments
        for integerOne, integerTwo in zip(firstInteger, secondInteger):
            self.verification.verifyTwoIntegers(integerOne, integerTwo)

    # Function for unit tests of verifyInputFile
    def inputFileUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        inputFile = ["pythonInput.txt",
                     "README.txt", "pythonOutput.txt", "pythonDatabase.txt", "pythoninput.txt", " pythonInput.txt", "pythonInput.pdf"]
        
        # Each index of inputFile is iterated through and input as an argument
        for string in inputFile:
            self.verification.verifyInputFile(string)

    # Function for unit tests of verifyOutputFile
    def outputFileUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        outputFile = ["pythonOutput.txt",
                     "README.txt", "pythonIntput.txt", "pythonDatabase.txt", "pythonoutput.txt", " pythonOutput.txt", "pythonOutput.pdf"]
        
        # Each index of outputFile is iterated through and input as an argument
        for string in outputFile:
            self.verification.verifyOutputFile(string)

    # Function for unit tests of verifyInputPassword
    def inputPasswordUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        inputPassword = ["FourFive_9", "1!dogCatRat", "ABCabcDEFdefGHIghiJKLjklMNOmnoPQRpqrSTUstuVWXvwxYZyz0123456789`~!@#$%^&*()-_=+,<.>/?;:\"\'[{]}\\|",
                         "SixSeven_0", "NineTen_1", "OneTwoSix7", "FourFive 9", "TenSixOne!", "FourFive $9"]

        # Each index of inputPassword is iterated through and input as an argument
        for string in inputPassword:
            self.verification.verifyInputPassword(string)

    # Function for unit tests of verifyDatabasePassword
    def databasePasswordUnitTests(self):
        # Top row in list is valid input and bottom row in list is invalid input
        databasePassword = ["FourFive_9", "1!dogCatRat", "ABCabcDEFdefGHIghiJKLjklMNOmnoPQRpqrSTUstuVWXvwxYZyz0123456789`~!@#$%^&*()-_=+,<.>/?;:\"\'[{]}\\|",
                            "SixSeven_0", "NineTen_1", "OneTwoSix7", "FourFive 9", "TenSixOne!", "FourFive $9"]

        # Each index of databasePassword is iterated through and input as an argument
        for string in databasePassword:
            self.verification.verifyDatabasePassword(string)
            

class Main:
    # Constructor for Main class
    def __init__(self):
        self.unitTests = UnitTests()

    # Runs all unit tests for all functions in Verification class and prints valid input to pythonOutput.txt
    def main(self):

        # Display for valid unit tests in pythonOutput.txt
        text = open("pythonOutput.txt", "a")
        text.write("Valid Unit Tests:------------------------------------------------------------------------ " + "\n")
        text.close()

        self.unitTests.firstNameUnitTests()
        print("---------------------------------------------------------------")
        self.unitTests.lastNameUnitTests()
        print("---------------------------------------------------------------")
        self.unitTests.twoIntegersUnitTests()
        print("---------------------------------------------------------------")
        self.unitTests.inputFileUnitTests()
        print("---------------------------------------------------------------")
        self.unitTests.outputFileUnitTests()
        print("---------------------------------------------------------------")
        self.unitTests.inputPasswordUnitTests()
        print("---------------------------------------------------------------")
        self.unitTests.databasePasswordUnitTests()
        print("---------------------------------------------------------------")

        text = open("pythonOutput.txt", "a")
        text.write("----------------------------------------------------------------------------------------- " + "\n")
        text.close()

# Runs main
if __name__ == '__main__':
   main = Main()
   main.main()
