def convert_distance(feet: float,) -> list[float]:
    inches = feet * 12
    yards = feet * (1 / 3)
    miles = feet * 0.000189393939

    return inches, yards, miles


def main():
    try:
        feet = float(input("Введіть відстань у футах: "))
    except ValueError:
        print("Помилка: Введіть число")
        return
    inches, yards, miles = convert_distance(feet)

    print(f"{feet} футів це {inches} дюймів")
    print(f"{feet} футів це {yards} ярдів")
    print(f"{feet} футів це {miles} миль")


if __name__ == "__main__":
    main()
