import datetime
import argparse

from timesheet_generator.TimesheetGenerator import TimesheetGenerator

def main():
  parser = argparse.ArgumentParser(description="Generates timesheet with properly formatted leaves in an excel file")
  parser.add_argument(
    "--name", 
    help="name of the employee for whome timesheet is being generated", 
    type=str, 
    required=True
  )
  parser.add_argument(
    "--month",
    help="number of the month for which timesheet is being generated (1-12) (if not provided current month will be used)",
    type=int,
    default=datetime.datetime.now().month
  )
  parser.add_argument(
    "--year",
    help="Year for which timesheet is being generated as number (e.g. 2026) (if not provided current year will be used)",
    type=int,
    default=datetime.datetime.now().year
  )
  parser.add_argument(
    "--leaves",
    help="""
      Leaves to be considered when timesheet is being generated
      These leaves should be in a particular format
      For example - if you've taken 1st as paid full leave and 10th was a 
      national holiday, then it should be --leaves "1:PFL 10:HO", 
      These are the supported leave types - 
      Present - P, Unpaid Half Leave - UHL, Unpaid Full Leave - UFL, Maternity Leave - ML, Casual Leave - CL, Client Holiday - CHO, Compensatory Off - COFF, Work From Home - WFH, Paid Full Leave - PFL, Paid Half Leave - PHL, National Holiday - HO, Week off - WO.
      You can use leave types not mentioned here as well but they won't be styled.
      If data is provided in improper format then the program will not proceed. 
      In case no leaves are provided all weekdays will be marked present and weekends as weekoff
    """,
    type=str,
    default=""
  )
  parser.add_argument(
    "--verbose",
    help="Print more information about the error",
    action=argparse.BooleanOptionalAction
  )
  args = parser.parse_args()

  try:
    TimesheetGenerator(
      args.name,
      args.month,
      args.year,
      args.leaves
    ).generate()
  except Exception:
    if args.verbose:
      raise
    else:
      parser.error("Program ran into an error. Please make sure all data is in proper format.")

if __name__ == "__main__": main()