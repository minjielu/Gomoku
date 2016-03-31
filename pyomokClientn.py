#!/usr/bin/python3
import random
import socket
import math
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

def Price(OValue):
    return {
	0: 0,
        1: 2,
        2: 5,
        3: 11,
        4: 23,
        5: 1000,
        6: 1000,
	7: 0,
	8: 0,
        }[OValue]

def DPrice(OValue):
    return {
	0: 0,
	1: 1,
	2: 4,
	3: 20,
	4: 900,
	5: 950,
        6: 950,
	}[OValue]


def Bonus(OValue):
   return {
	0: 0,
	1: 0,
	2: 2,
	3: 4,
	4: 800,
	5: 16,
        6: 100,
	}[OValue]

def DBonus(OValue):
    return {
	0: 0,
	1: 0,
	2: 2,
	3: 700,
	4: 8,
	5: 16,
        6: 20,
	}[OValue]
        
def ChangeRange(NewHori, NewVert):
    global Lem, Rim, Upm, Lom
    if (NewHori <= Lem):
        Lem = NewHori
    if (NewHori >= Rim):
        Rim = NewHori
    if (NewVert <= Upm):
        Upm = NewVert
    if (NewVert >= Lom):
        Lom = NewVert

def EndCheck(i, j, Side):
    global Position
    UL, LL, LR, UR, L, R, U, D = 1, 1, 1, 1, 1, 1, 1, 1
    for p in range(1, min(6, i+1, j+1)):
        if Position[i-p][j-p] != Side and Position[i-p][j-p] != Side-2:
            UL = p
            break
    for q in range(1, min(6, 17-i, 17-j)):
        if Position[i+q][j+q] != Side and Position[i+q][j+q] != Side-2:
            LR = q
            break
    for p in range(1, min(6, i+1, 17-j)):
        if Position[i-p][j+p] != Side and Position[i-p][j+p] != Side-2:
            LL = p
            break
    for q in range(1, min(6, 17-i, j+1)):
        if Position[i+q][j-q] != Side and Position[i+q][j-q] != Side-2:
            UR = q
            break
    for p in range(1, min(6, i+1)):
        if Position[i-p][j] != Side and Position[i-p][j] != Side-2:
            L = p
            break
    for q in range(1, min(6, 17-i)):
        if Position[i+q][j] != Side and Position[i+q][j] != Side-2:
            R = q
            break

    for p in range(1, min(6, 17-j)):
        if Position[i][j+p] != Side and Position[i][j+p] != Side-2:
            U = p
            break
    for q in range(1, min(6, j+1)):
        if Position[i][j-q] != Side and Position[i][j-q] != Side-2:
            D = q
            break
    if UL+LR-1 == 5 or UR+LL-1 == 5 or L+R-1 == 5 or U+D-1 == 5:
        return 1
    else:
	return 0 	


def BestMove():
    global FirstAnalyze, Lem, Rim, Upm, Lom, Self, Depth, Position, AnalyzeNumber, FirstVisit
    v = -10000
    Hori, Vert = -1, -1
    Depth = 0
    Number = 0
    BestPoints = [[0] * 4 for i in range(225)]
    #Measure = -10000
    FirstVisit = 1
    #BestPoint = []
    Alpha = -10000
    for i in range(max(1, Lem-2),min(16, Rim+3)):
	for j in range(max(1, Upm-2),min(16, Lom+3)):
	    if Position[i][j] != 1 and Position[i][j] != 2:
		BestPoints[Number][0] = i
		BestPoints[Number][1] = j
		BestPoints[Number][2], BestPoints[Number][3] = Evalp(i, j,  Self)
		Number += 1
    BestPoints = sorted(BestPoints, key=lambda x:x[2], reverse = True)
    #Position[BestPoint[0]][BestPoint[1]] = Self
    #RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
    #ChangeRange(BestPoint[0], BestPoint[1])
    #v = OpponentBest(-10000, +10000)
    #Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
    #Position[BestPoint[0]][BestPoint[1]] = 0
    #for i in range(max(1, Lem-2),min(16, Rim+3)):
	    #for j in range(max(1, Upm-2),min(16, Lom+3)):
	        #if Position[i][j] != 1 and Position[i][j] != 2 and i != BestPoint[0] and j != BestPoint[1]:
		    #Number += 1
		    #temv = Evalp(i, j, Self)
		    #if Number <= AnalyzeNumber:
			#BestPoints.append(temv)
		    #elif Number == AnalyzeNumber+1:
			#BestPoints.sort()
		    #if temv > BestPoints[0]:
			#BestPoints[0] == temv
			#BestPoints.sort()
		        #if temv >= 1000:
			    #return i, j
    for i in range(FirstAnalyze):
	if BestPoints[i][0] == -2:
	    break
	if BestPoints[i][3] == 1:
            return BestPoints[i][0], BestPoints[i][1]
        Position[BestPoints[i][0]][BestPoints[i][1]] = Self
        RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
        ChangeRange(BestPoints[i][0],BestPoints[i][1])
        b = OpponentBest(Alpha, +10000)
        Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
        Position[BestPoints[i][0]][BestPoints[i][1]] = 0
        if v < b:
            v, Alpha = b, b
            Hori, Vert = BestPoints[i][0], BestPoints[i][1]
        elif v == b:
	    probe = random.random()
	    if probe < 0.4:
	        v = b
	        Hori, Vert = BestPoints[i][0], BestPoints[i][1]
    print v
    return Hori, Vert 

def SelfBest(Alpha, Beta):
    global Lem, Rim, Upm, Lom, Self, MaxDepth, Depth, Position, AnalyzeNumber, FirstVisit
    Depth += 1
    Number = 0
    BestPoints = [[-2] * 4 for i in range(225)]
    #BestPoint = []
    #BestPoint.append(0)
    #BestPoint.append(0)
    #Measure = -10000
    if Depth >= MaxDepth:
        #FirstVisit = 0
	Depth -= 1
        return Eval()
    v = -10000
    #if FirstVisit == 1:
    for i in range(max(1, Lem-2),min(16, Rim+3)):
	for j in range(max(1, Upm-2),min(16, Lom+3)):
	    if Position[i][j] != 1 and Position[i][j] != 2 and Position[i][j] != 3 and Position[i][j] != 4:
		BestPoints[Number][0] = i
		BestPoints[Number][1] = j
		BestPoints[Number][2], BestPoints[Number][3] = Evalp(i, j, Self)
		Number += 1
    BestPoints = sorted(BestPoints, key=lambda x:x[2], reverse = True)
        #Position[BestPoint[0]][BestPoint[1]] = Self
        #RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
        #ChangeRange(BestPoint[0], BestPoint[1])
        #v = OpponentBest(-10000, +10000)
        #Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
        #Position[BestPoint[0]][BestPoint[1]] = 0
    for i in range(AnalyzeNumber):
                #Number += 1
		#temv = Evalp(i, j, Self)
		#if Number <= AnalyzeNumber:
	            #BestPoints.append(temv)
		#elif Number == AnalyzeNumber+1:
		    #BestPoints.sort()
		#if temv > BestPoints[0]:
		    #BestPoints[0] == temv
		    #BestPoints.sort()
                    #if temv >= 1000:
		        #Depth -= 1
		        #return 9000
        if BestPoints[i][3] == 1:
	    Depth -= 1
	    return 9000
        Position[BestPoints[i][0]][BestPoints[i][1]] = Self 
    	RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
    	ChangeRange(BestPoints[i][0], BestPoints[i][1])
    	v = max(v, OpponentBest(Alpha, Beta))
    	Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
    	Position[BestPoints[i][0]][BestPoints[i][1]] = 0
    	if v >= Beta:
            Depth -= 1
    	    return v
    	    Alpha = max(Alpha, v)
    Depth -= 1
    return v

def OpponentBest(Alpha, Beta):
    global Lem, Rim, Upm, Lom, Opponent, MaxDepth, Depth, Position, AnalyzeNumber, FirstVisit, FirstAnalyze
    OpponentAnalyze = AnalyzeNumber
    Depth += 1
    Number = 0
    BestPoints = [[0] * 4 for i in range(225)]
    #BestPoint = []
    #BestPoint.append(0)
    #BestPoint.append(0)
    #Measure = -10000
    if Depth >= MaxDepth:
        #FirstVisit = 1
        Depth -=1
        return Eval()
    v = 10000
    #if FirstVisit == 1:
    for i in range(max(1, Lem-2),min(16, Rim+3)):
	for j in range(max(1, Upm-2),min(16, Lom+3)):
	    if Position[i][j] != 1 and Position[i][j] != 2 and Position[i][j] !=3 and Position[i][j] !=4:
		BestPoints[Number][0] = i
		BestPoints[Number][1] = j
	        BestPoints[Number][2], BestPoints[Number][3] = Evalp(i,j, Opponent)
		Number += 1
    BestPoints = sorted(BestPoints, key=lambda x:x[2], reverse = True)
        #Position[BestPoint[0]][BestPoint[1]] = Self
        #RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
        #ChangeRange(BestPoint[0], BestPoint[1])
        #v = OpponentBest(-10000, +10000)
        #Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
        #Position[BestPoint[0]][BestPoint[1]] = 0
    if FirstVisit == 1:
        OpponentAnalyze = FirstAnalyze
        FirstVisit = 0
    for i in range(OpponentAnalyze):
                #Number += 1
		#temv = Evalp(i, j, Opponent)
		#if Number <= AnalyzeNumber:
	            #BestPoints.append(temv)
		#elif Number == AnalyzeNumber+1:
		    #BestPoints.sort()
		#if Number > AnalyzeNumber and temv > BestPoints[0]:
		    #BestPoints[0] == temv
		    #BestPoints.sort()		
		    #if temv >= 1000:
		        #Depth -= 1
		        #return -9000
	if BestPoints[i][0] == -2:
	    break
	if BestPoints[i][3] == 1:
            Depth -= 1
	    return -9000	
        Position[BestPoints[i][0]][BestPoints[i][1]] = Opponent 
    	RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
    	ChangeRange(BestPoints[i][0], BestPoints[i][1])
    	v = min(v, SelfBest(Alpha, Beta))
    	Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
    	Position[BestPoints[i][0]][BestPoints[i][1]] = 0
    	if v <= Alpha:
  	    Depth -= 1
    	    return v
    	Beta = min(Beta, v)
    Depth -= 1
    return v

def Evalp(i, j, Self):
    Value = 0
    UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, End = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0
    if Self == 3:
	Opponent = 4
    else: 
        Opponent = 3
    for p in range(1, min(6, i+1, j+1)):
	if Position[i-p][j-p] != Self and Position[i-p][j-p] != Self-2:
            UL = p
	    break
    for q in range(1, min(6, 17-i, 17-j)):
        if Position[i+q][j+q] != Self and Position[i+q][j+q] != Self-2:
	    LR = q
	    break
    if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
        if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
	    Up1 = Bonus(UL+LR-1)
    Value = Value + Price(UL+LR-1) + Up1

    for p in range(1, min(6, i+1, 17-j)):
        if Position[i-p][j+p] != Self and Position[i-p][j+p] != Self-2:
	    LL = p
	    break
    for q in range(1, min(6, 17-i, j+1)):
        if Position[i+q][j-q] != Self and Position[i+q][j-q] != Self-2:
	    UR = q
	    break
    if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
	if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
	    Up2 = Bonus(LL+UR-1)
    Value = Value + Price(LL+UR-1) + Up2

    for p in range(1, min(6, i+1)):
        if Position[i-p][j] != Self and Position[i-p][j] != Self-2:
	    L = p
	    break
    for q in range(1, min(6, 17-i)):
        if Position[i+q][j] != Self and Position[i+q][j] != Self-2:
	    R = q
	    break
    if i-L >= 1 and i+R <=15:
	if Position[i-L][j] == 0 and Position[i+R][j] == 0:
	    Up3 = Bonus(L+R-1)
    Value = Value + Price(L+R-1) + Up3

    for p in range(1, min(6, 17-j)):
	if Position[i][j+p] != Self and Position[i][j+p] != Self-2:
            U = p
	    break
    for q in range(1, min(6, j-1)):
	if Position[i][j-q] != Self and Position[i][j-q] != Self-2:
            D = q
	    break
    if j+U <= 15 and j-D >= 1:
	if Position[i][j+U] == 0 and Position[i][j-D] == 0:
  	    Up4 = Bonus(U+D-1)
    Value = Value + Price(U+D-1) + Up4
    if UL+LR >= 6 or LL+UR >= 6 or U+D >= 6 or L+R >= 6:
        End = 1

	# Evaluate the value of our defense
    UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4 = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0
    for p in range(1, min(7, i+1, j+1)):
        if Position[i-p][j-p] != Opponent and Position[i-p][j-p] != Opponent-2:
	    UL = p
	    break

    for q in range(1, min(7, 17-i, 17-j)):
        if Position[i+q][j+q] != Opponent and Position[i+q][j+q] != Opponent-2:
	    LR = q
	    break
    if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
        if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
	    Up1 = DBonus(UL+LR-2)
    Value = Value + DPrice(UL+LR-2)+Up1

    for p in range(1, min(7, i+1, 17-j)):
        if Position[i-p][j+p] != Opponent and Position[i-p][j+p] != Opponent-2:
	    LL = p
	    break
    for q in range(1, min(7, 17-i, j+1)):
        if Position[i+q][j-q] != Opponent and Position[i+q][j-q] != Opponent-2:
	    UR = q
	    break
    if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
        if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
	    Up2 = DBonus(LL+UR-2)
    Value = Value + DPrice(LL+UR-2)+Up2

    for p in range(1, min(7, i+1)):
        if Position[i-p][j] != Opponent and Position[i-p][j] != Opponent-2:
	    L = p
	    break
    for q in range(1, min(7, 17-i)):
        if Position[i+q][j] != Opponent and Position[i+q][j] != Opponent-2:
	    R = q
	    break
    if i-L >= 1 and i+R <=15:
        if Position[i-L][j] == 0 and Position[i+R][j] == 0:
 	    Up3 = DBonus(L+R-2)
    Value = Value + DPrice(L+R-2)+Up3

    for p in range(1, min(7, 17-j)):
        if Position[i][j+p] != Opponent and Position[i][j+p] != Opponent-2:
	    U = p
	    break
    for q in range(1, min(7, j+1)):
        if Position[i][j-q] != Opponent and Position[i][j-q] != Opponent-2:
	    D = q
	    break
    if j+U <= 15 and j-D >= 1:
        if Position[i][j+U] == 0 and Position[i][j-D] == 0:
	    Up4 = DBonus(U+D-2)
    Value = Value + DPrice(U+D-2)+Up4
    return Value, End
    
def Eval():
    global Lem, Rim, Upm, Lom, Opponent, Self
    Value = 0
    UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, BUR, BUL, BLL, BLR, BL, BR, BU, BD = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(Lem, Rim+1):
        for j in range(Upm, Lom+1):
            if Position[i][j] == Self:
            # Evaluate the value of our attack

                for p in range(1, min(6, i+1, j+1)):
                    if Position[i-p][j-p] != Self and Position[i-p][j-p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BUL == 0:
#			    BUL = -1
#			    continue
      			UL = p
                        break
                for q in range(1, min(6, 17-i, 17-j)):
                    if Position[i+q][j+q] != Self and Position[i+q][j+q] != Self-2:
#                        if Position[i-q][j-q] == 0 and BLR == 0:
#			    BLR = -1
#			    continue                        
			LR = q
                        break
		if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
		    if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
		        Up1 = Bonus(UL+LR-1)
                Value = Value + Price(UL+LR-1+BUL+BLR) + Up1
                
                for p in range(1, min(6, i+1, 17-j)):
                    if Position[i-p][j+p] != Self and Position[i-p][j+p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BLL == 0:
#			    BLL = -1
#			    continue
                        LL = p
                        break
                for q in range(1, min(6, 17-i, j+1)):
                    if Position[i+q][j-q] != Self and Position[i+q][j-q] != Self-2:
 #                       if Position[i-q][j-q] == 0 and BUR == 0:
#			    BUR = -1
#			    continue
                        UR = q
                        break
		if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
		    if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
		        Up2 = Bonus(LL+UR-1)
                Value = Value + Price(LL+UR-1+BUR+BLL) + Up2
                
                for p in range(1, min(6, i+1)):
                    if Position[i-p][j] != Self and Position[i-p][j] != Self-2:
#                        if Position[i-p][j-p] == 0 and BL == 0:
#			    BL = -1
#			    continue
                        L = p
                        break
                for q in range(1, min(6, 17-i)):
                    if Position[i+q][j] != Self and Position[i+q][j] != Self-2:
 #                       if Position[i-q][j-q] == 0 and BR == 0:
#			    BR = -1
#			    continue
                        R = q
                        break
		if i-L >= 1 and i+R <=15:
		    if Position[i-L][j] == 0 and Position[i+R][j] == 0:
		        Up3 = Bonus(L+R-1)
                Value = Value + Price(L+R-1+BL+BR) + Up3
                
                for p in range(1, min(6, 17-j)):
                    if Position[i][j+p] != Self and Position[i][j+p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BU == 0:
#			    BU = -1
#			    continue
                        U = p
                        break
                for q in range(1, min(6, j-1)):
                    if Position[i][j-q] != Self and Position[i][j-q] != Self-2:
#                        if Position[i-q][j-q] == 0 and BD == 0:
#			    BD = -1
#			    continue
                        D = q
                        break
		if j+U <= 15 and j-D >= 1:
		    if Position[i][j+U] == 0 and Position[i][j-D] == 0:
		        Up4 = Bonus(U+D-1)
                Value = Value + Price(U+D-1+BU+BD) + Up4
		
		# Evaluate the value of our defense
                UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, BUR, BUL, BLL, BLR, BL, BR, BU, BD = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
		for p in range(1, min(7, i+1, j+1)):
                    if Position[i-p][j-p] != Opponent and Position[i-p][j-p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BUL == 0:
#			    BUL = -1
#			    continue
                        UL = p
                        break
			
                for q in range(1, min(7, 17-i, 17-j)):
                    if Position[i+q][j+q] != Opponent and Position[i+q][j+q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BLR == 0:
#			    BLR = -1
#			    continue
                        LR = q
                        break
		if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
		    if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
		        Up1 = DBonus(UL+LR-2)
                Value = Value + DPrice(UL+LR-2+BUL+BLR)+Up1
                
                for p in range(1, min(7, i+1, 17-j)):
                    if Position[i-p][j+p] != Opponent and Position[i-p][j+p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BLL == 0:
#			    BLL = -1
#			    continue
                        LL = p
                        break
                for q in range(1, min(7, 17-i, j+1)):
                    if Position[i+q][j-q] != Opponent and Position[i+q][j-q] != Opponent-2:
 #                       if Position[i-q][j-q] == 0 and BUR == 0:
#			    BUR = -1
#			    continue
                        UR = q
                        break
		if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
		    if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
		        Up2 = DBonus(LL+UR-2)
                Value = Value + DPrice(LL+UR-2+BLL+BUR)+Up2
                
                for p in range(1, min(7, i+1)):
                    if Position[i-p][j] != Opponent and Position[i-p][j] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BL == 0:
#			    BL = -1
#			    continue
                        L = p
                        break
                for q in range(1, min(7, 17-i)):
                    if Position[i+q][j] != Opponent and Position[i+q][j] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BR == 0:
#			    BR = -1
#			    continue
                        R = q
                        break
		if i-L >= 1 and i+R <=15:
		    if Position[i-L][j] == 0 and Position[i+R][j] == 0:
		        Up3 = DBonus(L+R-2)
                Value = Value + DPrice(L+R-2+BL+BR)+Up3
                
                for p in range(1, min(7, 17-j)):
                    if Position[i][j+p] != Opponent and Position[i][j+p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BU == 0:
#			    BU = -1
#			    continue
                        U = p
                        break
                for q in range(1, min(7, j+1)):
                    if Position[i][j-q] != Opponent and Position[i][j-q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BD == 0:
#			    BD = -1
#			    continue
                        D = q
                        break
		if j+U <= 15 and j-D >= 1:
		    if Position[i][j+U] == 0 and Position[i][j-D] == 0:
		        Up4 = DBonus(U+D-2)
                Value = Value + DPrice(U+D-2+BU+BD)+Up4
		     
                
    for i in range(Lem, Rim+1):
        for j in range(Upm, Lom+1):
            if Position[i][j] == Opponent:
		#Evaluate the value of opponent's attack
                UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, BUR, BUL, BLL, BLR, BL, BR, BU, BD = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                for p in range(1, min(6, i+1, j+1)):
                    if Position[i-p][j-p] != Opponent and Position[i-p][j-p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BUL == 0:
#			    BUL = -1
#			    continue
                        UL = p
                        break
                for q in range(1, min(6, 17-i, 17-j)):
                    if Position[i+q][j+q] != Opponent and Position[i+q][j+q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BLR == 0:
#			    BLR = -1
#			    continue
                        LR = q
                        break
		if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
		    if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
		        Up1 = Bonus(UL+LR-1)
                Value = Value - Price(UL+LR-1+BUL+BLR) - Up1
                
                for p in range(1, min(6, i+1, 17-j)):
                    if Position[i-p][j+p] != Opponent and Position[i-p][j+p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BLL == 0:
#			    BLL = -1
#			    continue
                        LL = p
                        break
                for q in range(1, min(6, 17-i, j+1)):
                    if Position[i+q][j-q] != Opponent and Position[i+q][j-q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BUR == 0:
#			    BUR = -1
#			    continue
                        UR = q
                        break
		if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
		    if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
		        Up2 = Bonus(LL+UR-1)
                Value = Value - Price(LL+UR-1+BLL+BUR) - Up2
                
                for p in range(1, min(6, i+1)):
                    if Position[i-p][j] != Opponent and Position[i-p][j] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BL == 0:
#			    BL = -1
#			    continue
                        L = p
                        break
                for q in range(1, min(6, 17-i)):
                    if Position[i+q][j] != Opponent and Position[i+q][j] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BR == 0:
#			    BR = -1
#			    continue
                        R = q
                        break
		if i-L >= 1 and i+R <=15:
		    if Position[i-L][j] == 0 and Position[i+R][j] == 0:
		        Up3 = Bonus(L+R-1)
                Value = Value - Price(L+R-1+BL+BR) - Up3
                
                for p in range(1, min(6, 17-j)):
                    if Position[i][j+p] != Opponent and Position[i][j+p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BU == 0:
#			    BU = -1
#			    continue
                        U = p
                        break
                for q in range(1, min(6, j+1)):
                    if Position[i][j-q] != Opponent and Position[i][j-q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BD == 0:
#			    BD = -1
#			    continue
                        D = q
                        break
		if j+U <= 15 and j-D >= 1:
		    if Position[i][j+U] == 0 and Position[i][j-D] == 0:
		        Up4 = Bonus(U+D-1)
                Value = Value - Price(U+D-1+BU+BD) -Up4
                
		# Evaluate the value of our opponent's defense
                UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, BUR, BUL, BLL, BLR, BL, BR, BU, BD = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
		for p in range(1, min(7, i+1, j+1)):
                    if Position[i-p][j-p] != Self and Position[i-p][j-p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BUL == 0:
#			    BUL = -1
#			    continue
                        UL = p
                        break
                for q in range(1, min(7, 17-i, 17-j)):
                    if Position[i+q][j+q] != Self and Position[i+q][j+q] != Self-2:
#                        if Position[i-q][j-q] == 0 and BLR == 0:
#			    BLR = -1
#			    continue
                        LR = q
                        break
		if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
		    if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
		        Up1 = DBonus(UL+LR-2)
                Value = Value + DPrice(UL+LR-2+BUL+BLR)+Up1
                
                for p in range(1, min(7, i+1, 17-j)):
                    if Position[i-p][j+p] != Self and Position[i-p][j+p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BLL == 0:
#			    BLL = -1
#			    continue
                        LL = p
                        break
                for q in range(1, min(7, i+1, j+1)):
                    if Position[i+q][j-q] != Self and Position[i+q][j-q] != Self-2:
#                        if Position[i-q][j-q] == 0 and BUR == 0:
#			    BUR = -1
#			    continue
                        UR = q
                        break
		if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
		    if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
		        Up2 = DBonus(LL+UR-2)
                Value = Value + DPrice(LL+UR-2+BLL+BUR)+Up2
                
                for p in range(1, min(7, i+1)):
                    if Position[i-p][j] != Self and Position[i-p][j] != Self-2:
#                        if Position[i-p][j-p] == 0 and BL == 0:
#			    BL = -1
#			    continue
                        L = p
                        break
                for q in range(1, min(7, 17-i)):
                    if Position[i+q][j] != Self and Position[i+q][j] != Self-2:
#                        if Position[i-q][j-q] == 0 and BR == 0:
#			    BR = -1
#			    continue
                        R = q
                        break
		if i-L >= 1 and i+R <=15:
		    if Position[i-L][j] == 0 and Position[i+R][j] == 0:
		        Up3 = DBonus(L+R-2)
                Value = Value + DPrice(L+R-2+BL+BR)+Up3
                
                for p in range(1, min(7, 17-j)):
                    if Position[i][j+p] != Self and Position[i][j+p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BU == 0:
#			    BU = -1
#			    continue
                        U = p
                        break
                for q in range(1, min(7, j+1)):
                    if Position[i][j-q] != Self and Position[i][j-q] != Self-2:
#                        if Position[i-q][j-q] == 0 and BD == 0:
#			    BD = -1
#			    continue
                        D = q
                        break
		if j+U <= 15 and j-D >= 1:
		    if Position[i][j+U] == 0 and Position[i][j-D] == 0:
		        Up4 = DBonus(U+D-2)
                Value = Value + DPrice(U+D-2+BU+BD)+Up4
    return Value
    
    

Depth, MaxDepth, FirstVisit, FirstAnalyze, BlackFirstMove = 0, 8, 1, 35, 1
AnalyzeNumber = 3
Position = [[0] * 17 for i in range(17)]
Upm, Lom, Lem, Rim = 17, -2, 17, -2
while (1):
    data = client_socket.recv(512)
    data = data.decode() # convert bytes to a string
    for s in data.split('\n'):
        if len(s) == 0: continue
        print ("\t"+s)
        if (s[0:3] == 'WIN'):
            client_socket.close()
            exit(1)
        elif (s[0:7] == 'WELCOME'):
	    if 'WHITE' in s:
	        Self, Opponent = 4, 3
	    else:
	        Self, Opponent = 3, 4 
        elif (s[0:5] == 'ENTER'):
            # Our move, generate a random pair
	    if Self == 3 and BlackFirstMove == 1:
		dataSend = "8,8\n"
		BlackFirstMove = 0
	    else:
                x,y =  BestMove()
                dataSend = "%d,%d\n" % (x,y)
            #print("Making a move = `"+ dataSend + "'")
            client_socket.send(dataSend.encode())
        elif (s[0:10] == 'VALID_MOVE'):
            Doll = s.split(' ')[1].split(',')
            if (Doll[0] == 'BLACK'):
                Position[int(Doll[1])][int(Doll[2])] = 1 # 1 means black
            elif (Doll[0] == 'WHITE'):
	        Position[int(Doll[1])][int(Doll[2])] = 2 # 2 means white
	    ChangeRange(int(Doll[1]), int(Doll[2]))	    
