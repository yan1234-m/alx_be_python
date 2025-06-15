<<<<<<< HEAD
# daily_reminder.py

# Loop until the user enters a valid priority level
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if priority not in ["high", "medium", "low"]:
        print("Please enter a valid priority: high, medium, or low.")
        continue
    if time_bound not in ["yes", "no"]:
        print("Please enter yes or no for time-bound.")
        continue
    break

# Match Case to handle priority-specific messages
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to do it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to do it this week.")
    
    case "low":
        if time_bound == "yes":
            print(f"\nNote: '{task}' is a low priority task, but it's time-sensitive. Don’t forget to finish it today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
=======
# daily_reminder.py

# Loop until the user enters a valid priority level
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if priority not in ["high", "medium", "low"]:
        print("Please enter a valid priority: high, medium, or low.")
        continue
    if time_bound not in ["yes", "no"]:
        print("Please enter yes or no for time-bound.")
        continue
    break

# Match Case to handle priority-specific messages
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to do it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to do it this week.")
    
    case "low":
        if time_bound == "yes":
            print(f"\nNote: '{task}' is a low priority task, but it's time-sensitive. Don’t forget to finish it today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
>>>>>>> 1e16496f5ce8cda0563cc2e8270560911993ecb4
