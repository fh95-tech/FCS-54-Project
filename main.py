
class Driver:
  id = 1

  def __init__(self, name, start_city):
    self.name = name
    self.start_city = start_city
    self.worker_id = 'ID' +str(Driver.id).zfill(3) 
    Driver.id += 1

cities=['beirut','saida','jbeil','akkar']
drivers_list = [Driver('max verstappen', 'akkar'),
                Driver('charles leclerc', 'saida'),
                Driver('lando norris', 'jbeil')]
def add_driver():
  name = input("Enter the driver's name: ")
  while True:
    start_city= input("Enter the driver's start city: ")
    if start_city not in cities:
      answer=input('The city is not available in the database,would you like to add it?(y/n) ')
      if answer=='y':
        cities.append(start_city)
        print('City of ',start_city,'is added to the database')
        print(cities)
        break
      elif answer=='n':
        print('enter an existing city')
      else:
        print('enter a valid answer') 
    else:
      break     
  driver = Driver(name.lower(), start_city.lower())
  drivers_list.append(driver)

def view_all_drivers():
  for i in range(len(drivers_list)):
    
    driver = drivers_list[i]
    print(driver.worker_id + ',' , driver.name.title() + ',' , driver.start_city.capitalize())

def drivers_menu():
   print('1. To view all the drivers')
   print('2. To add a driver')
   print('3. To go back to main menu')

   user_input=input()
   if user_input=='1':
      view_all_drivers()
   elif user_input=='2':
      add_driver()
   elif user_input=='3':
      sys_execution()
   else:
      print('invalid input')
      drivers_menu()
      
def cities_menu():
   print('1. Show cities')
   print('2. Print neighboring cities')
   print('3. Print Drivers delivering to city')

def sys_execution():
   print('Hello! Please enter:')
   print('1. To go to the drivers menu')
   print('2. To go to the cities menu')
   print('3. To exit the system')

   answer=input()
   if answer=='1':
      drivers_menu()
   elif answer=='2':
      cities_menu()
   elif answer=='3':
      print('system shutting down')
   else:
      print('invalid input')
      sys_execution()

sys_execution()