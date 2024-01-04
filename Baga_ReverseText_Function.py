forbidden_word = "nigga"
while True:
    personal_input = input("Enter a string:")
    if personal_input.isalpha():
        if forbidden_word not in personal_input.lower():
            print("Output:",personal_input[::-1])
            break
        else:
            print("Error Reported! Enter a different text.")
    else:
        print("Error Reported! Enter text only.")