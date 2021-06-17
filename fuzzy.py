
class RoomTemp:
   coldMember = 0
   mildMember = 0
   normalMember = 0
   warmMember = 0
   hotMember = 0
   
   @classmethod 
   def initialize(cls):
      cls.coldMember = 0
      cls.mildMember = 0
      cls.normalMember = 0
      cls.warmMember = 0
      cls.hotMember = 0


   @classmethod
   def coldMemberSetter(cls,temperature):
      if(temperature>0 and temperature<=10):
         return (temperature-0)/(10-0)
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
         return (temperature-25)/(30-25)
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
   def initialize(cls):
      cls.mildMember = 0
      cls.normalMember = 0
      cls.warmMember = 0


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
         return (temperature-25)/(30-25)
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
   def initialize(cls):
      cls.fewMember = 0
      cls.moderateMember = 0
      cls.manyMember = 0
 
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
         return (55-people)/(55-45)
   
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
   linguisticValueOfRule = list()
   numeratorDict = dict()
   denominatorDict = dict()

   @classmethod
   def getInsideTemp(cls) :
      return {'cold' : RoomTemp.coldMember,'mild':RoomTemp.mildMember,'normal':RoomTemp.normalMember,'warm':RoomTemp.warmMember,'hot':RoomTemp.hotMember}
   
   @classmethod
   def getOutsideTemp(cls):
      return {'mild':OutsideTemp.mildMember,'normal':OutsideTemp.normalMember,'warm':OutsideTemp.warmMember}
   
   @classmethod
   def getPeople(cls):
      return {'few':TotalPeople.fewMember,'moderate':TotalPeople.moderateMember,'manyMember':TotalPeople.manyMember}
   
   @classmethod
   def getLinguisticValue(cls):
      linguisticValueDict = {el : cls.linguisticValueOfRule[el] for el in range(len(cls.linguisticValueOfRule))}
      return linguisticValueDict
   
   @classmethod
   def getDenoNomi(cls):
      return {"numerator" : cls.numeratorDict , "denominator":cls.denominatorDict}
   
   @classmethod
   def getDefuzyfikasi(cls):
      response = dict()
      response['cold'] = [i for i in cls.cold]
      response['cold'].append(max(cls.cold))  if(cls.cold) else response['cold'].append(0)
      response['quitecold'] = [i for i in cls.quiteCold]
      response['quitecold'].append(max(cls.quiteCold)) if(cls.quiteCold) else response['quitecold'].append(0)
      response['mild'] = [i for i in cls.quiteMild]
      response['mild'].append(max(cls.mild)) if(cls.mild) else response['mild'].append(0)
      response['normal'] = [i for i in cls.normal]
      response['normal'].append(max(cls.normal)) if(cls.normal) else response['normal'].append(0)
      return response
      

   @classmethod
   def valueIinitialization(cls,roomTemp,outsideTemp,numPeople):
      RoomTemp.initialize()
      OutsideTemp.initialize()
      TotalPeople.initialize()
      cls.cold = list()
      cls.quiteCold = list()
      cls.mild = list()
      cls.quiteMild = list()
      cls.normal = list()
      cls.listOfUsedRule = list()
      cls.linguisticValueOfRule = list()
      cls.numeratorDict = dict()
      cls.denominatorDict = dict()
      RoomTemp.roomTemperatureMember(roomTemp)
      OutsideTemp.outsideTemperatureMember(outsideTemp)
      TotalPeople.totalPeopleMember(numPeople)
   

   @classmethod
   def normalSetter(cls,a,b,c) : 
      minValue = min(a,b,c)
      cls.linguisticValueOfRule.append([a,b,c,minValue])
      cls.normal.append(minValue)
   
   @classmethod
   def quiteColdSetter(cls,a,b,c) :
      minValue = min(a,b,c)
      cls.linguisticValueOfRule.append([a,b,c,minValue])
      cls.quiteCold.append(minValue)

   @classmethod
   def quiteMildSetter(cls,a,b,c) :
      minValue = min(a,b,c)
      cls.linguisticValueOfRule.append([a,b,c,minValue])
      cls.quiteMild.append(minValue)

   @classmethod
   def mildSetter(cls,a,b,c) :
      minValue = min(a,b,c)
      cls.linguisticValueOfRule.append([a,b,c,minValue])
      cls.mild.append(minValue)
   
   @classmethod
   def coldSetter(cls,a,b,c):
      minValue = min(a,b,c)
      cls.linguisticValueOfRule.append([a,b,c,minValue])
      cls.cold.append(minValue)
   

   
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
         cls.listOfUsedRule.append(12)
      
      #rule 13
      if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0) : 
         cls.mildSetter(RoomTemp.mildMember,OutsideTemp.normalMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(13)
      
      #rule 14
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0) : 
         cls.mildSetter(RoomTemp.mildMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(14)
      
      #rule 15
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0) :
         cls.quiteColdSetter(RoomTemp.mildMember,OutsideTemp.normalMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(15)
      
      #rule 16
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.mildMember,OutsideTemp.warmMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(16)
      
      #rule 17
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0):
         cls.quiteColdSetter(RoomTemp.mildMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(17)
      
      #rule 18
      if(OutsideTemp.warmMember>0 and TotalPeople.manyMember>0) :
         cls.coldSetter(RoomTemp.mildMember,OutsideTemp.warmMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(18)
   
   #rule 19 - 27
   #inside Temp / room temp pasti normal
   @classmethod
   def normalCheck(cls):
      #rule 19
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
         cls.quiteMildSetter(RoomTemp.normalMember,OutsideTemp.mildMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(19)
      
      #rule 20
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
         cls.quiteMildSetter(RoomTemp.normalMember,OutsideTemp.mildMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(20)
      
      #rule 21 
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0):
         cls.mildSetter(RoomTemp.normalMember,OutsideTemp.mildMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(21)
      
      #rule 22
      if(OutsideTemp.normalMember>0  and TotalPeople.fewMember>0):
         cls.mildSetter(RoomTemp.normalMember,OutsideTemp.normalMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(22)

      #rule 23 
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0):
         cls.mildSetter(RoomTemp.normalMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(23)
      
      #rule 24 
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0):
         cls.quiteColdSetter(RoomTemp.normalMember,OutsideTemp.normalMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(24)
      
      #rule 25
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.normalMember,OutsideTemp.warmMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(25)
      
      #rule 26
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0) :
         cls.quiteColdSetter(RoomTemp.normalMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(26)
      
      #rule 27 
      if(OutsideTemp.warmMember> 0  and TotalPeople.manyMember>0):
         cls.coldSetter(RoomTemp.normalMember,OutsideTemp.warmMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(27)
      
   
   #rule 28-36 
   #roomtemp pasti warm
   @classmethod
   def warmCheck(cls):

      #rule 28
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
         cls.quiteMildSetter(RoomTemp.warmMember,OutsideTemp.mildMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(28)
      
      #rule 29
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
         cls.quiteMildSetter(RoomTemp.warmMember,OutsideTemp.mildMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(29)
      
      #rule 30
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0):
         cls.mildSetter(RoomTemp.warmMember,OutsideTemp.mildMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(30)
      
      #rule 31
      if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0) : 
         cls.mildSetter(RoomTemp.warmMember,OutsideTemp.normalMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(31)

      #rule 32
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0) : 
         cls.mildSetter(RoomTemp.warmMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(32)
      
      #rule 33
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0) : 
         cls.quiteColdSetter(RoomTemp.warmMember,OutsideTemp.normalMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(33)
      
      #rule 34
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
         cls.quiteColdSetter(RoomTemp.warmMember,OutsideTemp.warmMember,TotalPeople.fewMember)
         cls.listOfUsedRule.append(34)
      
      #rule 35 
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0) :
         cls.quiteColdSetter(RoomTemp.warmMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
         cls.listOfUsedRule.append(35)
      
      #rule 36
      if(OutsideTemp.warmMember> 0 and TotalPeople.manyMember>0):
         cls.coldSetter(RoomTemp.warmMember,OutsideTemp.warmMember,TotalPeople.manyMember)
         cls.listOfUsedRule.append(36)

   #Rule 37-45
   #roomtemp Hot
   @classmethod
   def hotCheck(cls):

   #rule 37
      if(OutsideTemp.mildMember>0 and TotalPeople.fewMember>0):
            cls.mildSetter(RoomTemp.hotMember,OutsideTemp.mildMember,TotalPeople.fewMember)
            cls.listOfUsedRule.append(37)
      
      #rule 38
      if(OutsideTemp.mildMember>0 and TotalPeople.moderateMember>0):
            cls.mildSetter(RoomTemp.hotMember,OutsideTemp.mildMember,TotalPeople.moderateMember)
            cls.listOfUsedRule.append(38)

      #rule 39
      if(OutsideTemp.mildMember>0 and TotalPeople.manyMember>0):
            cls.quiteColdSetter(RoomTemp.hotMember,OutsideTemp.mildMember,TotalPeople.manyMember)
            cls.listOfUsedRule.append(39)
      
      #rule 40
      if(OutsideTemp.normalMember>0 and TotalPeople.fewMember>0):
            cls.quiteColdSetter(RoomTemp.hotMember,OutsideTemp.normalMember,TotalPeople.fewMember)
            cls.listOfUsedRule.append(40)
      
      #rule 41
      if(OutsideTemp.normalMember>0 and TotalPeople.moderateMember>0):
            cls.quiteColdSetter(RoomTemp.hotMember,OutsideTemp.normalMember,TotalPeople.moderateMember)
            cls.listOfUsedRule.append(41)

      #rule 42
      if(OutsideTemp.normalMember>0 and TotalPeople.manyMember>0):
            cls.coldSetter(RoomTemp.hotMember,OutsideTemp.normalMember,TotalPeople.manyMember)
            cls.listOfUsedRule.append(42)
      
      #rule 43
      if(OutsideTemp.warmMember>0 and TotalPeople.fewMember>0):
            cls.coldSetter(RoomTemp.hotMember,OutsideTemp.warmMember,TotalPeople.fewMember)
            cls.listOfUsedRule.append(43)
      
      #rule 44
      if(OutsideTemp.warmMember>0 and TotalPeople.moderateMember>0):
            cls.coldSetter(RoomTemp.hotMember,OutsideTemp.warmMember,TotalPeople.moderateMember)
            cls.listOfUsedRule.append(44)

      #rule 45
      if(OutsideTemp.warmMember>0 and TotalPeople.manyMember>0):
            cls.coldSetter(RoomTemp.hotMember,OutsideTemp.warmMember,TotalPeople.manyMember)
            cls.listOfUsedRule.append(45)



   @classmethod
   def membershipOfOutput(cls,lBound,upBound,x) :
      return (upBound-x)/(x-lBound)

   @classmethod
   def defuzzifikasi(cls,maxList):
      numerator = 0
      denominator = 0 
      #sample = [12,13,14,15,16,17,18,19,20,21,22,23,24]
      # sampleCold = [12,13,14,15,16]
      # sampleQuiteCold = [16,17,18]
      # sampleMild = [18,19,20]
      # sampleQuiteMild = [20,21,22]
      # sampleNormal = [22,23,24]
      membershipOutput = {1:[12,13,14,15,16],2:[16,17,18],3:[18,19,20],4:[20,21,22],5:[22,23,24]}
      membershipOutputConstant = {1:[12,13,14,15,16],2:[16,17,18],3:[18,19,20],4:[20,21,22],5:[22,23,24]}
      
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
                     middleIndex = (len(membershipOutputConstant[checkLst[i+1]]) - 1)/2
                     # print("middle index",middleIndex)
                     # print("membership output",membershipOutputConstant[checkLst[i+1]][int(middleIndex)])
                     lstTuple.append((e,cls.membershipOfOutput(membershipOutputConstant[checkLst[i+1]][0],
                                             membershipOutputConstant[checkLst[i+1]][int(middleIndex)],e)))
                     membershipOutput[checkLst[i+1]].remove(e)

         except Exception as e: 
            break
      cls.numeratorDict["data"] =''
      cls.denominatorDict["data"] = ''
      print(membershipOutput)
      print(lstTuple)
      for i in checkLst : 
         numerator += sum(membershipOutput[i]) * maxList[i]
         denominator += len(membershipOutput[i])*maxList[i]
         memberStr = [str(i) for i in membershipOutput[i]]
         cls.numeratorDict["data"] += '(' + ' + '.join(memberStr) + ')' + ' * {}'.format(maxList[i]) + ' + '
         cls.denominatorDict['data'] += '{} * {} + '.format(len(membershipOutput[i]),maxList[i])
      for i,tuplee in lstTuple:
         numerator+= i * tuplee
         cls.numeratorDict["data"] +=  '{} * {} + '.format(i,tuplee)
         denominator += tuplee
         cls.denominatorDict["data"] += '{} * 1 + '.format(tuplee,3)
      
      cls.numeratorDict['value'] = numerator
      cls.denominatorDict['value'] = denominator    
      cls.numeratorDict['otuputValue'] = numerator/denominator  
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
         cls.hotCheck()
   
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
      


