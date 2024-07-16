class Driver:
  id = 1

  def __init__(self, name, startCity):
    self.name = name
    self.startCity = startCity
    self.workerId = 'ID' +str(Driver.id).zfill(3) 
    Driver.id += 1