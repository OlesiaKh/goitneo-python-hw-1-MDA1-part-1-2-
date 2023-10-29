
from datetime import datetime, timedelta

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
USERS = [
    {"name": "Ann", "birthday": datetime(year=1950, month=10, day=27).date()},
    {"name": "Charl", "birthday": datetime(year=1960, month=10, day=27).date()},
    {"name": "Richard", "birthday": datetime(year=1970, month=10, day=27).date()},
    {"name": "Alex", "birthday": datetime(year=1980, month=10, day=27).date()},
    {"name": "Max", "birthday": datetime(year=1990, month=10, day=27).date()},
]

def close_birthday_users(users, start, end):
    now = datetime.today().date()
    result = [user for user in users if start <= user["birthday"].replace(year=now.year) <= end]
    return result

def get_birthdays_per_week(users):
    now = datetime.today().date()
    current_week_day = now.weekday()
    if current_week_day >= 5:
        start_date = now - timedelta(days=(7 - current_week_day))
    elif current_week_day == 0:
        start_date = now - timedelta(days=2)
    else:
        start_date = now
    days_ahead = 4 - current_week_day
    if days_ahead < 0:
        days_ahead += 7
    end_date = now + timedelta(days=days_ahead)
    
    birthday_users = close_birthday_users(users, start=start_date, end=end_date)
    weekday = None
    result = {}  # Store birthday celebrants by day
    for user in sorted(birthday_users, key=lambda x: x["birthday"].replace(year=now.year).weekday()):
        user_birthday = user["birthday"].replace(year=now.year).weekday()
        user_congratulation_day = WEEKDAYS[user_birthday]
        
        if user_congratulation_day not in result:
            result[user_congratulation_day] = []
        
        result[user_congratulation_day].append(user["name"])
    
    for day, names in result.items():
        print(f"{day}: {', '.join(names)}")

if __name__ == "__main__":
    get_birthdays_per_week(USERS)
