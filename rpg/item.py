class Item():
  
  def __init__(self, item_name):
    """ Initialise the item with a name """
    self.name = item_name
    self.description = None
    
  def get_name(self):
    """ Returns the name of the item """
    return self.name
    
  def set_name(self, item_name):
    """ Sets the name of the item to item_name """
    self.name = item_name
    
  def get_description(self):
    """ Returns the description of the item """
    return self.description
    
  def set_description(self, item_description):
    """ Sets the item's description """
    self.description = item_description

  def describe(self):
    """ Prints out a description of the item """
    print("The [" + self.name + "] is here - " + self.description)
