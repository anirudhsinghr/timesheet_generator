import calendar
from .TimesheetDate import TimesheetDate

class TimesheetDataGenerator:
  def __init__(self, name, month, year, leaves):
    self.name = name
    self.month = month
    self.year = year
    self.leaves = self.parse_leaves(leaves)

  def generate_timesheet_data(self):
    number_of_days = calendar.monthrange(self.year, self.month)[1]
    dates = list(range(1, number_of_days + 1))
    return [
      TimesheetDate(
        date,
        self.month,
        self.year,
        self.attendance_for_date(date)
      ).to_dict() for date in dates
    ]
  
  def attendance_for_date(self, date):
    if date in self.leaves:
      return self.leaves[date]
    else:
      return None

  def parse_leaves(self, leaves):
    if not leaves:
      return {}
    
    list_of_leaves = list(map(lambda leave: leave.split(":"), leaves.split(" ")))

    if (len(list_of_leaves) == 0):
      return {}

    return { int(leave[0]): leave[1] for leave in list_of_leaves }