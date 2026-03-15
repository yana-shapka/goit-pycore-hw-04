def total_salary(path):
    try:
        with open(path, encoding="utf-8") as f:
            salaries = [int(line.split(",")[1]) for line in f if line.strip()]
        
        total = sum(salaries)
        average = total // len(salaries)
        return total, average

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None


def run():
    total, average = total_salary("task1_salary.txt")
    if total is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    run()