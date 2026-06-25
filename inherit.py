class _vehicle:

  def __init__(self,brand,color,speed):

    self.brand = brand
    self.color = color
    self.speed = speed
    self.is_running = False #means all cars at off position in starting

  def start(self):
    if self.is_running:
      print(f" {self.brand} is already running !")
    else:
      self.is_running = True
      print(f"{self.brand} started. Vroom!!")

  def stop(self):
    if not self.is_running:
      print(f"  {self.brand} is already stopped!")
    else:
      self.is_running = False
      print(f"{self.brand} has stopped!!")

def fuel_type(self):
  print(f"Fuel: Petrol/Diesel")
def describe(self):
  status = "Running" if self.is_running else "stopped"
  print(f"""
  Brand: {self.brand}
  Color: {self.color}
  Speed: {self.speed} km/hr
  Status: {self.status}
  """")