from datetime import date, timedelta


WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_birthdays_per_week(users):

    birthdays = defaultdict(list)
    today = date.today()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).weekday()
            birthdays[WEEKDAYS[weekday]].append(name)

    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")
