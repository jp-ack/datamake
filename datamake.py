# This python program will populate a csv with rows and columns 
import random 
from datetime import datetime


def makeName():
    name = ["Alice" , "Bob", "Charlie" , "Jackson" , "Nick" , "Kyle" , "Tony" , "Grace" ,"Fred" , "Johnny" , "JP", "Joyce" , "Tim"]
    return random.choice(name)

def makeDOB():
    #00/00/0000
    #mo/d/year
    year = random.randint(1900, datetime.today().year)
    mo = random.randint(1,12)
    if mo in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif mo in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # February, handle leap years
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):  # Leap year check
            day = random.randint(1, 29)  # Leap year February has 29 days
        else:
            day = random.randint(1, 28)  # Non-leap year February has 28 days
    
    # Return the formatted date in the format mm/dd/yyyy
    return f"{mo:02}/{day:02}/{year}"
       
def assignOccupation():
    occupations = ["accounting" , "legal" , "human_resources"]
    return random.choice(occupations)

def main():
    # name , dob , occupation
    print(makeName().capitalize(),makeDOB(),assignOccupation())

main()
