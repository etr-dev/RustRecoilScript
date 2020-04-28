#SENSITIVITY: .5
#DPI: 800dpi


#AK SHOT DELAY: 133ms
#int[] akY = { 58 ,56, 50,46 ,40,26,24,34,16,12,14,16,36,34,42 ,46 ,36 ,40 ,30 ,20 ,16 ,8  ,8  ,12,26,0,0,0,0,0};
#int[] akX = { -41,5 ,-60,-52,0 ,20,28,46,58,48,52,30,28,-8,-20,-30,-52,-54,-60,-56,-52,-44,-42,18,0 ,0,0,0,0,0};
	
#int lrX[] = { -4, -7, -12, -15, -18, -20, -15, -7, 19, 24, 23, 22, 13, -7, -8, -10, -11, -13, -16, -19, -20, -25, -27, 10, 10, 15, 45, 55, 20 };
#int lrY[] = { 31, 32, 37, 36, 27, 21, 13, 17, 13, 9, 10, 8, 7, 6, 5, 6, 5, 6, 5, 6, 5, 5, 5, 4, 5, 4, 5, 4, 4 };

#int sarX[] = {0};
#int sarY[] = {88};

#startX = 976;
#startY = 717;
title = "RECOIL SCRIPT"
currentX = 976
currentY = 717
convertedX = []
convertedY =[]
smoothFactor = 4;

def userInput():
  print("------------NULLPNTR'S RUST RECOIL RAZER MACRO CREATOR------------")
  print("This has no error checking so enter the right thing, if you enter 0 shots \nor more shots than the gun has in a mag it will give you an error or messed up list\n")
  print("------------------------------------------------------------\n")
  weaponChoice = input("Choose Weapon: (Enter the Number) \n"
      + "\t1) AK-47\n"
      + "\t2) LR-300\n"
      + "\t3) SAR\n");
  weaponChoice = str(int(weaponChoice) - 1)
  
  print("\n")

  shotLength = input("How many bullets do you want to shoot?")

  title = input("What would you like to name this script?\n")
  XMLprint(getWeaponCoords(0)[0][:int(shotLength)-1],getWeaponCoords(0)[1][:int(shotLength)-1],getWeaponCoords(0)[2][0],title)

def getWeaponCoords(weaponIndex):
  if weaponIndex == 0: #is AK
    return [
      [-41,5 ,-60,-52,0 ,20,28,46,58,48,52,30,28,-8,-20,-30,-52,-54,-60,-56,-52,-44,-42,18,0 ,0,0,0,0,0], #AKX
      [ 58 ,56, 50,46 ,40,26,24,34,16,12,14,16,36,34,42 ,46 ,36 ,40 ,30 ,20 ,16 ,8  ,8  ,12,26,0,0,0,0,0], #AKY
      [133], #AK SHOT DELAY
      [30]
      ];
  if weaponIndex == 1: #is LR
    return [
      [ -4, -7, -12, -15, -18, -20, -15, -7, 19, 24, 23, 22, 13, -7, -8, -10, -11, -13, -16, -19, -20, -25, -27, 10, 10, 15, 45, 55, 20], #LRX
      [31, 32, 37, 36, 27, 21, 13, 17, 13, 9, 10, 8, 7, 6, 5, 6, 5, 6, 5, 6, 5, 5, 5, 4, 5, 4, 5, 4, 4], #LRY
      [120], #LR SHOT DELAY
      [30]
    ];
  if weaponIndex == 2: #is SAR
    return [
      [0], #SARX
      [88], #SARY
      [175], #SAR SHOT DELAY
      [16]
    ];

#getWeaponCoords(selectedWeapon)[0]
def XMLprint(weaponX,weaponY,delay,title):
  #stuff
  #print(XMLprintStart(title))
  #print(XMLprintRecoil(weaponX,weaponY,delay))
  #print(XMLprintEnd())
  file = open(title+".xml", "w") 
  file.write(XMLprintStart(title) + XMLprintRecoil(weaponX,weaponY,delay) + XMLprintEnd()) 
  file.close() 

def XMLprintStart(scriptName):
  return "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n" + "<Macro xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">\r\n" + "  <Name>" + scriptName + "</Name>\r\n" + "  <Guid>90b869c3-c9ea-438d-b055-2ba311899260</Guid>\r\n" + "  <MacroEvents>\r\n" + "    <MacroEvent>\r\n" + "      <Type>2</Type>\r\n" + "      <MouseEvent>\r\n" + "        <MouseButton>1</MouseButton>\r\n" + "        <State>0</State>\r\n" + "      </MouseEvent>\r\n" + "    </MacroEvent>\r\n" + "    <MacroEvent>\r\n" + "      <Type>3</Type>\r\n" + "      <Delay>0</Delay>\r\n" + "      <MouseMovement>\r\n"

def XMLprintRecoil(weaponX,weaponY,delay):
  convertedX = convertList(weaponX,currentX)
  convertedY = convertList(weaponY,currentY)

  smoothedX = smoothing(convertedX, smoothFactor)
  smoothedY = smoothing(convertedY, smoothFactor)

  #print(smoothedX)
  #print(smoothedY)
  output =""
  output += "<MouseMovementEvent>\r\n" +"	<Type>3</Type>\r\n" +"	  <X>" + str(smoothedX[0]) + "</X>\r\n" +"          <Y>" + str(smoothedY[0]) + "</Y>\r\n" + "          <Delay>"+ str(0) + "</Delay>\r\n" +"</MouseMovementEvent>\r\n"


  for k in range(1,len(smoothedX)):
    if (k%(smoothFactor+1)) == 1:
      output += "<MouseMovementEvent>\r\n" +"	<Type>3</Type>\r\n" +"	  <X>" + str(smoothedX[k]) + "</X>\r\n" + "          <Y>" + str(smoothedY[k]) + "</Y>\r\n" + "          <Delay>"+ str(int(((delay/(smoothFactor+1)) + (delay%(smoothFactor+1))))) + "</Delay>\r\n" +"</MouseMovementEvent>\r\n"
    else:
      output +="<MouseMovementEvent>\r\n" +"	<Type>3</Type>\r\n" +"	  <X>" + str(smoothedX[k]) + "</X>\r\n" + "          <Y>" + str(smoothedY[k]) + "</Y>\r\n" + "          <Delay>"+ str(int(delay/(smoothFactor+1))) + "</Delay>\r\n" +"</MouseMovementEvent>\r\n"
  return output



def convertList(recoilPointList, current):
  converted = [len(recoilPointList)]
  converted[0] = current
  for k in recoilPointList:
    current += k #add the recoil
    converted.append(current)
  
  return converted

def smoothing(mousePositionList,smooth):
  smoothedList = []
  smoothedList.append(mousePositionList[0])

  for k in range(0,len(mousePositionList)-1):
    before = mousePositionList[k]
    after = mousePositionList[k+1]
    difference = before-after

    for i in range(0,smooth):
      smoothedList.append(int(round(
        smoothedList[-1] - (difference/(smooth+1))
      )))
    smoothedList.append(after)
  return smoothedList


def XMLprintEnd():
  return "</MouseMovement>\r\n" + "    </MacroEvent>\r\n" + "    <MacroEvent>\r\n" + "      <Type>2</Type>\r\n" + "      <Delay>2</Delay>\r\n" + "      <MouseEvent>\r\n" + "        <MouseButton>1</MouseButton>\r\n" + "        <State>1</State>\r\n" + "      </MouseEvent>\r\n" + "    </MacroEvent>\r\n" + "  </MacroEvents>\r\n" + "</Macro>"


userInput()

