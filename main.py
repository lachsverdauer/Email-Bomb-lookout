import os
import smtplib
from smtplib import SMTPAuthenticationError
import sys
import time
import random
from config import senders_info

# Clear the screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

clear_screen()

def email_flying_animation(duration=3):
    envelope = "📧"
    distance = 50  # Adjust based on your terminal width
    start_time = time.time()

    while time.time() - start_time < duration:
        for position in range(distance):
            sys.stdout.write('\r' + ' ' * position + envelope)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust for speed
        for position in range(distance, 0, -1):
            sys.stdout.write('\r' + ' ' * position + envelope)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust for speed

    sys.stdout.write('\r' + ' ' * distance + ' ' + '\n')  # Clear the line after animation

# Function to read and print ASCII art from file
def print_ascii_art_from_file(file_path):
    RED = '\033[91m'
    END = '\033[0m'
    with open(file_path, 'r') as file:
        ascii_art = file.read()
        print(f"{RED}{ascii_art}{END}")

# ASCII art file path
ascii_art_file_path = 'yoda.txt'
print_ascii_art_from_file(ascii_art_file_path)

BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'

def get_non_negative_integer(prompt):
    while True:
        try:
            print(f"{BLUE}{prompt}{END}", end='')
            value = input()
            print(f"{RED}{value}{END}\n")  # Echo back the input in red
            integer_value = int(value)
            if integer_value < 0:
                raise ValueError("The number cannot be negative.")
            return integer_value
        except ValueError as e:
            print(f"{RED}Invalid input. Please enter a non-negative integer.\n{END}", str(e))

def get_non_empty_input(prompt, error_message="Input cannot be empty. Please try again."):
    while True:
        print(f"{BLUE}{prompt}{END}", end='')
        value = input().strip()
        if not value:
            print(f"{RED}{error_message}{END}\n")
        else:
            print(f"{RED}{value}{END}\n")  # Echo back the input in red
            return value


def select_email_service():
    print(f"{BLUE}Select which Email the recipient uses:{END}")
    print(f"{RED}[1] Gmail")
    print(f"[2] Outlook")
    print(f"[3] Other{END}")
    
    while True:
        choice = input(f"{BLUE}Mail Server: {END}").strip()
        if choice in ['1', '2', '3']:
            print(f"{RED}{choice}{END}\n")  # Optionally echo back the choice in red
        if choice == '1':
            return 'gmail'
        elif choice == '2' or choice == '3':
            return 'outlook'
        else:
            print(f"{RED}Invalid selection. Please enter 1, 2, or 3.{END}\n")



# Service selection
email_service = select_email_service()

if email_service == 'gmail':
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
else: 
    smtp_server = 'smtp.office365.com' 
    smtp_port = 587

sender_email, sender_password = random.choice(senders_info[email_service])

# Email content and recipient details
recipient_email = get_non_empty_input("Please enter the recipient's email address: ")
recipient_name = get_non_empty_input("What is the recipient's name?: ")
sender_alias = get_non_empty_input("Enter the display name for the sender (IMPORTANT: DO NOT USE YOUR REAL NAME!): ")
number_of_emails_per_account = get_non_negative_integer("How many emails would you like to send per account?: ")
delay = get_non_negative_integer("Enter the delay (in seconds) between sending emails: ")

# Randomized sentences to not be thrown into the spam folder
message_sentences = [
    "Greetings from the tropical beaches of Hawaii, where relaxation awaits.",
    "Our arrival was greeted by the warm sands and azure waters.",
    "Mystical sunsets mirrored the vibrant hues of the sea, a sight to behold.",
    "Hidden coves and secret tide pools were unveiled on our walks.",
    "Ancient volcanoes stood tall, whispering centuries-old tales.",
    "Local hospitality turned meals into luau feasts among new friends.",
    "Evenings were alive with the sound of ukulele music.",
    "We learned the art of surfing, from paddling to riding the waves.",
    "Artisan crafts at local markets showcased Hawaii's heritage.",
    "A boat journey offered breathtaking views of the coastline.",
    "Early mornings revealed the majestic sight of humpback whales.",
    "The history of the native Hawaiian culture enriched our journey.",
    "Each path revealed stunning panoramas of lush landscapes.",
    "Leaving the beaches was bittersweet, with memories to cherish.",
    "Dreams of our next tropical adventure are already taking shape.",
    "The warm breeze and sunny skies made every view picturesque.",
    "Nights under the palm trees felt like stepping into another world.",
    "Every meal was an introduction to delicious island cuisine.",
    "The serenity of the islands was unlike anything we've experienced.",
    "We left inspired by the spirit and beauty of Hawaii."
]

for sender_email, sender_password in senders_info[email_service]:
    email_counter = 1  # Reset counter for each sender
    print(f"{RED}Sending from {sender_email}\n{END}")
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            try:
                server.login(sender_email, sender_password)
                print(f"{RED}Login successful. Preparing to send emails...\n{END}")
                email_flying_animation(duration=2)  # Show animation for 2 seconds
            except SMTPAuthenticationError:
                print(f"{RED}Failed to send email from {sender_email}. The username or password might be incorrect. Please check your credentials and try again.{END}\n")
                continue  # Skip to the next sender if login fails

            for _ in range(number_of_emails_per_account):
                random_subject = random.choice(message_sentences)
                random.shuffle(message_sentences)
                message_body = ' '.join(message_sentences)

                subject_line = f"{random_subject} - {email_counter}"
                
                customized_message = f"""From: {sender_email}
To: {recipient_email}
Subject: {subject_line}

Hello {recipient_name}!

{message_body}

Warm regards,

{sender_alias}
"""
                server.sendmail(sender_email, recipient_email, customized_message.encode('utf-8'))
                print(f"{RED}Email {email_counter} from {sender_email} to {recipient_email} has been sent.\n{END}")
                time.sleep(delay)
                email_counter += 1

    except Exception as e:
        print(f"An error occurred: {e}\n")
        
    # Optional: Add animation here as well to indicate transition to next sender or completion.
    if len(senders_info[email_service]) > 1:
        print("Preparing next sender...\n")
        email_flying_animation(duration=1)  # Transition animation

print(f"{RED}Process completed.\n{END}")
