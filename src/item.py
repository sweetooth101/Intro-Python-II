class Item():
  def __init__(self, name , description):
    self.name = name
    self.descript = description

  def on_take(self, item):
    print(f"You have picked up {item}")

  def on_drop(self, item):
    print(f"You have dropped {item}")    

  def __repr__(self):
    return self.name  