# This python program will populate a csv with rows and columns 
import random 
import csv
from datetime import datetime
import sys


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

    
#generates rows and columns in form of csv    
def make_csv(num_of_rows,output_file_name):
    #make the header and csv file
    header = ["NAME","DOB","JOB"]
    
    csv_filename = str(output_file_name)+".csv"
    
    with open(csv_filename,mode = "w",newline="") as file:  ## error was happening earlier because the while loop was outside of the 'open' block. which automatically closes the file
        writer = csv.writer(file)
        writer.writerow(header)
       
        i = 1
        while (i <= int(num_of_rows)):
            print(f"Writing row {i}")
            writer.writerow([makeName(),makeDOB(),assignOccupation()]) ## this issue is that this needs to be a single list 
            i+=1
            
    print(f"finished writing csv ,overwrote {output_file_name}.csv")
            


#Run    
def main():
    make_csv(sys.argv[1],sys.argv[2]) # passes the argument specified on command line 

if __name__ == "__main__":
    main()
