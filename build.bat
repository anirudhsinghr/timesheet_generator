SET SPEC_FILE=timesheet_generator.spec

IF EXIST %SPEC_FILE% (
  pipenv run pyinstaller %SPEC_FILE%
) else (
  pipenv run pyinstaller --onefile --console --add-data "timesheet_template.xlsx:." --name "timesheet_generator" --clean main.py
)