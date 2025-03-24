class Villager:
  def __init__(self, name, species, catchphrase):
      self.name = name
      self.species = species
      self.catchphrase = catchphrase
      self.furniture = []

  def add_item(self, item_name):
    valid_list = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
    if item_name in valid_list:
      self.furniture.append(item_name)

  def print_inventory(self):
    inventory_dictionary = {}

    if len(self.furniture) == 0:
      print("Inventory empty")
    else:
      for i in self.furniture:
        if i not in inventory_dictionary:
          inventory_dictionary[i] = 1
        else: 
          inventory_dictionary[i] += 1
    
    
    for key, value in inventory_dictionary.items():
    
        
    
    


alice = Villager("Alice", "Koala", "guvnor")
alice.print_inventory()


add_list = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
for i in add_list:
  alice.add_item(i)

alice.print_inventory()