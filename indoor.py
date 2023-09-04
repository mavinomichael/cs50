def main():
    # get user input
    text = input("Please enter a text input")
    lower_case_text = convert_to_lowercase(text)
    print(lower_case_text)


def convert_to_lowercase(text: str):
    return text.lower()


main()
