import commands
import astralixi_api
import time
import readline
import os
import signal
import sys

try:
    os.nice(-20)
except PermissionError:
    pass

COMMAND_LIST = [
    'lf', 'wc', 'mkf', 'rm', 'cp', 'mv', 'rn', 'prf', 'search',
    'ld', 'cd', 'pcwd', 'mkdir', 'rmdir', 'cpdir', 'mvdir', 'rndir',
    'ps', 'kill', 'df', 'mem', 'clear', 'history', 'whoami', 'username',
    'password', 'pyrun', 'uptime', 'reboot', 'shutdown', 'hibernate', 'cpuinfo',
    'orbit', 'rocket', 'planets', 'launchsites', 'phases', 'timeinspace',
    'constellation', 'trackiss', 'sunit',
    'aka', 'help', 'axrun', 'hello', 'beacon', 'calc', 'rng',
]

def _completer(text, state):
    """Provides command autocomplete suggestions based on user input text."""
    matches = [c for c in COMMAND_LIST if c.startswith(text)]
    return matches[state] if state < len(matches) else None

readline.set_completer(_completer)
readline.parse_and_bind('tab: complete')

CREDENTIALS_FILE = "credentials.txt"

def credentials_are_set():
    """Check if credentials file contains non-empty username and password entries."""
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                if line.startswith("Username:"):
                    value = line.split(":", 1)[1].strip()
                    if value:
                        return True
                if line.startswith("Password:"):
                    value = line.split(":", 1)[1].strip()
                    if value:
                        return True
    except FileNotFoundError:
        pass
    return False

def login():
    """Prompt user to log in with username and password from credentials file."""
    print("-- Login --")
    attempts = 3
    while attempts > 0:
        try:
            with open(CREDENTIALS_FILE, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: '{CREDENTIALS_FILE}' not found.")
            raise SystemExit(1)

        stored_username = ""
        stored_password = ""
        for line in lines:
            if line.startswith("Username:"):
                stored_username = line.split(":", 1)[1].strip()
            elif line.startswith("Password:"):
                stored_password = line.split(":", 1)[1].strip()

        username_input = input("Username: ").strip()
        password_input = input("Password: ").strip()

        if username_input == stored_username and password_input == stored_password:
            print(f"Welcome, {stored_username}!\n")
            commands._credentials["username"] = stored_username
            commands._credentials["password"] = stored_password
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect credentials. {attempts} attempt(s) remaining.\n")
            else:
                print("Too many failed attempts. Exiting.")
                raise SystemExit(1)

commands.clear_terminal()

print(r"""
    _   ___ _____ ___    _   _    _____  _____ 
   /_\ / __|_   _| _ \  /_\ | |  |_ _\ \/ /_ _|
  / _ \\__ \ | | |   / / _ \| |__ | | >  < | | 
 /_/ \_\___/ |_| |_|_\/_/ \_\____|___/_/\_\___| 
""")

if credentials_are_set():
    login()

while True:
    try:
        command = input("> ")
        prev_len = len(commands.command_history_log)
        commands.execute_command(command)
        if len(commands.command_history_log) > prev_len:
            readline.add_history(command)
            if readline.get_current_history_length() > 25:
                readline.remove_history_item(0)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDo not use Ctrl+C to exit Astralixi!")
    except Exception as e:
        pass
