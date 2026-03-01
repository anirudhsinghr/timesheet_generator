from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

class DayCellStyleGenerator:
  def __init__(self, day):
    self.day = day

  def is_weekend(self):
    return self.day in ["Saturday", "Sunday"]
  
  def generate_styles(self):    
    thin_side = Side(border_style="thin", color="000000")
    all_borders = Border(top=thin_side, bottom=thin_side, left=thin_side, right=thin_side)
    color = "FFE598" if self.is_weekend() else "BDD6EE"

    return {
      "value": self.day,
      "fill": PatternFill(start_color=color, fill_type="solid"),
      "alignment": Alignment(horizontal='center', vertical='center'),
      "border": all_borders,
      "font": Font(
        name='Calibri',
        size=11,
        bold=True,
        italic=False,
        color="000000"
      )
    }