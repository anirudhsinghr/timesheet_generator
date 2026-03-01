from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

class AttendanceCellStyleGenerator:
  def __init__(self, attendance):
    self.attendance = attendance
    self.attendance_colors = {
      "P": "92D050",
      "UHL": "FF0000",
      "UFL": "8EAADB",
      "ML": "548135",
      "CL": "FFD965",
      "CHO": "FFFF00",
      "COFF": "757070",
      "WFH": "F4B083",
      "PFL": "C5E0B3",
      "PHL": "00B0F0",
      "HO": "FF33CC",
      "WO": "00FF00"
    }
  
  def generate_styles(self):    
    thin_side = Side(border_style="thin", color="000000")
    all_borders = Border(top=thin_side, bottom=thin_side, left=thin_side, right=thin_side)
    color = self.attendance_colors[self.attendance] if self.attendance in self.attendance_colors else "FFFFFF"

    return {
      "value": self.attendance,
      "fill": PatternFill(start_color=color, fill_type="solid"),
      "alignment": Alignment(horizontal='center', vertical='bottom'),
      "border": all_borders,
      "font": Font(
        name='Cambria',
        size=11,
        bold=True,
        italic=True,
        color="000000"
      )
    }