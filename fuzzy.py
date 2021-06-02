class RoomTemp:
   coldMember = 0
   mildMember = 0
   normalMember = 0
   warmMember = 0
   hotMember = 0
   
   @classmethod
   def coldMemberSetter(cls,temperature):
      if(temperature>0 and temperature<=10):
         return (temperature-0)/(10-temperature)
      elif(temperature>10 and temperature<20):
         return (20-temperature)/(20-10)
   
   @classmethod
   def mildMemberSetter(cls,temperature):
      if(temperature>15 and temperature<=20):
         return (temperature-15)/(20-15)
      elif(temperature>10 and temperature<20):
         return (25-temperature)/(25-20)
   
   @classmethod
   def normalMemberSetter(cls,temperature):
      if(temperature>20 and temperature<=25):
         return (temperature-20)/(25-20)
      elif(temperature>25 and temperature<30):
         return (30-temperature)/(30-25)

   @classmethod
   def warmMemberSetter(cls,temperature):
      if(temperature>25 and temperature<=30):
         return (temperature-20)/(25-20)
      elif(temperature>30 and temperature<35):
         return (35-temperature)/(35-30)
   
   @classmethod
   def hotMemberSetter(cls,temperature):
      if(temperature>30 and temperature<=35):
         return (temperature-30)/(35-30)
      elif(temperature>35 and temperature<40):
         return (40-temperature)/(40-35)

   @classmethod
   def roomTemperatureMember(cls,temperature):
      cls.coldMember = (0 if (temperature<=0 or temperature>=20) 
                             else cls.coldMemberSetter(temperature))
      cls.mildMember = (0 if(temperature<=15 or temperature>=25) else 
                        cls.mildMemberSetter(temperature))
      cls.normalMember = (0 if(temperature<=20 or temperature>=30) else
                         cls.normalMemberSetter(temperature))
      cls.warmMember = (0 if(temperature<=25 or temperature>=35) else
                         cls.normalMemberSetter(temperature))
      cls.hotMember = (0 if(temperature<=30 or temperature>=40) else
                         cls.warmMemberSetter(temperature))

class outsideTemp:
   mildMember = 0
   normalMember = 0
   warmMember = 0

   @classmethod
   def mildMemberSetter(cls,temperature):
      if(temperature>15 and temperature<=20):
         return (temperature-15)/(20-15)
      elif(temperature>10 and temperature<20):
         return (25-temperature)/(25-20)
   
   @classmethod
   def normalMemberSetter(cls,temperature):
      if(temperature>20 and temperature<=25):
         return (temperature-20)/(25-20)
      elif(temperature>25 and temperature<30):
         return (30-temperature)/(30-25)

   @classmethod
   def warmMemberSetter(cls,temperature):
      if(temperature>25 and temperature<=30):
         return (temperature-20)/(25-20)
      elif(temperature>30 and temperature<35):
         return (35-temperature)/(35-30)

   @classmethod
   def roomTemperatureMember(cls,temperature):
      cls.mildMember = (0 if(temperature<=15 or temperature>=25) else 
                        cls.mildMemberSetter(temperature))
      cls.normalMember = (0 if(temperature<=20 or temperature>=30) else
                         cls.normalMemberSetter(temperature))
      cls.warmMember = (0 if(temperature<=25 or temperature>=35) else
                         cls.normalMemberSetter(temperature))


class totalPeople:
   littleMember = 0
   moderateMember = 0
   manyMember = 0

   @classmethod
   def littleMember(cls, people):
      if(people>0 and people<=25):
         return (people-0)/(25-0)
      elif(people>-5 and people<25):
         return (30-people)/(30-25)
   
   @classmethod
   def moderateMember(cls, people):
      if(people>15 and people<=40):
         return (people-15)/(40-15)
      elif(people>10 and people<40):
         return (45-people)/(45-40)

   @classmethod
   def manyMember(cls, people):
      if(people>30 and people<=50):
         return (people-30)/(50-30)
      elif(people>25 and people<50):
         return (50-people)/(50-25)
   
   @classmethod()
   def totalPeopleMember(cls,people):
      cls.littleMember = (0 if(people<=0 or people>=30) else 
                           cls.littleMemberSetter(people)) 
      cls.moderateMember = (0 if(people<=15 or people>=45) else 
                           cls.moderateMemberSetter(people))  
      cls.manyMember = (0 if(people<=30 or people>=55) else 
                           cls.manyMemberSetter(people))   


class Fuzzy :
   @classmethod
   def valueIinitialization(cls,roomTemp,outsideTemp,numPeople):
      RoomTemp.roomTemperatureMember(roomTemp)
      print("{} {} {} {} {}".format(RoomTemp.coldMember,RoomTemp.hotMember,
                           RoomTemp.mildMember,RoomTemp.warmMember,
                           RoomTemp.normalMember))
   @classmethod
   def inferensi(cls):
      pass



