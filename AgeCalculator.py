#!/bin/python3
import datetime
print("Age Calculator for New Navigation.")
while True:
  def calculate_age(y,m,d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days / 365.25)
    print("The age of person is {} years.".format(age))

  try:
    ask_year = int(input("Enter year in yyyy format: "))
    ask_month = int(input("Enter month in  mm format: "))
    ask_date = int(input("Enter day in dd format: "))
    calculate_age(ask_year, ask_month, ask_date)
    ask_to_continue = input("Write yes to continue or press any key to exit: ").lower()
    if ask_to_continue == "yes":
      continue
    else:
      print("Thank You.")
      break
  except:
    print("Please enter in number.")
    
  