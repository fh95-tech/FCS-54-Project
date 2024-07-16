class Driver:
  id = 1

  def __init__(self, name, startCity):
    self.name = name
    self.startCity = startCity
    self.workerId = 'ID' +str(Driver.id).zfill(3) 
    Driver.id += 1

cities=[]
driversList = [Driver('max verstappen', 'akkar'),
               Driver('charles leclerc', 'saida'),
              Driver('lando norris', 'jbeil')]
def add_driver():
  name = input("Enter the driver's name: ")
  while True:
    startCity= input("Enter the driver's start city: ")
    if startCity not in cities:
      answer=input('The city is not available in the database,would you like to add it?(y/n) ')
      if answer=='y':
        cities.append(startCity)
        print('City of ',startCity,'is added to the database')
        print(cities)
        break
      elif answer=='n':
        print('enter an existing city')
      else:
        print('enter a valid answer') 
    else:
      break     
  driver = Driver(name.lower(), startCity.lower())
  driversList.append(driver)

def view_all_drivers():
  for i in range(len(driversList)):
    
    driver = driversList[i]
    print(driver.workerId+',', driver.name.title()+',', driver.startCity.capitalize())

