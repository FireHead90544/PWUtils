# PWRpc - Manually Operated Rich Presence Client for Discord
# Developed By </Rudransh Joshi>
# Haven't took care of checks/validations for url, and a bit hardcoded (because I technically made it for myself)
# Since some non-tech people are also gonna use it, wrong inputs will cause the program to crash, so better not play with it.
# Follow the instructions as shown xD
# Contributions are welcome, please always provide the source if someone asks for, thank you :)

import time
import base64
try:
    from pypresence import Presence
except ImportError:
    import os
    os.system('pip install pypresence')
    os.system('cls' if os.name == 'nt' else 'clear')


print("""
  _______          _______             
 |  __ \ \        / /  __ \            
 | |__) \ \  /\  / /| |__) |_ __   ___ 
 |  ___/ \ \/  \/ / |  _  /| '_ \ / __|
 | |      \  /\  /  | | \ \| |_) | (__ 
 |_|       \/  \/   |_|  \_\ .__/ \___|
                           | |         
                           |_|     

    Developer: </Rudransh Joshi>
""")


CLIENT_ID = "987287937467170846" # <-- Your CLIENT_ID "Go to developer portal, create your application, go to oauth2 tab and grab it"

# You also need to go to the rich presence tab and upload your assets and use their names as keys in the application
# Otherwise just let my client_id handle everything :)

# Not so highly intellectual stuffs
# but your pathetic brain might not
# be able to handle it, so probably
# just go with the flow :)

state = input("\n\nState: ")
details = input("\nBatch: ")
t = int(input("\nTime Type [1. Definite, 2. Indefinite]: "))
if t == 2:
    start = time.time()
    print("\nEnter 0 in both inputs if you just started studying.\nOr enter how many hours/minutes before you started studying.")
    start = start - int(input("Hours: ")) * 3600 - int(input("Minutes: ")) * 60
    end = None
else:
    start = time.time()
    print("\nEnter how many hours/minutes will you study for.")
    end = start + int(input("Hours: ")) * 3600 + int(input("Minutes: ")) * 60

print("\nAvailable keys to use: 'pw', 'physics', 'chemistry', 'mathematics', 'biology', 'test' <-- Only valid values of inputs for Logo, Subject\n")
image = input("\nLogo (Large Image): ").lower() or "pw"
text = str(input("\nText (Text which will be shown upon hovering the Large Image): ") or "Physics Wallah!") + base64.b64decode(b'IHx8IERldmVsb3BlZCBCeTogPC9SdWRyYW5zaCBKb3NoaT4jMjAyMg==').decode("utf-8")
subject = input("\nSubject (Small Image): ")

print("\nButtons [Leave all inputs empty for no buttons]: ")

buttons = []
for i in range(2):
    lbl = input(f"\nEnter Button #{i+1}'s Text: ")
    url = input(f"Enter Button #{i+1}'s URL: ")
    if lbl and url:
        buttons.append({"label": lbl, "url": url})
if not buttons:
    buttons = None


RPC = Presence(CLIENT_ID)
RPC.connect()

RPC.update(
    state=state, 
    details=details, 
    start= start, 
    end=end, 
    large_image=image, 
    large_text=text, 
    small_image=subject.lower(), 
    small_text=subject.capitalize(), 
    buttons=buttons)


while True:
    print("RPC Updated!")
    time.sleep(3600)
