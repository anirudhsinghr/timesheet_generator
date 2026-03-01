import calendar

from . import ExcelTimesheetRenderer
from . import TimesheetDataGenerator

class TimesheetGenerator:
  def __init__(self, employee_name, month, year, leaves):
    self.employee_name = employee_name
    self.month = month
    self.year = year
    self.leaves = leaves

  def generate(self):
    month_name = calendar.month_name[self.month]
    sheet_name = f"{month_name}_{self.year}"
    file_name = f"{self.employee_name}_{month_name}_{self.year}_timesheet.xlsx"
    
    timesheet_data = TimesheetDataGenerator(
      self.employee_name, 
      self.month, 
      self.year, 
      self.leaves
    ).generate_timesheet_data()

    ExcelTimesheetRenderer(
      self.employee_name,
      month_name,
      sheet_name,
      timesheet_data
    ).render(file_name)
    
    print(f"Timesheet written to file - {file_name}")
