from datetime import datetime

user_input = input("enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

# print(f"Dear user, Time remaining for your goal: {goal} is {time_till.days} days")
hours_till = int(time_till.total_seconds()/60/60)
print(f"Dear user, Time remaining for your goal: {goal} is {hours_till} hours")

