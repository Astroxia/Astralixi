*These docs were written 100% by humans.*
### Introduction
You came to this documentation, which means you probably know what Astralixi is. But if you don't, Astralixi is a space-enthusiast focused User Interface which acts like an Operating System, made for ARM devices. It is written 100% in python standard library. This documentation will teach you how to use Astralixi, while being a great point of reference in the future. Let’s begin!

### Installation & Setup
To install Astralixi, you first have to head to the github repositry: https://github.com/Astroxia/Astralixi. At the repository, head to the releases section, and look for the latest release. Once the latest release is found, download respective files. Place the .axapp files in the ~/.axapp directory. Place the .axapp.bz2 files at ~/Astralixi/axappPackages/, these are your optionally Installable axapps for the future. Finally, place the astralixi binary in your home directory (~/) and run the binary. You are now in the Astralixi environment!

### Basic Usage
With the tools that Astralixi has to offer, you can absolutely become a power user, but to do that, you have to set a basic foundation. You need to learn 32 of the most basic commands, to be able to utilise Astralixi accordingly. The following is a table of the 32 basic commands (there are many more total commands, but not included in this documentation), along with usage notes.

| **Command**              | **Usage Notes**                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| lf                       | List Files. Will list only files, and not directories in your current working directory. |
| ld                       | List Directories. Will list only directories in your current working directory.          |
| pcwd                     | Print Current Working Directory.                                                         |
| cd [directory]           | Change Directory. Change your current working directory.                                 |
| mkf [file name]          | Make File. Creates a file with given name in current working directory.                  |
| rm [file name]           | Remove File. Deletes a file with given name, if exists, in current working directory.    |
| prf [file name]          | Print File. Prints the contents of the given file onto the terminal.                     |
| search [terms]           | Search File. Looks in current working directory for a file, that matches search terms.   |
| mkdir [directory name]   | Make Directory. Creates a folder with given name in working directory.                   |
| rmdir [Directory name]   | Remove Directory. Deletes a folder, if exists, in current working directory.             |
| df                       | Disk Free. Informs you of how much of your storage is used and free.                     |
| mem                      | Memory Statistics.                                                                       |
| clear                    | Clear Terminal.                                                                          |
| history                  | Command History. Prints the history of the last 25 used commands to the terminal.        |
| uptime                   | System Uptime. How long your system has been on.                                         |
| shutdown                 | Shutdown computer.                                                                       |
| pwr                      | Battery Percentage.                                                                      |
| exit                     | Force Exit Astralixi. Use only if system has errors.                                     |
| planets                  | Planets reference. List of planets with basic information.                               |
| launchsites              | Popular launchsites. List of launchsites across the globe with basic info.               |
| crew                     | Random astronaut profile.                                                                |
| constellation            | Constellation reference list.                                                            |
| lunarcrater              | List of popular moon craters.                                                            |
| quote                    | Random quote from space-industry related person.                                         |
| help                     | Prints a help manual, for basic commands.                                                |
| axrun [app name]         | Runs an axapp (astralixi app).                                                           |
| pyrun [file]             | Runs a python file in current working directory.                                         |
| chatbot                  | Run a basic chatbot integrated into Astralixi.                                           |
| calc                     | Basic maths calculator tool.                                                             |
| mv [origin, destination] | Move given file, from one place to another.                                              |
| cp [origin, destination] | Copies a file, from one place to another.                                                |
| clip [command]           | Copies command output to clipboard (doesn't work on all systems)                         |
These basic usage commands aren't enough to daily drive Astralixi, but they will get you started with this amazing user interface.

### Axapp Usage
First, check installation instructions for where to place your pre-installed axapps, and where to place your axapp packages.
Axapps are applications built specifically for Astralixi, using the custom api. The api lets developers design TUI-style apps for you to use.
Let's learn how to run, install, exit, uninstall and use axapps!
To run the pre-installed axapps, is the easiest of what you can do. All you have to do is run the ```axrun [appName]``` command to run any app from the available pre-installed axapps.
To install an axapp from the installable catalogue, you have to run ```axinstall [appName]```, pretty simple right?
To exit an axapp, the instructions are usually given in the bottom help bar, but by default 'Q' is used to exit.
Uninstalling an axapp is just like installing one, ```axuninstall [appName]```, but you can Uninstall only from your installed, non-default apps.
Using axapps is very simple, but the api can be very extensible for developers. This is how the app architecture was made, so it is easy, while being powerful.

### Contact Help/Feedback
If you ever feel stuck, or have some constructive feedback to do with Astralixi or any Astroxia-related thing, you can reach out! The easiest and most preffered method, is to message (@astr0x) on Cyberspace, but you can also email (4astrox@gmail.com) alternatively.

### Conclusion
I hope this documentation is of some help to you. Make sure to recap on sections before reaching out when help is needed, to reduce the load on our end. Thanks for reading, in the meantime check out my cyberspace account (@astr0x) and our YouTube channel (@astroxia). Thanks!

*This documentation is a product of Astroxia, and was 100% written by humans.*
