import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def show_directory(path, indent=0):
    try:
        items = sorted(path.iterdir())
    except PermissionError:
        print(f"{'  ' * indent}{Fore.RED}[доступ заборонено]")
        return

    for item in items:
        prefix = "  " * indent
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/")
            show_directory(item, indent + 1)
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}")


def run():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: вкажіть шлях до директорії")
        print("Використання: python3 task3.py /шлях/до/директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях '{path}' не існує")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією")
        return

    print(f"{Fore.BLUE}{path.name}/")
    show_directory(path)


if __name__ == "__main__":
    run()