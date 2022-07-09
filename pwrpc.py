import os
import time
try:
    from pypresence import Presence  # pip install pypresence
    from InquirerPy import prompt # pip install InquirerPy
    from colorama import init, Fore # pip install colorama
except ImportError:
    os.system("pip install pypresence InquirerPy colorama")
    from pypresence import Presence
    from InquirerPy import prompt
    from colorama import init, Fore

init(autoreset=True)

clsr = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clsr()

CLIENT_ID = "987287937467170846"

def pp():
    clsr()
    print(f"""
    {Fore.RED}  _______          _______             
    {Fore.RED} |  __ \ \        / /  __ \            
    {Fore.YELLOW} | |__) \ \  /\  / /| |__) |_ __   ___ 
    {Fore.YELLOW} |  ___/ \ \/  \/ / |  _  /| '_ \ / __|
    {Fore.GREEN} | |      \  /\  /  | | \ \| |_) | (__ 
    {Fore.GREEN} |_|       \/  \/   |_|  \_\ .__/ \___|
    {Fore.GREEN}                           | |         
    {Fore.GREEN}                           |_|     

    {Fore.WHITE}----------------------------------------
        {Fore.RED}Developer: {Fore.BLUE}FireHead90544
        {Fore.RED}Discord: {Fore.BLUE}</Rudransh Joshi>#2022
        {Fore.RED}Client ID: {Fore.BLUE}{CLIENT_ID}
        {Fore.RED}Version: {Fore.BLUE}1.0.2
    {Fore.WHITE}----------------------------------------

    """)
pp()

stylesheet = {
    "questionmark": "#16C60C bold",
    "question": "#E74856 bold",
    "pointer": "#3A96DD",
    "answer": "#E5E512"
}

LOG_TIME = time.time()

def rpcData():
    pp()
    dataIn = [
        {
            "type": "input",
            "name": "batch",
            "message": "Which batch are you studying from: ",
            "validate": lambda res: len(res) > 0,
            "invalid_message": "Input Cannot be empty."
        },
        {
            "type": "list",
            "name": "subject",
            "message": "Select the subject you are studying: ",
            "choices": ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'Attempting Test']
        },
        {
            "type": "input",
            "name": "topic",
            "message": "What chapter/topic are you studying: ",
            "validate": lambda res: len(res) > 0,
            "invalid_message": "Input Cannot be empty."
        }
    ]
    data = prompt(dataIn, style=stylesheet)
    return data['batch'], "test" if data['subject'].startswith("At") else data['subject'].lower(), data['topic']

RPC = Presence(CLIENT_ID)
RPC.connect()

def update_presence():
    data = rpcData()
    try:
        RPC.clear()
    except Exception:
        RPC.connect() # This means that the connection already got disconnected, so attempt to start a new one
    RPC.update(
        state=data[2].title(),
        details=data[0].title(),
        start=LOG_TIME,
        large_image=data[1],
        large_text="Attempting Test" if data[1] == "test" else data[1].title(),
        small_image="pw",
        small_text="Physics Wallah!",
        buttons=[{"label": "Physics Wallah 💖", "url": "https://discord.gg/physicswallah"}, { "label": "PW Utils ⭐", "url": "https://github.com/FireHead90544/PWUtils"}]
    )
    print(f"{Fore.GREEN} >>> Updated Rich Presence :)")
    print(f"{Fore.CYAN} >>> Now just leave this window open (maybe just minimize it), you can update/close whenever you want by selecting the below options.")

while True:
    print("\n")
    data = prompt({"type": "list", "name": "dat", "message": "What do you want to do?", "choices": ["Update RPC", "Stop & Close"]}, style=stylesheet)
    if data['dat'] == "Update RPC":
        update_presence()
    else:
        try:
            RPC.close()
        except Exception:
            pass
        print(f"{Fore.GREEN} >>> Closed Rich Presence :)")
        break
