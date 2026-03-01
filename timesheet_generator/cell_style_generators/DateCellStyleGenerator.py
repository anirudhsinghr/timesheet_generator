from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

class DateCellStyleGenerator:
  def __init__(self, date):
    self.date = date
  
  def generate_styles(self):    
    thin_side = Side(border_style="thin", color="000000")
    all_borders = Border(top=thin_side, bottom=thin_side, left=thin_side, right=thin_side)

    return {
      "value": self.date,
      "fill": PatternFill(start_color="FFFFFF", fill_type="solid"),
      "alignment": Alignment(horizontal='center', vertical='center'),
      "number_format": "d-mmm-yy",
      "border": all_borders,
      "font": Font(
        name='Calibri',
        size=11,
        bold=False,
        italic=False,
        color="000000"
      )
    }