import datetime

class TimesheetDate:
  def __init__(self, date, month, year, attendance="P"):
    self.date = date
    self.month = month
    self.year = year
    self.day = datetime.date(year, month, date).strftime("%A")
    self.attendance_date = datetime.datetime(self.year, self.month, self.date)
    self.attendance = self.map_attendance(attendance, self.day)

  def map_attendance(self, attendance, day):
    if attendance:
      return attendance
    
    if day in ["Saturday", "Sunday"]:
      return "WO"

    return "P"
  
  def to_dict(self):
    return {
      "date": self.date,
      "month": self.month,
      "year": self.year,
      "day": self.day,
      "attendance_date": self.attendance_date,
      "attendance": self.attendance
    }

  def __repr__(self):
    return f"date={self.date} month={self.month} year={self.year} day={self.day} attendance_date={self.attendance_date} attendance={self.attendance}"
  
  def __str__(self):
    return f"date={self.date} month={self.month} year={self.year} day={self.day} attendance_date={self.attendance_date} attendance={self.attendance}"
