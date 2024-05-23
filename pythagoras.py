import math

bodA = [4,2]
bodB = [7,6]

vzdalenost = math.sqrt( (( bodA[0] - bodB[0])**2) + (( bodA[1] - bodB[1])**2) )
print("Vzdalenost mezi body A a B je: ", str(vzdalenost))