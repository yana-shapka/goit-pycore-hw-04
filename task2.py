def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as f:
            cats = []
            for line in f:
                if line.strip():
                    cat_id, name, age = line.strip().split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
        return cats

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []


def run():
    cats = get_cats_info("task2_cats.txt")
    if cats:
        print(cats)


if __name__ == "__main__":
    run()