# timesheet_generator
Generates timesheet in an existing format of an excel file.

# Setup
Make sure pipenv is installed on your system
- cd into the directory that contains code for this project
- Run `pipenv sync`
- Run `./build.sh`
- You will have the executable in a newly created `dist` folder name `timesheet_generator` or `timesheet_generator.exe` depending on your platform

# Help
Run `timesheet_generator --help`

# Build
Run `./build.sh` on macOS or linux
Run `.\build.bat` on windows

# Sample Usage
`./timesheet_generator --name "Anirudh Singh Rathore" --month 2 year 2026 --leaves "2:PFL 3:PFL 4:PFL 5:PFL 6:PFL 10:PFL"`
