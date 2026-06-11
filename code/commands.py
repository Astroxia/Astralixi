import os
import sys
import signal
import subprocess
import shutil
import math
import psutil
import platform
import random
import urllib.request


# ── State ────────────────────────────────────────────────────────────

# Tracks successfully run commands and stores command shortcuts and credentials.

command_history_log = []   # Tracks every successfully run command
_shortcuts         = {}    # Stores aka aliases: { shortcut: full_command }

# Credentials are stored in RAM only - they are NOT persisted to disk.
# Populated at startup by main.py reading credentials.txt (legacy bootstrap),
# or left empty if no credentials file exists.
_credentials = {
    "username": "",
    "password": "",
}

_RAM_WARNING = (
    "[!] This change is saved in RAM only and will be lost on shutdown or reboot.\n"
    "[i] Permanent credential storage is coming in a future version of Astralixi OS."
)

def _print_ram_warning():
    """Print the RAM-storage warning whenever a credential is changed."""
    # Outputs warning message about credentials being stored only in RAM memory.

# ── Command dispatcher ────────────────────────────────────────────────────────

def execute_command(command):
    """Parse and dispatch a command string to its handler function."""
    # Parses user command string and dispatches to appropriate handler function.
    parts = command.split()
    if not parts:
        return
    cmd, *args = parts

    COMMANDS = {
        # Files
        'lf':     list_files,
        'wc':     file_stats,
        'mkf':    create_file,
        'rm':     remove_file,
        'cp':     copy_file,
        'mv':     move_file,
        'rn':     rename_file,
        'prf':    print_file,
        'search': search_for_file,
        # Directories
        'ld':     list_directories,
        'cd':     change_directory,
        'pcwd':   print_current_directory,
        'mkdir':  make_folder,
        'rmdir':  remove_folder,
        'cpdir':  copy_folder,
        'mvdir':  move_folder,
        'rndir':  rename_folder,
        # System
        'ps':        processes_running,
        'kill':      kill_process,
        'df':        disk_free,
        'mem':       memory_used,
        'clear':     clear_terminal,
        'history':   command_history,
        'whoami':    who_am_i,
        'username':  change_username,
        'password':  change_password,
        'uptime':    uptime, 
        'reboot':    reboot, 
        'shutdown':  shutdown, 
        'hibernate': hibernate,  
        # Space
        'orbit':         orbital_speed,
        'rocket':        rocket_equation,
        'planets':       planet_reference,
        'launchsites':   launch_sites,
        'phases':        moon_phases,
        'timeinspace':   time_in_space,
        'constellation': constellation_reference,
        'trackiss':      track_iss,
        'sunit':         space_unit_convert, 
        # Hardware
        'cpuinfo':      cpu_info,
        # Misc
        'aka':         shortcut_to_long_command,
        'help':        help_manual,
        'axrun':       app_run,
        'hello':       hello,
        'pyrun':       pyrun,
        # 'clip':        clip, # not implemented (copies cmd's output to clipboard)
        'beacon':      ping_website, 
        'calc':        calculator,
        'rng':         random_number, 
    }

    if cmd in COMMANDS:
        try:
            COMMANDS[cmd](*args)
            command_history_log.append(command)
        except TypeError as e:
            print(f"Error: Wrong number of arguments for '{cmd}'. {e}")
        except Exception as e:
            print(f"Error running '{cmd}': {e}")
    else:
        print(f"Command '{cmd}' not found. Type 'help' for a list of commands.")


# ════════════════════════════════════════════════════════════════
#  FILE COMMANDS
# ════════════════════════════════════════════════════════════════

def list_files():
    """List only files (not directories) in the current directory."""
    # Lists only regular files in the current working directory for user inspection.

def file_stats(file_path):
    """Display character, word, and line counts for a file."""
    # Analyzes file and displays character frequency, word count, and line statistics.

def create_file(name):
    """Create a new empty file."""
    # Creates a new empty file with the specified name in current directory now.

def remove_file(path):
    """Delete a file (not a directory — use rmdir for that)."""
    # Removes specified file from filesystem after confirming it is not directory.

def copy_file(source, destination):
    """Copy a file to a new location."""
    # Copies file from source path to destination maintaining original content exactly.

def move_file(source, destination):
    """Move a file to a new location."""
    # Relocates file from source to destination path in filesystem preserving content.

def rename_file(old_name, new_name):
    """Rename a file."""
    # Renames file from old name to new name in current directory location today.

def print_file(name):
    """Print the full contents of a file to the terminal."""
    # Reads and displays entire file contents to terminal for user viewing purposes.

def search_for_file(search_term):
    """Search for files (not directories) whose names contain the given term."""
    # Searches current directory for files matching search term in filename substring.


# ════════════════════════════════════════════════════════════════
#  DIRECTORY COMMANDS
# ════════════════════════════════════════════════════════════════

def list_directories():
    """List only directories (not files) in the current directory."""
    # Lists only directories excluding regular files in current working directory now.

def change_directory(new_directory):
    """Change the current working directory."""
    # Changes current working directory to specified path in filesystem structure.

def print_current_directory():
    """Print the current working directory path."""
    # Displays absolute path of current working directory to user on terminal.

def make_folder(path):
    """Create a new directory."""
    # Creates new directory with specified name in current working directory location.

def remove_folder(path):
    """Remove a directory and all its contents."""
    # Removes directory and all its contents recursively from filesystem structure.

def copy_folder(source, destination):
    """Recursively copy a directory and all its contents."""
    # Copies entire directory tree from source to destination preserving structure.

def move_folder(source, destination):
    """Move a directory to a new location."""
    # Moves directory from source path to destination preserving all contents inside.

def rename_folder(old_name, new_name):
    """Rename a directory."""
    # Renames directory from old name to new name in filesystem structure today.


# ════════════════════════════════════════════════════════════════
#  SYSTEM COMMANDS
# ════════════════════════════════════════════════════════════════

def uptime():
    """Display system uptime in seconds, minutes, or hours."""
    # Calculates and displays system uptime in appropriate human-readable time unit.

def processes_running():
    """List all running processes with their PID and name."""
    # Displays list of all running processes with process ID and process names.

def kill_process(selected_pid):
    """Kill a process by its PID."""
    # Terminates specified process using process ID after user confirmation requested.

def clear_terminal():
    """Clear the terminal screen using a direct ANSI escape sequence."""
    # Clears terminal screen using ANSI escape codes compatible with various terminals.

def command_history():
    """Print the last 25 commands that were run."""
    # Displays the last twenty five commands executed by user in current session.

def disk_free():
    """Show total, used, and free disk space for the current drive."""
    # Displays disk space statistics including total used and remaining free space.

def memory_used():
    """Show current RAM usage (total, used, available, and percent)."""
    # Shows RAM memory statistics including total used available and percentage usage.

def shutdown():
    """Shut down the computer after user confirmation."""
    # Prompts user to confirm shutdown then executes system shutdown command now.

def reboot():
    """Reboot the computer after user confirmation."""
    # Prompts user for confirmation then executes system reboot command if approved.

def hibernate():
    """Hibernate the computer after user confirmation."""
    # Prompts user to confirm hibernation then executes system hibernation command.


# ════════════════════════════════════════════════════════════════
#  HARDWARE-RELATED COMMANDS
# ════════════════════════════════════════════════════════════════

def cpu_info():
    """Display CPU information including core count and architecture details."""
    # Shows CPU core count processor name machine type and architecture information.


# ════════════════════════════════════════════════════════════════
#  ACCOUNT COMMANDS
# ════════════════════════════════════════════════════════════════

def who_am_i():
    """Print the current username stored in RAM."""
    # Displays currently logged in username stored in system memory for verification.

def change_username():
    """Update the stored username after verifying the current one."""
    # Allows user to change stored username after entering and verifying old password.

def change_password():
    """Update the stored password after verifying the current one."""
    # Allows user to change stored password after verification with old password first.


# ════════════════════════════════════════════════════════════════
#  SPACE COMMANDS
# ════════════════════════════════════════════════════════════════

def space_unit_convert(value, unit, converted_unit):
    """Convert between space distance units: AU, Light-Years (LY), and kilometers (KM)."""
    # Converts between astronomical units light years and kilometers for space calculations.

def orbital_speed(planet):
    """Show orbital speed, period, and distance for Earth (around Sun) or Moon (around Earth)."""
    # Displays orbital speed period and distance data for specified planetary body.

def rocket_equation(isp, m0, mf):
    """Calculate delta-v using the Tsiolkovsky rocket equation."""
    # Calculates delta-v velocity change using rocket equation with mass and impulse.

def planet_reference():
    """Print a quick-reference table of key data for all eight solar system planets."""
    # Shows reference table with key data for all eight planets in solar system.

def launch_sites():
    """Print a reference list of major rocket launch sites around the world."""
    # Displays reference list of major global rocket launch sites with coordinates.

def moon_phases():
    """Show the approximate current moon phase based on a known reference new moon."""
    # Calculates and displays current moon phase illumination percentage and cycle days.

def time_in_space(start_date, end_date):
    """Calculate the duration between two dates (e.g. a mission window)."""
    # Calculates duration between two dates showing days weeks months and years elapsed.

def constellation_reference():
    """Print a reference list of notable constellations and their brightest star."""
    # Displays notable constellations with brightest stars and interesting astronomical facts.

def track_iss():
    """Fetch and display current ISS position data from online tracking API."""
    # Retrieves and displays current International Space Station latitude longitude altitude.


# ════════════════════════════════════════════════════════════════
#  MISC COMMANDS
# ════════════════════════════════════════════════════════════════

def hello():
    """Greet the user with a friendly hello message."""
    # Outputs friendly greeting message to user on terminal screen.

def ping_website(url):
    """Test if a website is reachable by performing an HTTP GET request."""
    # Tests website connectivity by attempting HTTP request and showing response code.

def calculator(equation):
    """Perform basic binary arithmetic operations (addition subtraction multiplication etc)."""
    # Evaluates binary arithmetic expression and displays calculated result to user.

def random_number(num_range):
    """Generate a random integer within a specified range."""
    # Generates and displays random integer between two specified number values.

def pyrun(script_path):
    """Run a Python script file using the Python interpreter."""
    # Executes Python script file from specified path using system Python interpreter.

def shortcut_to_long_command(shortcut, *cmd_parts):
    """Create a shortcut alias for a longer command."""
    # Creates command alias allowing shortcut to execute specified longer command.

def app_run(appName):
    """Runs an app in-process so it can access astralixios_api."""
    # Loads and executes Astralixi app with full access to astralixi_api functions.

def help_manual():
    """Print basic available commands and their usage."""
    # Displays comprehensive help documentation listing all commands and usage instructions.