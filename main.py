from datetime import datetime, timedelta
import random
import re

"""
Завдання 1
"""


def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            f"Неправильний формат дати: '{date}'. Очікується 'РРРР-ММ-ДД'."
        )

    today = datetime.today().date()
    delta = today - given_date

    return delta.days


# --- Тести ---
if __name__ == "__main__":
    print(get_days_from_today("2021-05-05"))
    print(get_days_from_today("2030-01-01"))
try:
    print(get_days_from_today("invalid-date"))
except ValueError as e:
    print(f"Помилка: {e}")


"""
Завдання 2
"""


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000 or quantity < 1:
        return []
    if min >= max:
        return []
    if quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


# --- Тести ---
if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    print("5 з 36:", get_numbers_ticket(1, 36, 5))

    print("min > max:", get_numbers_ticket(50, 10, 5))
    print("quantity > діапазон:", get_numbers_ticket(1, 5, 10))
    print("min < 1:", get_numbers_ticket(0, 49, 6))
    print("max > 1000:", get_numbers_ticket(1, 1001, 6))


"""
Завдання 3
"""


def normalize_phone(phone_number: str) -> str:
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    if cleaned.startswith("+"):
        pass
    elif cleaned.startswith("380"):
        cleaned = "+" + cleaned
    else:
        cleaned = "+38" + cleaned

    return cleaned


# --- Тести ---
if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


"""
Завдання 4
"""


def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta = (birthday_this_year - today).days
        if 0 <= delta <= 6:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming


# --- Тести ---
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Alice Brown", "birthday": "1992.03.08"},
        {"name": "Bob Martin", "birthday": "1988.03.09"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
