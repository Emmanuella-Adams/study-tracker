#we wil import data from json file
import json
import os

#we will then define our constants
data_file = 'data/logs.json'

#we will define our function which will extract the file and handle the errors if it came
def extract_logs():
    #this loads our study logs from the json file and then returns an empty list if there is none to avoud errors
    if not os.path.exists(data_file): #checks if the file is not there
        return [] #returning en[mpty string
    
    try:
        with open(data_file, 'r') as f:
            #opening our file and reading it as f
            logs = json.load(f)

            if isinstance(logs ,list): #this checks if it is a list
                return logs
            else:
                print('WARNING! data file is incorrect. starting fresh.')
                return[]
            
    except json.JSONDecodeError:
        print('WARNING: data file corrupted (invalid JSON format). starting fresh.')
        return []
    except Exception as e:
        print(f'An unexpected error occured while loading logs: {e}')


def save_logs(logs):
    #this saves the list of study logs to the json file

    try:
        #we'll make sure the data directory exists before trying to write the file
        os.makedirs(os.path.dirname(data_file), exist_ok=True)

        with open(data_file, 'w') as f:

            #we use indent=4 for easy human reeading
            json.dump(logs , f , indent = 4)

        print('logs saved successfully!')

    except Exception as e:
        print(f"❌ Error saving logs: {e}")


        
def validate_number(prompt):
    """
    Prompts the user and ensures the input is a positive integer.
    """
    while True:
        try:
            value = input(prompt)
            num = int(value)
            if num > 0:
                return num
            else:
                print("❌ Duration/Input must be a positive number.")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")


#we then create a function that calls on the current date

from datetime import datetime

def get_current_date():
    
    return datetime.now().strftime('%y-%m-%d')

#we then implement the core infrastructure

def add_study_session():

    #load existing data
    logs = extract_logs()
    print('\n ADD NEW STUDY SESSION')

    #prompt for input
    subject = input('subjects studied: ').strip
    duration = validate_number('duration in minutes, please input a positive integer: ')
    notes = input('Inputes notes taken (optional)').strip

    #get the current date for the log entry
    date = get_current_date()

    #create new session dictionary

    new_session = {

        'subject': subject,
        'duration' : duration,
        'notes' : notes,
        'date' : date
    }

    #to append the new session
    logs.append(new_session)


    #to save the logs
    save_logs(logs)

    print('new session successfully updated')