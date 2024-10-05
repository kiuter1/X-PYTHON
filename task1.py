from time import sleep
from colorama import Fore


def washing(is_washing: bool = None):
    for i in range(0, 101, 2):
        print(Fore.CYAN + f"Набір води {i}%", end="\r")
        sleep(0.05)

    for i in range(1, 101):
        if i == 1:
            print("\r")
        print(Fore.YELLOW + f"Прання одягу {i}%", end="\r")
        sleep(0.05)

    for i in range(1, 101, 7):
        if i == 1:
            print("\r")
        if i == 99:
            i = 100
        print(Fore.LIGHTBLUE_EX + f"Полоскання одягу {i}%", end="\r")
        sleep(0.1)

    for i in range(1, 101, 20):
        if i == 1:
            print("\n")
        if i == 81:
            i = 100
        print(Fore.LIGHTBLACK_EX + f"Злив води {i}%", end="\r")
        sleep(0.1)

    if is_washing:
        for i in range(1, 101, 10):
            if i == 1:
                print("\r")
            if i == 91:
                i = 100
            print(Fore.LIGHTCYAN_EX + f"Віджимання одягу {i}%", end="\r")
            sleep(0.1)


def start():
    is_washing = not bool(input('Віджимати одяг? (Натисніть «Enter» якщо ні або впишіть щось якщо так): '))
    starts = input("Для початку прання нажміть Enter: ")

    if not starts:
        washing(is_washing)
        print("\n")
        print(Fore.GREEN + "Прання завершено")
    else:
        print(Fore.RED + "Скасування")


if __name__ == '__main__':
    start()
