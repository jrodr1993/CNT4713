# Assignment 2 - Juan Rodriguez
import datetime
import socket


class Assignment2:

    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f"Your age is {age}")

    def listAnniversaries(self):
        today = datetime.date.today()
        currentYear = today.year
        anniInt = 10
        anni = []

        while (self.year + anniInt) <= currentYear:
            anni.append(anniInt)
            anniInt += 10

        return anni

    def modifyYear(self, n):
        moddedStringYear = (str(self.year)[:2] * n) + str(self.year * n)[::2]

        return moddedStringYear

    @staticmethod
    def checkGoodString(string):
        condition1 = False
        condition2 = False
        condition3 = False

        if len(string) >= 9:
            condition1 = True

        if string[0].islower():
            condition2 = True

        numbers = sum(c.isdigit() for c in string)
        if numbers == 1:
            condition3 = True

        if condition1 and condition2 and condition3:
            return True
        else:
            return False


    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                return True
        except socket.error as e:
            return False


