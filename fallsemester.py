import uuid as u
from datetime import datetime , timezone

class Expense:
  """Represents an individual financial expense """

  def __init__(self,title : str,amount : float)  -> None :
    """Create instance class variables"""
    self.title = title
    self.amount = float(amount)
    self.id = str(u.uuid4())
    self.created_at = datetime.utcnow()
    self.updated_at = None
  
  def update(self,title=None,amount=None) -> None:
    """Allows updating the title and/or amount, updating the updated_at timestamp """
  
    if title:
      self.title = title
      self.updated_at = datetime.utcnow()
      print("updated Expense {} title to {}".format(self.id,self.title))
    
    if amount:
      self.amount = float(amount)
      self.updated_at = datetime.utcnow()
      print("updated Expense amount to {}".format(self.amount))
      print()
    
    else :
      print("Enter a new title or Amount")
      print()
  
  def to_dict(self) -> dict:
    """Returns a dictionary representation of the expense."""

    return dict(id=self.id,title=self.title,amount=self.amount,created_at=self.created_at,updated_at=self.updated_at)


class ExpenseDatabase:
  """Represents a database that stores expenses"""

  def __init__(self):
    """initialize an empty expense list. A list storing Expense instances"""
    self.expenses = []
  
  def add_expense(self,expense):
    """adds an expense into the  database"""
    
    if expense:
      self.expenses.append(expense)
      print("Expense {} added to database".format(expense.id))
      print()
    
    else :
      print("Enter an expense")
      print()

  def remove_expense(self,expense_id : str):
    """remove an expense from the database"""
    
    for expense in self.expenses:
      if expense.id == expense_id:
        self.expenses.remove(expense)
        print("Expense: {} has been deleted from database".format(expense_id))
        print()
  

  def get_expense_by_id(self,expense_id):
    """Retrieves an expense by ID"""
   
    for expense in self.expenses:
      if expense.id == expense_id:
        return expense


  def get_expense_by_title(self,expense_title) -> list:
    """ Retrieves expenses by title """
    return [expense for expense in self.expenses if expense.title == expense_title]

  def to_dict(self):
    """Returns a list of dictionaries representing expenses """

    return [expense.to_dict() for expense in self.expenses]
  


if __name__ == '__main__':
  """to demonstrate how to use the classes and methods , there are 5 static instances of class expense created below """

  expense1 = Expense("groceries",4500)
  expense2 = Expense("groceries",10000)
  expense3 = Expense("fuel",20000)
  expense4 = Expense("tioletries",2400)
  expense5 = Expense("healthcare",50000)

#create a instance of the expenseDatabase
  db = ExpenseDatabase()

#Add all expenses to the database
  for expense in [expense1,expense2,expense3,expense4,expense5]:
    db.add_expense(expense)

#update an expense
  expense4.update(title='stationary')

# remove an expense from the db
  db.remove_expense(expense3.id)

#get an expense using id
  output = db.get_expense_by_id(expense1.id) #returns an object
  print(output,end='\n')

#return expenses by title
  output = db.get_expense_by_title('groceries') #returns a list of objects
  print(output,end='\n')

#return all expenses from db
  output = db.to_dict()
  print(output,end='\n')
