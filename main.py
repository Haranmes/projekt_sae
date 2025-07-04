from konsolenmenue import *


def main():
    try:
        loop_konsolen_menue()
    except Error as e:
        print(f"Fehler: {e}")


if __name__ == "__main__":
    main()