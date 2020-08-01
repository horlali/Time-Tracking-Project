# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:47:15 2020

@author: horla.li
"""

from datetime import datetime
import csv

# Customer and Task/Project Information
customer_name = input('Enter Customer Name Here \n')
customer_contact = input('Enter Customer Contact Here \n')
customer_location = input('Enter Customer Location Here \n')


# Capturing System Date
system_date = datetime.now().date()


# Accepting User Input: Task Name, Start Time and End Time
# This code takes the user start and end time as a string
task_name = input('Enter task to be performed here \n')
start_time = input('Enter start time in this format: HH:MM AM/PM: ')
end_time = input('Enter end time in this format: HH:MM AM/PM: ')

#time_format = '%I:%M %p'


# Converting the Start and End time from string to Datetime by using the strptime() method
start_time = datetime.strptime(start_time, '%I:%M %p') 
end_time = datetime.strptime(end_time, '%I:%M %p')


# The hours spend on a work during a day
# We will do this by diving the total seconds spents by 3600 second; this is equivalent to 1hr  
time_spent = round(((end_time - start_time).seconds) / 3600, 2)


# Calculating the Amount of Money the User Earns for Work Done

price_per_hour = 5            # amount in dollars
amount_due = round((time_spent*price_per_hour))


#Recording All Information Collected
records = []

# Convert from datetime format to string using datetime.strftime 
system_date = datetime.strftime(system_date, '%D')
start_time = datetime.strftime(start_time, '%I:%M %p')
end_time = datetime.strftime(end_time, '%I:%M %p')

records.append(customer_name)
records.append(customer_contact)
records.append(customer_location)
records.append(task_name)
records.append(system_date)
records.append(start_time)
records.append(end_time)
records.append(time_spent)
records.append(amount_due)


# Passing the information collected into a csv file
with open('record_book.csv', mode = 'a') as record_book:
    record_writer = csv.writer(record_book, delimiter = ',')
    record_writer.writerow(records)


# View the results 
print ('\n') 
print ('..'*40) 
print ('Date : {}'.format(system_date)) 
print ('Total hours spent on the work : {}'.format(time_spent)) 
print ("Amount of money earned for the day : ${:0,.2f}".format(amount_due)) 
print ('..'*40) 
print ('Information written to records successfully') 






