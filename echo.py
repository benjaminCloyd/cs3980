# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    textLength = len(text)
    for i in range(repetitions, 0, -1):
        print(text[textLength - i :])
    return "."


if __name__ == "__main__":
    text = input("Yell at a mountain: ")
    print(echo(text))
