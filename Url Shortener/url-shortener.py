import random
import string

FILE_NAME = "urls.txt"

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def save_url(short, long_url):
    with open(FILE_NAME, "a") as file:
        file.write(f"{short},{long_url}\n")

def load_urls():
    urls = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                short, long_url = line.strip().split(",", 1)
                urls[short] = long_url
    except FileNotFoundError:
        pass
    return urls

def shorten_url(long_url):
    urls = load_urls()
    short = generate_short_code()
    while short in urls:
        short = generate_short_code()
    save_url(short, long_url)
    return short

def get_original_url(short):
    urls = load_urls()
    return urls.get(short, "URL not found!")

# -------- Program --------
while True:
    print("\n🔗 URL Shortener")
    print("1. Shorten URL")
    print("2. Get Original URL")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        short = shorten_url(long_url)
        print("Short URL: http://short.ly/" + short)

    elif choice == "2":
        short = input("Enter short code: ")
        print("Original URL:", get_original_url(short))

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice!")
