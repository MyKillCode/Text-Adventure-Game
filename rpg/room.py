class Room():
  def __init__(self, room_name):
    """ Initialises a room with a name """
    self.name = room_name
    self.description = None 
    self.linked_rooms = {}
    self.character = None
    self.item = None

  def set_character(self, character):
    """ adds a character to the room """
    self.character = character

  def get_character(self):
    """ Returns if there is a character in the room and who they are """
    return self.character
  
  def set_description(self, room_description):
    """ Sets a description for the room """
    self.description = room_description
  
  def get_description(self):
    """ Returns the room's description """
    return self.description
  
  def set_name(self, room_name):
    """ Sets the Room's name """
    self.name = room_name
  
  def get_name(self):
    """ Returns the Room's name """
    return self.name

  def set_item(self, item_name):
    """ sets the item that is in the room """
    self.item = item_name
  
  def get_item(self):
    """ Returns if there is an item in the Room """
    return self.item
  
  def describe(self):
    """ Prints out a description of the Room """
    print(self.description)
  
  def link_room(self, room_to_link, direction):
    """ Likns the room to other rooms using a compass point """
    self.linked_rooms[direction] = room_to_link
    #print( self.name + " linked rooms :" + repr(self.linked_rooms) )
  
  def get_details(self):
    """ Prints out the full details of the room, including Name, Description, and the rooms that are linked """
    print(self.name)
    print("------------------")
    print(self.description)
    for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print( "The " + room.get_name() + " is " + direction)
  
  def move(self, direction):
    """ Checks to see if there is a room connected in the given direction """
    if direction in self.linked_rooms:
        return self.linked_rooms[direction]
    else:
        print("You can't go that way")
        return self
