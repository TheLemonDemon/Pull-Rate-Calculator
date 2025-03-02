pack = input("Are you opening up Genetic Apex (G), Space-Time Smackdown (S), or Triumphant Light (T)?\n")
commonNum = input("How many One diamonds do you need?\n")
uncommonNum = input("How many Two diamonds do you need?\n")
holoNum = input("How many Three diamonds do you need?\n")
exNum = input("How many Four diamonds do you need?\n")

if pack.upper() == "G":
    CCOdds = .02

    FCOddsU = .02571
    FCOddsH = .00357
    FCOddsE = .00333

    SCOddsU = .01714
    SCOddsH = .01428
    SCOddsE = .01332

elif pack.upper() == "S":
    CCOdds = .02272
    
    FCOddsU = .02647
    FCOddsH = .00357
    FCOddsE = .00333

    SCOddsU = .01764
    SCOddsH = .01428
    SCOddsE = .01332

elif pack.upper() == "T":
    CCOdds = .03225
    
    FCOddsU = .03461
    FCOddsH = .00384
    FCOddsE = .00333

    SCOddsU = .02307
    SCOddsH = .01538
    SCOddsE = .01332



commonCard = 1- (float(commonNum)*CCOdds)
firstCard = 1 - (float(uncommonNum)*FCOddsU + float(holoNum)*FCOddsH + float(exNum)*FCOddsE)
secondCard = 1 - (float(uncommonNum)*SCOddsU + float(holoNum)*SCOddsH + float(exNum)*SCOddsE)

trueOdds = 100*(1- (firstCard*secondCard*commonCard*commonCard*commonCard))

print("The odds of you getting a new card from that pack is " + str(round(trueOdds, 3))+ "%")