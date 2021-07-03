class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passanger = []
  
  def add_passanger(self, name):
    if not self.open_seat():
      return False
    self.passanger.append(name)
    return True

  def open_seat(self):
    return self.capacity - len(self.passanger)

flight = Flight(3)
people= ["kar", "kav", "nil", "kan"]
for person in people:
  if flight.add_passanger(person):
    print(f"Added {person} successfully to the flight")
  else:
    print(f"No available seat for {person}")