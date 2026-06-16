import os
import sys
import signal
import subprocess
import shutil
import math
import psutil
import platform
import random
import time
import urllib.request
import datetime
import tkinter as tk
import json
import tempfile
import string
import secrets
from collections import Counter


# ── State ──────────────────────────────────────────────────────────────────────

command_history_log = []   # Tracks every successfully run command
_shortcuts         = {}    # Stores aka aliases: { shortcut: full_command }
_clipboard_text    = ""    # Used by the clip command as a custom clipboard

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

time_string ="1200"
date = "01012000"

def _print_ram_warning():
    """Print the RAM-storage warning whenever a credential is changed."""
    print(_RAM_WARNING)

def set_clipboard_text(text):
    """Store text for Ctrl+V pasting."""
    global _clipboard_text
    _clipboard_text = text if text is not None else ""

def get_clipboard_text():
    """Return the stored clipboard text."""
    return _clipboard_text


# ── Command dispatcher ─────────────────────────────────────────────────────────

def execute_command(command):
    """Parse and dispatch a command string to its handler function."""
    parts = command.split()
    if not parts:
        return
    cmd, *args = parts

    COMMANDS = {
        # Files
        'lf':     list_files,
        'lfh':    list_hidden_files, 
        'wc':     file_stats,
        'mkf':    create_file,
        'rm':     remove_file,
        'cp':     copy_file,
        'mv':     move_file,
        'rn':     rename_file,
        'prf':    print_file,
        'search': search_for_file,
        'peek':   peek_file_content,

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
        'cpuinfo':   cpu_info,
        'wifi':      wifi_tools, 
        'time':      time_tools,
        'date':      date_tools,
        'pwr':       battery_percentage,

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
        'lunarcrater':   moon_craters, 
        'telemetry':     fake_telemetry_sim,
        'sol':           earthday_marssol,
        'gravweigh':     weight_calculator,
        'crew':          random_crew_profiles,
        'quote':         random_space_quote,
        'captain-log':   journal_writing,

        # Misc
        'aka':       shortcut_to_long_command,
        'help':      help_manual,
        'axrun':     app_run,
        'hello':     hello,
        'pyrun':     pyrun,
        'tally':     tally_tool,
        'countdown': countdown_clock,
        'clip':      clip, 
        'genpass':   random_password_gen,
        'beacon':    ping_website,
        'calc':      calculator,
        'rng':       random_number,
        'dice':      dice_roller,
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


# ══════════��═══════════════════════════════════════════════════════════════════
#  FILE COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def list_files():
    """List only files (not directories) in the current directory."""
    pass

def list_hidden_files():
    """List only hidden files in the current directory."""
    pass

def file_stats(file_path):
    """Display character, word, and line counts for a file."""
    pass

def create_file(name):
    """Create a new empty file."""
    pass

def remove_file(path):
    """Delete a file (not a directory — use rmdir for that)."""
    pass

def copy_file(source, destination):
    """Copy a file to a new location."""
    pass

def move_file(source, destination):
    """Move a file to a new location."""
    pass

def rename_file(old_name, new_name):
    """Rename a file."""
    pass

def print_file(name):
    """Print the full contents of a file to the terminal."""
    pass

def peek_file_content(name):
    """Print the first 5 and last 5 lines of a file."""
    pass

def search_for_file(search_term):
    """Search for files (not directories) whose names contain the given term."""
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  DIRECTORY COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def list_directories():
    """List only directories (not files) in the current directory."""
    pass

def change_directory(new_directory):
    """Change the current working directory."""
    pass

def print_current_directory():
    """Print the current working directory path."""
    pass

def make_folder(path):
    """Create a new directory."""
    pass

def remove_folder(path):
    """Remove a directory and all its contents."""
    pass

def copy_folder(source, destination):
    """Recursively copy a directory and all its contents."""
    pass

def move_folder(source, destination):
    """Move a directory to a new location."""
    pass

def rename_folder(old_name, new_name):
    """Rename a directory."""
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  SYSTEM COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def uptime():
    """Display system uptime in seconds, minutes, or hours."""
    pass

def processes_running():
    """List all running processes with their PID and name."""
    pass

def kill_process(selected_pid):
    """Kill a process by its PID."""
    pass

def clear_terminal():
    """Clear the terminal screen using a direct ANSI escape sequence."""
    print("\033[2J\033[H", end="", flush=True)

def command_history():
    """Print the last 25 commands that were run."""
    pass

def disk_free():
    """Show total, used, and free disk space for the current drive."""
    pass

def memory_used():
    """Show current RAM usage (total, used, available, and percent)."""
    pass

def shutdown():
    """Shut down the computer after user confirmation."""
    pass

def reboot():
    """Reboot the computer after user confirmation."""
    pass

def hibernate():
    """Hibernate the computer after user confirmation."""
    pass

def wifi_tools(action):
    """Wi-Fi helper command with connect, disconnect, scan, enable, disable actions."""
    pass

def time_tools(action):
    """Manages system time with set and display actions for user tracking."""
    pass

def date_tools(action):
    """Manages system date with set and display actions for user tracking."""
    pass

def battery_percentage():
    """Display current battery percentage from system power supply."""
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  HARDWARE-RELATED COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def cpu_info():
    """Display CPU information including core count and architecture details."""
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  ACCOUNT COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def who_am_i():
    """Print the current username stored in RAM."""
    pass

def change_username():
    """Update the stored username after verifying the current one."""
    pass

def change_password():
    """Update the stored password after verifying the current one."""
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  SPACE COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def space_unit_convert(value, unit, converted_unit):
    """Convert between space distance units: AU, Light-Years (LY), and kilometers (KM)."""
    pass

def orbital_speed(planet):
    """Show orbital speed, period, and distance for Earth (around Sun) or Moon (around Earth)."""
    pass

def rocket_equation(isp, m0, mf):
    """Calculate delta-v using the Tsiolkovsky rocket equation."""
    pass

def planet_reference():
    """Print a quick-reference table of key data for all eight solar system planets."""
    pass

def launch_sites():
    """Print a reference list of major rocket launch sites around the world."""
    pass

def moon_phases():
    """Show the approximate current moon phase based on a known reference new moon."""
    pass

def time_in_space(start_date, end_date):
    """Calculate the duration between two dates (e.g. a mission window)."""
    pass

def constellation_reference():
    """Print a reference list of notable constellations and their brightest star."""
    pass

def track_iss():
    """Fetch and display current ISS position data from online tracking API."""
    pass

def moon_craters():
    """Print popular moon craters with locations and descriptions in a table."""
    pass

def fake_telemetry_sim():
    """Simulates rocket launch telemetry with countdown and exponential altitude calculations."""
    pass

def earthday_marssol(numOfEarthDays):
    """Converts Earth days to Mars sols using conversion factor for mission planning."""
    pass

def weight_calculator(mass, body):
    """Calculates object weight on specified celestial body given mass in kilograms."""
    pass

def random_crew_profiles():
    """Display a random astronaut or cosmonaut profile with biographical information."""
    pass

def random_space_quote():
    """Display a random inspirational quote related to space exploration and discovery."""
    pass

def journal_writing(note):
    """Write captain's log entry to file with word limit enforced for mission logs."""
    pass


# ══════════════════════════════════════════════════════════════════════════════
#  MISC COMMANDS
# ══════════════════════════════════════════════════════════════════════════════

def hello():
    """Greet the user with a friendly hello message."""
    pass

def ping_website(url):
    """Test if a website is reachable by performing an HTTP GET request."""
    pass

def calculator(equation):
    """Perform basic binary arithmetic operations (addition subtraction multiplication etc)."""
    pass

def random_number(num_range):
    """Generate a random integer within a specified range."""
    pass

def pyrun(script_path):
    """Run a Python script file using the Python interpreter."""
    pass

def shortcut_to_long_command(shortcut, *cmd_parts):
    """Create a shortcut alias for a longer command."""
    pass

def app_run(appName):
    """Runs an app in-process so it can access astralixios_api."""
    pass

def clip(command_name, *args):
    """Capture the output of a command and store it for Ctrl+V paste."""
    pass

def countdown_clock(seconds):
    """Count down from specified seconds to zero with real-time display updates."""
    pass

def tally_tool():
    """Interactive tally counter incremented by enter key and exited with q."""
    pass

def random_password_gen(length):
    """Generate secure random password and append to AstralixiLocker file."""
    pass

def dice_roller(sides, dice):
    """Roll specified number of dice with given sides and display individual results."""
    pass

def help_manual():
    """Print basic available commands and their usage."""
    pass
