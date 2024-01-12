import morse_code

user_text = input("Please enter text to convert to morse code:\n")
print(f"Morse code for your text is: \n{morse_code.text_to_morse(user_text=user_text)}")
