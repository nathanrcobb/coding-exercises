MIN_LEVEL = 5
MAX_LEVEL = 15

# Light Switch | Brightnesses for given Bulb Capacity
# Dimmer Level | 5 Watt | 10 Watt | 20 Watt
# 5            | 0      | 0       | 0
# 15           | 5      | 10      | 20
# 10           | 2.5    | 5       | 10

class Bulb:
  def setBrightness(self,multiplier:float):
    self.brightness = multiplier * self.wattage
    
  def __init__(self,i:int,w:int,l:float):
    self.i = i
    self.wattage = w
    self.setBrightness(l)

class DimmerSwitch:
  bulbs = {}
  
  def showBulbs(self):
    for k,v in self.bulbs.items():
      print("%s: %s" %(k, v))
  
  def addBulb(self,i:str,wattage:int):
    b = Bulb(i,wattage,self.level)
    self.bulbs[b.i] = b.brightness
  
  def normalizeLevel(self,level:int):
    return ((level-5)/10)
  
  def setLevel(self,level:int):
    self.level = self.normalizeLevel(level)
  
  def __init__(self,level:int):
    self.level = 0.0
    self.brightness = 0.0
    
    self.setLevel(level)

if __name__ == "__main__":
  dimmer = DimmerSwitch(10)
  
  dimmer.addBulb("1",5)
  dimmer.addBulb("2",10)
  dimmer.addBulb("3",15)
  
  dimmer.showBulbs()