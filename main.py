print("Welcome to seasons calculator!")
user_input = int(input("We can do this two ways. Type 1 to do the question-answer format, and 2 for entering-a-date format. "))
while user_input == 1 or user_input == 2:
  if user_input == 1:
    ninety_or_more_degrees = input("is it more than 90* outside today: ")
    if ninety_or_more_degrees == "yes":
      print("it is probably summertime")
      break
    if ninety_or_more_degrees == "no":
      fifty_or_less_degrees = input("Okay, then is it less than 50 degrees outside?")
      if fifty_or_less_degrees == "yes":
        print("it is probably winter")
        break
      if fifty_or_less_degrees == "no":
        leaves_on_trees = input("Okay, then are there leaves falling of the trees, or changing color: ")
        if leaves_on_trees == "yes":
          print("It is most likely fall")
          break
        if leaves_on_trees == "no":
          print("it is probably spring then")
          break
  if user_input == 2:
    season = "winter"
    month_num = int(input("Enter the number of your month, ie. January corresponds to 1: "))
    day_num = int(input("Enter the day of the month: "))
    if month_num > 6 and month_num < 9:
      season = "summer"
    if month_num < 6 and month_num > 2:
      season = "spring"
    if month_num > 9 and month_num <= 11:
      season = "fall"
    print("It is " + season)
    user_input = ("Enter 0 to terminate, 1 for Q&A format, and 2 for date format.")
if user_input == 0:
  print("Thanks for using seasons calculator!")
