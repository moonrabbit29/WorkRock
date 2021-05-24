class RoomTemp:
   coldMember = 0
   mild = 0
   normal = 0
   warm = 0
   hot = 0
   
   @classmethod
   def coldMemberSetter(temperature):
      if(temperature>0 and temperature<=10):
         return (temperature-0)/(10-temperature)
      elif(temperature>10 and temperature<20):
         return (20-temperature)/(20-10)
   
   @classmethod
   def mildMemberSetter(temperature):
      if(temperature>15 and temperature<=20):
         return (temperature-15)/(20-temperature)
      elif(temperature>10 and temperature<20):
         return (25-temperature)/(25-20)
   
   @classmethod
   def normalMemberSetter(temperature):
      if(temperature>20 and temperature<=25):
         return (temperature-20)/(25-20)
      elif(temperature>25 and temperature<30):
         return (30-temperature)/(30-25)

   @classmethod
   def warmMemberSetter(temperature):
      if(temperature>25 and temperature<=30):
         return (temperature-20)/(25-20)
      elif(temperature>30 and temperature<35):
         return (35-temperature)/(35-30)
   
   @classmethod
   def warmMemberSetter(temperature):
      if(temperature>30 and temperature<=35):
         return (temperature-30)/(35-30)
      elif(temperature>35 and temperature<40):
         return (40-temperature)/(40-35)

   @classmethod
   def roomTemperatureMember(temperature):
      RoomTemp.coldMember = (0 if (temperature<=0 or temperature>=20) 
                             else RoomTemp.coldMemberSetter(temperature))
      RoomTemp.mild = (0 if(temperature<=15 or temperature>=25) else 
                        RoomTemp.mildMemberSetter(temperature))
      RoomTemp.normal = (0 if(temperature<=20 or temperature>=30) else
                         RoomTemp.normalMemberSetter(temperature))
      RoomTemp.warm = (0 if(temperature<=25 or temperature>=35) else
                         RoomTemp.normalMemberSetter(temperature))
      RoomTemp.hot = (0 if(temperature<=30 or temperature>=40) else
                         RoomTemp.warmMemberSetter(temperature))

class Fuzzy :

   @classmethod
   def inferensi():
      pass


