# This python program will populate a csv with rows and columns 
import random 
import datetime


def makeName():
    name = ["Alice" , "Bob", "Charlie" , "Jackson" , "Nick" , "Kyle" , "Tony" , "Grace" ,"Fred" , "Johnny" , "JP", "Joyce" , "Tim"]
    return random.choice(name)

def makeDOB():
    #00/00/0000
    #mo/d/year
    year = random.randint(1900, datetime.today.year)
    mo = random.randint(1,12)
    if mo in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif mo in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # February, handle leap years
        day = random.randint(1, 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28)
    

def main():
    print(makeName())

main()