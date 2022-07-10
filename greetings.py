import datetime

"""Time greetings"""
name = input("Enter your name:")
time = datetime.datetime.now()
hour = time.hour

# check  hour greetings
if hour < 12:
    greeting = ("Good morning", "Добрий ранок", "בוקר טוב")
elif hour < 18:
    greeting = ("Good afternoon", "Добрий день", "הצהריים טובים")
elif hour < 21:
    greeting = ("Good afternoon", "Добрий вечір", "ערב טוב")
else:
    greeting = ("Good night", "Добраніч", "לילה טוב")

# user language check
first_symbol = name[0]
if ord(first_symbol) < 127:  # English
    hello = greeting[0]
elif ord(first_symbol) >= 1024 and ord(first_symbol) <= 1279:  # Ukrainian
    hello = greeting[1]
elif ord(first_symbol) >= 1424 and ord(first_symbol) <= 1535:  # Hebrew
    hello = greeting[2]
else:
    print("Sorry, another language")

print(f"{name}", hello)
