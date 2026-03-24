from datetime import datetime
import uuid
from collections import defaultdict

class Expense:
  def __init__(self,amount,category,description, date=None):
    self.id=str(uuid.uuid4())
    self.amount=amount
    self.category=category
    self.description=description

    if date is None:
      self.date=datetime.now().date()
    else:
      self.date=date

def get_valid_date():
  while True:
    user_input=input("Enter date(YYY-MM-DD):")
    try:
      return datetime.strptime(user_input,"%Y-%m-%d").date()
    except ValueError:
      print("Invalid date format.Try again.")

def add_expense(expenses):
  amount=float(input("Enter amount: "))
  category=input("Enter category:")
  description=input("Enter description: ")

  date=get_valid_date()

  expense=Expense(amount,category,description,date)
  expenses.append(expense)

  print("Expense added!!\n")

def show_expenses(expenses):
  if not expenses:
    print("No expenses found.")
    return 

  for e in expenses:
    print(f"ID:{e.id}")
    print(f"Amount:{e.amount}")
    print(f"Category:{e.category}")
    print(f"Description:{e.description}")
    print(f"Date:{e.date}")
    print("-"*30)
def monthly_summary(expenses):
  summary=defaultdict(float)

  for e in expenses:
    month=e.dict.strftime("%Y-%m")
    summary[month]+=e.amount

  print("\n---Monthly Summary---")
  for month,total in summary.items():
    print(f"{month}:{total}")

def category_breakdown(expeneses):
  breakdown=defaultdict(float)

  for e in expenses:
    breakdown[e.category]+=e.amount

  
  print("\n---Category Breakdown---")
  for category, total in breakdown.item():
    print(f"{category}:{total}")
expenses=[]

while True:
  print("\n---Expense Tracker---")
  print("1.Add Expense")
  print("2.Show Expense")
  print("3.Monthly Summary")
  print("4.Category Breakdown")
  print("5.Exit")

  choice=input("Enter choice(1-5)")

  if choice=="1":
    add_expense(expenses)
  elif choice=="2":
    show_expenses(expenses)
  elif choice=="3":
    monthly_summary(expenses)
  elif choice=="4":
    category_breakdown(expenses)
  elif choice=="5":
    print("Exiting...")
    break
  else:
    print("Invalid Choice. \n")