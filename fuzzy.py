from typing import Dict


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
      elif(temperature>20 and temperature<25):
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
                         cls.warmMemberSetter(temperature))
      cls.hotMember = (0 if(temperature<=30 or temperature>=40) else
                         cls.hotMemberSetter(temperature))

class OutsideTemp:
   mildMember = 0
   normalMember = 0
   warmMember = 0

   @classmethod
   def mildMemberSetter(cls,temperature):
      if(temperature>15 and temperature<=20):
         return (temperature-15)/(20-15)
      elif(temperature>20 and temperature<25):
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
   def outsideTemperatureMember(cls,temperature):
      cls.mildMember = (0 if(temperature<=15 or temperature>=25) else 
                        cls.mildMemberSetter(temperature))
      cls.normalMember = (0 if(temperature<=20 or temperature>=30) else
                         cls.normalMemberSetter(temperature))
      cls.warmMember = (0 if(temperature<=25 or temperature>=35) else
                         cls.warmMemberSetter(temperature))


class TotalPeople:
   fewMember = 0
   moderateMember = 0
   manyMember = 0
 
   @classmethod
   def fewMemberSetter(cls, people):
      if(people>0 and people<=15):
         return (people-0)/(15-0)
      elif(people>15 and people<30):
         return (30-people)/(30-15)
   
   @classmethod
   def moderateMemberSetter(cls, people):
      if(people>15 and people<=30):
         return (people-15)/(30-15)
      elif(people>30 and people<45):
         return (45-people)/(45-30)

   @classmethod
   def manyMemberSetter(cls, people):
      if(people>30 and people<=45):
         return (people-30)/(45-30)
      elif(people>45 and people<55):
         return (55-people)/(45-55)
   
   @classmethod
   def totalPeopleMember(cls,people):
      cls.fewMember = (0 if(people<=0 or people>=30) else 
                           cls.fewMemberSetter(people)) 
      cls.moderateMember = (0 if(people<=15 or people>=45) else 
                           cls.moderateMemberSetter(people))  
      cls.manyMember = (0 if(people<=30 or people>=55) else 
                           cls.manyMemberSetter(people))   


class Fuzzy :
   cold = list()
   quiteCold = list()
   mild = list()
   quiteMild = list()
   normal = list()
   listOfUsedRule = list()

   @classmethod
   def valueIinitialization(cls,roomTemp,outsideTemp,numPeople):
      RoomTemp.roomTemperatureMember(roomTemp)
      OutsideTemp.outsideTemperatureMember(outsideTemp)
      TotalPeople.totalPeopleMember(numPeople)
   
   @classmethod
   def normalSetter(cls,a,b,c) : 
      cls.normal.append(min(a,b,c))
   
   @classmethod
   def quiteColdSetter(cls,a,b,c) :
      cls.quiteCold.append(min(a,b,c))

   @classmethod
   def quiteMildSetter(cls,a,b,c) :
      cls.quiteMild.append(min(a,b,c))

   @classmethod
   def mildSetter(cls,a,b,c) :
      cls.mild.append(min(a,b,c))
   
   @classmethod
   def coldSetter(cls,a,b,c):
      cls.cold.append(min(a,b,c))
   

   
   #rule 1 - 9
   #inside temp / room temp pasti dingin
   @classmethod
   def checkCold(cls) :
      #rule 1
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0) : 
         cls.normalSetter(RoomTemp.coldMember,OutsideTemp.mildMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(1)
      
      #rule2
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0) :
         cls.normalSetter(RoomTemp.coldMember,OutsideTemp.mildMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(2)
      
      #rule3
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0) : 
         cls.quiteMildSetter(RoomTemp.coldMember,OutsideTemp.mildMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(3)
      
      #rule 4
      if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0):
         cls.quiteMildSetter(RoomTemp.coldMember,OutsideTemp.normalMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(4)
      
      #rule 5
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0) : 
         cls.quiteMildSetter(RoomTemp.coldMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(5)
      
      #rule 6 
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0):
         cls.mildSetter(RoomTemp.coldMember,OutsideTemp.normalMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(6)
      
      #rule 7
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0) :
         cls.mildSetter(RoomTemp.coldMember,OutsideTemp.warmMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(7)
      
      #rule 8
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0) :
         cls.mildSetter(RoomTemp.coldMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(8)

      #rule 9 
      if(OutsideTemp.warmMember>0 and TotalPeople.manyMember>0) : 
         cls.quiteMildSetter(RoomTemp.coldMember,OutsideTemp.warmMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(9)


   #rule 10 - 18
   #inside temp/room temp pasti sejuk
   @classmethod
   def checkMild(cls):
      
      #rule 10
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
         cls.quiteMildSetter(RoomTemp.mildMember,OutsideTemp.mildMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(10)
      
      #rule 11 (salah di TotalPeople)
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
         cls.quiteMildSetter(RoomTemp.mildMember,OutsideTemp.mildMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(11)
      
      #rule 12
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0) : 
         cls.mildSetter(RoomTemp.mildMember,OutsideTemp.mildMember,TotalPeople.manyMember)
      
      #rule 13
      if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0) : 
         cls.mildSetter(RoomTemp.mildMember,OutsideTemp.normalMember,TotalPeople.fewMember)
      
      #rule 14
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0) : 
         cls.mildSetter(RoomTemp.mildMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
      
      #rule 15
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0) :
         cls.quiteColdSetter(RoomTemp.mildMember,OutsideTemp.normalMember,TotalPeople.manyMember)
      
      #rule 16
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.mildMember,OutsideTemp.warmMember,TotalPeople.fewMember)
      
      #rule 17
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0):
         cls.quiteColdSetter(RoomTemp.mildMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
      
      #rule 18
      if(OutsideTemp.warmMember>0 and TotalPeople.manyMember>0) :
         cls.coldSetter(RoomTemp.mildMember,OutsideTemp.warmMember,TotalPeople.manyMember)
   
   #rule 19 - 27
   #inside Temp / room temp pasti normal
   @classmethod
   def normalCheck(cls):
      #rule 19
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
         cls.quiteMildSetter(RoomTemp.normalMember,OutsideTemp.mildMember,TotalPeople.fewMember)
      
      #rule 20
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
         cls.quiteMildSetter(RoomTemp.normalMember,OutsideTemp.mildMember,TotalPeople.moderateMember)
      
      #rule 21 
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0):
         cls.mildSetter(RoomTemp.normalMember,OutsideTemp.mildMember,TotalPeople.manyMember)
      
      #rule 22
      if(OutsideTemp.normalMember>0  and TotalPeople.fewMember>0):
         cls.mildSetter(RoomTemp.normalMember,OutsideTemp.normalMember,TotalPeople.fewMember)

      #rule 23 
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0):
         cls.mildSetter(RoomTemp.normalMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
      
      #rule 24 
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0):
         cls.quiteColdSetter(RoomTemp.normalMember,OutsideTemp.normalMember,TotalPeople.manyMember)
      
      #rule 25
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.normalMember,OutsideTemp.warmMember,TotalPeople.fewMember)
      
      #rule 26
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0) :
         cls.quiteColdSetter(RoomTemp.normalMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
      
      #rule 27 
      if(OutsideTemp.warmMember> 0  and TotalPeople.manyMember>0):
         cls.coldSetter(RoomTemp.normalMember,OutsideTemp.warmMember,TotalPeople.manyMember)
      
   
   #rule 28-36 
   #roomtemp pasti warm
   @classmethod
   def warmCheck(cls):

      #rule 28
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
         cls.quiteMildSetter(RoomTemp.warmMember,OutsideTemp.mildMember,TotalPeople.fewMember)
      
      #rule 29
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
         cls.quiteMildSetter(RoomTemp.warmMember,OutsideTemp.mildMember,TotalPeople.moderateMember)
      
      #rule 30
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0):
         cls.mildSetter(RoomTemp.warmMember,OutsideTemp.mildMember,TotalPeople.manyMember)
      
      #rule 31
      if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0) : 
         cls.mildSetter(RoomTemp.warmMember,OutsideTemp.normalMember,TotalPeople.fewMember)

      #rule 32
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0) : 
         cls.mildSetter(RoomTemp.warmMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
      
      #rule 33
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0) : 
         cls.quiteColdSetter(RoomTemp.warmMember,OutsideTemp.normalMember,TotalPeople.manyMember)
      
      #rule 34
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.warmMember,OutsideTemp.warmMember,TotalPeople.fewMember)
      
      #rule 35 
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0) :
         cls.quiteColdSetter(RoomTemp.warmMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
      
      #rule 36
      if(OutsideTemp.warmMember> 0 and TotalPeople.manyMember>0):
         cls.coldSetter(RoomTemp.warmMember,OutsideTemp.warmMember,TotalPeople.manyMember)

   #Rule 37-45
   #roomtemp Hot
   @classmethod
   def hotCheck(cls):

   #rule 37
   if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
         cls.MildSetter(RoomTemp.HotMember,OutsideTemp.mildMember,TotalPeople.fewMember)
   
   #rule 38
   if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
         cls.MildSetter(RoomTemp.HotMember,OutsideTemp.mildMember,TotalPeople.moderateMember)

   #rule 39
   if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0):
         cls.quiteColdSetter(RoomTemp.HotMember,OutsideTemp.mildMember,TotalPeople.manyMember)
   
   #rule 40
   if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.HotMember,OutsideTemp.normalMember,TotalPeople.fewMember)
   
   #rule 41
   if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0):
         cls.quiteColdSetter(RoomTemp.HotMember,OutsideTemp.normalMember,TotalPeople.moderateMember)

   #rule 42
   if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0):
         cls.coldSetter(RoomTemp.HotMember,OutsideTemp.normalMember,TotalPeople.manyMember)
   
   #rule 43
   if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.coldSetter(RoomTemp.HotMember,OutsideTemp.warmMember,TotalPeople.fewMember)
   
   #rule 44
   if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0):
         cls.coldSetter(RoomTemp.HotMember,OutsideTemp.warmMember,TotalPeople.moderateMember)

   #rule 45
   if(OutsideTemp.warmMember>0 and TotalPeople.manyMember>0):
         cls.coldSetter(RoomTemp.HotMember,OutsideTemp.warmMember,TotalPeople.manyMember)



   @classmethod
   def membershipOfOutput(cls,lBound,upBound,x) :
      a = (upBound-x)/(x-lBound)
      return (upBound-x)/(x-lBound)

   @classmethod
   def defuzzifikasi(cls,maxList):
      numerator = 0
      denominator = 0 
      sample = [12,13,14,15,16,17,18,19,20,21,22,23,24]
      # sampleCold = [12,13,14,15,16]
      # sampleQuiteCold = [16,17,18]
      # sampleMild = [18,19,20]
      # sampleQuiteMild = [20,21,22]
      # sampleNormal = [22,23,24]
      membershipOutput = {1:[12,13,14,15,16],2:[16,17,18],3:[18,19,20],4:[20,21,22],5:[22,23,24]}
      
      checkLst = []
      
      #create list of tuple for sample that are in between two outpu fuzzy graph
      lstTuple = []

      for key,value in maxList.items() : 
         if value>0 : 
            checkLst.append(key)
      for i in range(len(checkLst)):
         try :
            if(checkLst[i+1] - checkLst [i] == 1):
               for e in membershipOutput[checkLst[i]] : 
                  if(e in membershipOutput[checkLst[i+1]]):
                     membershipOutput[checkLst[i]].remove(e)
                     lstTuple.append((e,cls.membershipOfOutput(membershipOutput[checkLst[i+1]][0]-1,
                                             membershipOutput[checkLst[i+1]][-1]+1,e)))

         except Exception as e: 
            break
      
      for i in checkLst : 
         numerator += sum(membershipOutput[i]) * maxList[i]
         denominator += len(membershipOutput[i])*maxList[i]
      for i,tuplee in lstTuple:
         numerator+= i * tuplee
         denominator += tuplee
      
      return numerator/denominator 
         
      

   @classmethod
   def inferensi(cls):
      bestTemp = 0

      if(RoomTemp.coldMember > 0 ) : 
         cls.checkCold()
      if(RoomTemp.mildMember > 0 ) : 
         cls.checkMild()
      if(RoomTemp.normalMember >0 ) :
         cls.normalCheck()
      if(RoomTemp.warmMember>0):
         cls.warmCheck()
      if(RoomTemp.hotMember>0):
         pass
   
      #keterangan 
      # 1:cold
      # 2:quiteCold
      # 3:mild
      # 4:quiteMild
      # 5: normal
      maxList = list() 
      maxList.append((1,max(cls.cold)))  if(cls.cold) else maxList.append((1,0))
      maxList.append((2,max(cls.quiteCold))) if(cls.quiteCold) else maxList.append((2,0))
      maxList.append((3,max(cls.mild))) if(cls.mild)  else maxList.append((3,0))
      maxList.append((4,max(cls.quiteMild))) if(cls.quiteMild) else maxList.append((4,0))
      maxList.append((5,max(cls.normal)))if(cls.normal) else maxList.append((5,0))

      maxDictionary = dict()
      for a, b in maxList:
         maxDictionary.setdefault(a,b)
      bestTemp = cls.defuzzifikasi(maxDictionary)
      return bestTemp
      


