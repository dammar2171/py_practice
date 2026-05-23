class Tempreture:
  def __init__(self,celsius):
    self.__Celsius = celsius

  @property
  def celcius(self):
    if self.__Celsius >= -273:
      return self.__Celsius
    else:
      return f"❌ Below absolute zero!"
    
  @celcius.setter
  def celcius(self,new_celcius):
    if new_celcius >= -273:
      self.__Celsius = new_celcius
      return self.__Celsius
    else:
      raise ValueError("❌ Below absolute zero!")
    
  @property
  def fahrenheit(self):
    f = self.__Celsius * (9/5) + 32
    return f
  
  @property
  def kelvin(self):
    k = self.__Celsius + 273.15
    return k
  
t = Tempreture(100)
print(t.celcius)
print(t.fahrenheit)
print(t.kelvin)
t.celcius = -400
