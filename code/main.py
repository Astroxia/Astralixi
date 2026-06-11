import commands
import astralixi_api
import time
import readline
import os
import signal

# Sets highest process priority when run as root for system performance optimization.

COMMAND_LIST = [
    'lf', 'mkf', 'rm', 'cp', 'mv', 'rn', 'prf', 'search',
    'ld', 'cd', 'pcwd', 'mkdir', 'rmdir', 'cpdir', 'mvdir', 'rndir',
    'ps', 'kill', 'df', 'mem', 'clear', 'history', 'whoami', 'username',
    'password', 'pyrun',
    'orbit', 'rocket', 'planets', 'launchsites', 'phases', 'timeinspace',
    'constellation',
    'aka', 'help',
]

# Completes commands based on input text in the terminal
def _completer(text, state):
    """Provides command autocomplete suggestions based on user input text."""
    # Finds commands matching input text prefix and returns next match for autocompletion.
    matches = [c for c in COMMAND_LIST if c.startswith(text)]
    return matches[state] if state < len(matches) else None

# Binds tab key to use autocomplete function for command line completion feature.
readline.set_completer(_completer)
readline.parse_and_bind('tab: complete')

# Credentials.txt stores user credentials on disk for system bootstrap and access.
CREDENTIALS_FILE = "credentials.txt"

# Checks if credentials.txt has the user's credentials
def credentials_are_set():
    """Check if credentials file contains non-empty username and password entries."""
    # Checks credentials file for non-empty username and password stored on disk.
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
    # Authenticates user by reading credentials from file and comparing with input.
    print("-- Login --")
    attempts = 3
    while attempts > 0:
        # Reads credentials file for stored username and password comparison operations.
        try:
            with open(CREDENTIALS_FILE, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: '{CREDENTIALS_FILE}' not found.")
            raise SystemExit(1)
        # Stores username password in variables for comparison with user input now.
        stored_username = ""
        stored_password = ""
        # Separates credential labels from actual values in credentials file parsing.
        for line in lines:
            if line.startswith("Username:"):
                stored_username = line.split(":", 1)[1].strip()
            elif line.startswith("Password:"):
                stored_password = line.split(":", 1)[1].strip()

        username_input = input("Username: ").strip()
        password_input = input("Password: ").strip()
        
        # Checks if credentials entered by user match stored credentials in system.
        if username_input == stored_username and password_input == stored_password:
            print(f"Welcome, {stored_username}!\n")
            # Seeds in-RAM credentials so whoami username password commands work correctly.
            commands._credentials["username"] = stored_username
            commands._credentials["password"] = stored_password
            return
        # Decreases user's remaining login attempts counter and shows status message.
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect credentials. {attempts} attempt(s) remaining.\n")
            else:
                print("Too many failed attempts. Exiting.")
                raise SystemExit(1)

# Clears terminal display before showing welcome banner to user on startup screen.
commands.clear_terminal()

# Displays Astralixi ASCII art banner and system welcome message to user startup.
print(r"""
    _   ___ _____ ___    _   _    _____  _____ 
   /_\ / __|_   _| _ \  /_\ | |  |_ _\ \/ /_ _|
  / _ \\__ \ | | |   / / _ \| |__ | | >  < | | 
 /_/ \_\___/ |_| |_|_\/_/ \_\____|___/_/\_\___| 
""")

# Checks if credentials exist and runs login procedure if credentials file found.
if credentials_are_set():
    login()

# Infinite loop prompts user for commands and executes them in system shell.
while True:
    try:
        # Prompts user for input command and stores it for processing and execution.
        command = input("> ")
        # Stores command history log length before executing new command for tracking.
        prev_len = len(commands.command_history_log)
        # Executes command provided by user through command parsing and dispatching system.
        commands.execute_command(command)
        # Checks if command history increased and adds command to readline history buffer.
        if len(commands.command_history_log) > prev_len:
            readline.add_history(command)
            # Removes oldest history item if history length exceeds limit of items.
            if readline.get_current_history_length() > 25:
                readline.remove_history_item(0)
        # Adds delay to prevent excessive CPU usage from tight loop iterations.
        time.sleep(0.1)
    # Catches keyboard interrupt and prevents user from exiting via control+c key.
    except KeyboardInterrupt:
        print("\nDo not use Ctrl+C to exit Astralixi!")
    # Catches all other exceptions and silently continues program execution flow.
    except Exception as e:
        # Silently passes on any unhandled exceptions to maintain program stability.
        pass