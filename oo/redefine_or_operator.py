class x:
  """Define "|" on an arbitrary class to prove that 
     you can define almost any operator on a class."""

  def __init__(self, name):
    self.name = name;

  def __or__(self, other):
    print(self.name + "<-->" + other.name)

x1 = x("Robin")
x2 = x("Smith")
x1 | x2

