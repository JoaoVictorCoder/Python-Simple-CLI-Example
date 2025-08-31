list = ["item 1", "item 2", "item 3", "item 4"]


def main():
    for i, option in enumerate(list):
        print(f"[{i + 1}] {option.title()}")


if __name__ == "__main__":
    main()
