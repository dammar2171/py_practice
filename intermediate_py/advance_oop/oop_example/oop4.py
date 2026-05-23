from abc import ABC,abstractmethod
class Vechile(ABC):
  @abstractmethod
  def start_engine(self):
    pass
  @abstractmethod
  def stop_engine(self):
    pass
  @abstractmethod
  def fuel_type(self):
    pass
  def __str__(self):
    return f"{self.__class__.__name__} (Fuel: {self.fuel}, Speed: {self.speed})"
class PetrolCar(Vechile):
  def __init__(self,fuel,speed):
    self.fuel = fuel
    self.speed = speed

  def start_engine(self):
    return f"{self.fuel} car engine is started!"
  
  def stop_engine(self):
    return f"{self.fuel} car engine is stopped!"
  
  def fuel_type(self):
    return f"Fuel type : {self.fuel}"
  
  @property
  def speed_limit(self):
    if self.speed > 200:
      return "Speed is too high!"
    else:
      return "Good speed!"
  
class ElectricCar(Vechile):
  def __init__(self,fuel,speed):
    self.speed = speed
    self.fuel = fuel

  def start_engine(self):
    return f"{self.fuel} car engine is started!"
  
  def stop_engine(self):
    return f"{self.fuel} car engine is stopped!"
  
  def fuel_type(self):
    return f"Fuel type : {self.fuel}"
  @property
  def speed_limit(self):
    if self.speed > 80:
      return "Speed is too high!"
    else:
      return "Good speed!"
    
class Bicycle(Vechile):
  def __init__(self,fuel,speed):
    self.speed = speed
    self.fuel = fuel

  def start_engine(self):
    return f"peddling started!"
  
  def stop_engine(self):
    return f"{self.fuel} car engine is stopped!"
  
  def fuel_type(self):
    return f"Fuel type : {self.fuel}"
  @property
  def speed_limit(self):
    if self.speed > 40:
      return "Speed is too high!"
    else:
      return "Good speed!"
    
pc = PetrolCar("petrol",200)
Ec = ElectricCar("electricity",78)
bc = Bicycle("Human Power",22)

print(pc)
print(pc.start_engine())
print(pc.stop_engine())
print(pc.speed_limit)