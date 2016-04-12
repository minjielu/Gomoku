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
        5: 1500,
        6: 1500,
	7: 1500,
	8: 1500,
        }[OValue]

def DPrice(OValue):
    return {
	0: 0,
	1: 3,
	2: 6,
	3: 10,
	4: 1400,
	5: 1450,
        6: 950,
	7: 950,
	8: 950
	}[OValue]


def Bonus(OValue):
   return {
	0: 0,
	1: 0,
	2: 2,
	3: 20,
	4: 800,
	5: 800,
        6: 800,
	7: 800,
	8: 800,
	}[OValue]

def DBonus(OValue):
    return {
	0: 0,
	1: 0,
	2: 3,
	3: 700,
	4: 700,
	5: 700,
        6: 700,
	7: 700,
	8: 700,
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
    global FirstAnalyze, Lem, Rim, Upm, Lom, Self, Depth, Position, AnalyzeNumber, FirstVisit, AcMaxDepth, OpponentWin, FastWin
    SWinDepth, OWinDepth, SWinDepth= 50, 0, 30
    FastWin = [-2, -2]
    OpponentWin = [-2, -2]
    AcAnalyzeNumber = FirstAnalyze 
    AcMaxDepth = MaxDepth
    v = -30000
    Hori, Vert = -1, -1
    Depth = 0
    Number = 0
    BestPoints = [[-2] * 4 for i in range(225)]
    #Measure = -10000
    #BestPoint = []
    Alpha = -30001
    for i in range(max(1, Lem-2),min(16, Rim+3)):
	for j in range(max(1, Upm-2),min(16, Lom+3)):
	    if Position[i][j] != 1 and Position[i][j] != 2:
		BestPoints[Number][0] = i
		BestPoints[Number][1] = j
		BestPoints[Number][2], BestPoints[Number][3] = Evalp(i, j,  Self)
		Number += 1
    BestPoints = sorted(BestPoints, key=lambda x:x[2], reverse = True)
    if BestPoints[0][2] >= 1400:
        AcAnalyzeNumber = 1
        AcMaxDepth += 1
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
    for i in range(AcAnalyzeNumber):
	if BestPoints[i][0] == -2:
	    break
	if BestPoints[i][3] == 1:
            return BestPoints[i][0], BestPoints[i][1]
        Position[BestPoints[i][0]][BestPoints[i][1]] = Self
        RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
        ChangeRange(BestPoints[i][0],BestPoints[i][1])
	FirstVisit= 1
        b, CWinDepth, CLoseDepth = OpponentBest(Alpha, +30001)
	if b == 29000:
	    if SWinDepth > CWinDepth:
		SWinDepth, FastWin[0], FastWin[1] = CWinDepth, BestPoints[i][0], BestPoints[i][1]
	if b == -29000:
            if OWinDepth < CLoseDepth:
		OWinDepth, OpponentWin[0], OpponentWin[1] = CLoseDepth, BestPoints[i][0], BestPoints[i][1]
        Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
        Position[BestPoints[i][0]][BestPoints[i][1]] = 0
	if v < b:
            v, Alpha = b, b
            Hori, Vert = BestPoints[i][0], BestPoints[i][1]
        elif v == b:
	    probe = random.random()
	    if probe < 0.4:
	        Hori, Vert = BestPoints[i][0], BestPoints[i][1]
    if v == -29000:
	for i in range(AcAnalyzeNumber, 20):
	    if BestPoints[i][2] <= 0:
		break
	    FirstVisit= 1
            Position[BestPoints[i][0]][BestPoints[i][1]] = Self
            RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
            ChangeRange(BestPoints[i][0],BestPoints[i][1])
            b, CWinDepth, CLoseDepth = OpponentBest(Alpha, +30001)
	    if b == 29000:
	        if SWinDepth > CWinDepth:
		    SWinDepth, FastWin[0], FastWin[1] = CWinDepth, BestPoints[i][0], BestPoints[i][1]
	    if b == -29000:
		if OWinDepth < CLoseDepth:
		    OWinDepth, OpponentWin[0], OpponentWin[1] = CLoseDepth, BestPoints[i][0], BestPoints[i][1]
            Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
            Position[BestPoints[i][0]][BestPoints[i][1]] = 0
	    if b > -29000:
		print b
		return BestPoints[i][0], BestPoints[i][1]  
    print v
    if v == -29000:
	print OpponentWin[0], OpponentWin[1], OWinDepth
	return OpponentWin[0], OpponentWin[1]
    if v == 29000:
	print FastWin[0], FastWin[1], SWinDepth
	return FastWin[0], FastWin[1]
    return Hori, Vert 

def SelfBest(Alpha, Beta):
    global Lem, Rim, Upm, Lom, Self, MaxDepth, Depth, Position, AnalyzeNumber, FirstVisit, AcMaxDepth
    AcAnalyzeNumber = AnalyzeNumber
    Depth += 1
    Number = 0
    BestPoints = [[-2] * 4 for i in range(225)]
    #BestPoint = []
    #BestPoint.append(0)
    #BestPoint.append(0)
    #Measure = -10000
    if Depth >= AcMaxDepth:
        #FirstVisit = 0
	Depth -= 1
        return Eval(), 30, 30
    v, WinDepth, LoseDepth = -30000, 30, 0
    #if FirstVisit == 1:
    for i in range(max(1, Lem-2),min(16, Rim+3)):
	for j in range(max(1, Upm-2),min(16, Lom+3)):
	    if Position[i][j] != 1 and Position[i][j] != 2 and Position[i][j] != 3 and Position[i][j] != 4:
		BestPoints[Number][0] = i
		BestPoints[Number][1] = j
		BestPoints[Number][2], BestPoints[Number][3] = Evalp(i, j, Self)
		Number += 1
    BestPoints = sorted(BestPoints, key=lambda x:x[2], reverse = True)
    if BestPoints[0][2] >= 1400:
	AcMaxDepth += 1
	AcAnalyzeNumber = 1
        #Position[BestPoint[0]][BestPoint[1]] = Self
        #RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
        #ChangeRange(BestPoint[0], BestPoint[1])
        #v = OpponentBest(-10000, +10000)
        #Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
        #Position[BestPoint[0]][BestPoint[1]] = 0
    for i in range(AcAnalyzeNumber):
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
	    if AcAnalyzeNumber == 1:
		AcMaxDepth -= 1
	    Depth -= 1
	    return 29000, Depth+1, 30
        Position[BestPoints[i][0]][BestPoints[i][1]] = Self 
    	RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
    	ChangeRange(BestPoints[i][0], BestPoints[i][1])
	Cvalue, CWinDepth, CLoseDepth = OpponentBest(Alpha, Beta)
    	v = max(v, Cvalue)
	WinDepth = min(WinDepth,CWinDepth) 
	LoseDepth = max(LoseDepth,CLoseDepth) 
    	Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
    	Position[BestPoints[i][0]][BestPoints[i][1]] = 0
    	if v > Beta:
	    if AcAnalyzeNumber == 1:
		AcMaxDepth -= 1
            Depth -= 1
    	    return v, WinDepth, LoseDepth
    	Alpha = max(Alpha, v)
    if AcAnalyzeNumber == 1:
        AcMaxDepth -= 1
    Depth -= 1
    return v, WinDepth, LoseDepth

def OpponentBest(Alpha, Beta):
    global Lem, Rim, Upm, Lom, Opponent, MaxDepth, Depth, Position, AnalyzeNumber, FirstVisit, AcMaxDepth, OpponentFirstAnalyze
    AcAnalyzeNumber = AnalyzeNumber
    Doit = 0
    if FirstVisit == 1:
	FirstVisit, Doit, AcAnalyzeNumber = 0, 1, OpponentFirstAnalyze
    Depth += 1
    Number = 0
    BestPoints = [[-2] * 4 for i in range(225)]
    #BestPoint = []
    #BestPoint.append(0)
    #BestPoint.append(0)
    #Measure = -10000
    if Depth >= AcMaxDepth:
        #FirstVisit = 1
        Depth -=1
        return Eval(), 30, 30
    v, WinDepth, LoseDepth = 30000, 0, 30
    #if FirstVisit == 1:
    for i in range(max(1, Lem-2),min(16, Rim+3)):
	for j in range(max(1, Upm-2),min(16, Lom+3)):
	    if Position[i][j] != 1 and Position[i][j] != 2 and Position[i][j] !=3 and Position[i][j] !=4:
		BestPoints[Number][0] = i
		BestPoints[Number][1] = j
	        BestPoints[Number][2], BestPoints[Number][3] = Evalp(i,j, Opponent)
		Number += 1
    BestPoints = sorted(BestPoints, key=lambda x:x[2], reverse = True)
    if BestPoints[0][2] >= 1400:
        AcAnalyzeNumber = 1
	AcMaxDepth += 1
        #Position[BestPoint[0]][BestPoint[1]] = Self
        #RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
        #ChangeRange(BestPoint[0], BestPoint[1])
        #v = OpponentBest(-10000, +10000)
        #Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
        #Position[BestPoint[0]][BestPoint[1]] = 0
    for i in range(AcAnalyzeNumber):
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
	    if AcAnalyzeNumber == 1:
		AcMaxDepth -= 1
            Depth -= 1
	    return -29000, 30, Depth+1	
        Position[BestPoints[i][0]][BestPoints[i][1]] = Opponent 
    	RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
    	ChangeRange(BestPoints[i][0], BestPoints[i][1])
    	Cvalue, CWinDepth, CLoseDepth = SelfBest(Alpha, Beta)
	v = min(v, Cvalue)
	WinDepth = max(WinDepth, CWinDepth)
	LoseDepth = min(LoseDepth, CLoseDepth)
    	Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
    	Position[BestPoints[i][0]][BestPoints[i][1]] = 0
    	if v < Alpha:
	    if AcAnalyzeNumber == 1:
		AcMaxDepth -= 1
  	    Depth -= 1
    	    return v, WinDepth, LoseDepth
    	Beta = min(Beta, v)
    if v == 29000 and Doit == 1:
	for i in range(AcAnalyzeNumber, 20):
	    if BestPoints[i][0] == -2:
		break
	    if BestPoints[i][2] <= 0:
		break
	    if BestPoints[i][3] == 1:
	        if AcAnalyzeNumber == 1:
		    AcMaxDepth -= 1
                Depth -= 1
	        return -29000, 30, Depth+1	
            Position[BestPoints[i][0]][BestPoints[i][1]] = Opponent 
    	    RemUpm, RemLom, RemLem, RemRim = Upm, Lom, Lem, Rim
    	    ChangeRange(BestPoints[i][0], BestPoints[i][1])
    	    Cvalue, CWinDepth = SelfBest(Alpha, Beta)
    	    v = min(v, Cvalue)
	    WinDepth = max(WinDepth, CWinDepth)
	    LoseDepth = min(LoseDepth, CLoseDepth)
    	    Upm, Lom, Lem, Rim = RemUpm, RemLom, RemLem, RemRim
    	    Position[BestPoints[i][0]][BestPoints[i][1]] = 0
            if v < 29000:
	        if AcAnalyzeNumber == 1:
		    AcMaxDepth -= 1
    	        Depth -= 1
                return v, 30, 30
    if AcAnalyzeNumber == 1:
	AcMaxDepth -= 1
    Depth -= 1
    return v, WinDepth, LoseDepth

def Evalp(i, j, Self):
    Value = 0
    UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, End, SUR, SUL, SLL, SLR, SL ,SR, SU, SD = 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1
    OUR, OUL, OLL, OLR, OL, OR, OU, OD = 1, 1, 1, 1, 1, 1, 1, 1
    if Self == 3:
	Opponent = 4
    else: 
        Opponent = 3
    FirstNone1 = 1
    
    #Evaluate the value of our attack 
    for p in range(1, min(6, i+1, j+1)):
	if Position[i-p][j-p] != Self and Position[i-p][j-p] != Self-2:
    	    if FirstNone1 == 1:
	        if i-p == 0 or j-p == 0:
		    UL, SUL = p, p
		    break
		if Position[i-p][j-p] == Opponent or Position[i-p][j-p] == Opponent-2:
		    UL, SUL = p, p
		    break
		elif Position[i-p-1][j-p-1] == Self or Position[i-p-1][j-p-1] == Self-2:
		    UL, FirstNone1 = p, 0
		    continue
		else:
		    UL, SUL = p, p
		    break
	    if FirstNone1 == 0:
		SUL = p
		break
    FirstNone2 = 1
    for q in range(1, min(6, 17-i, 17-j)):
        if Position[i+q][j+q] != Self and Position[i+q][j+q] != Self-2:
    	    if FirstNone2 == 1:
	        if i+q == 16 or j+q == 16:
		    LR, SLR = q, q
		    break
		if Position[i+q][j+q] == Opponent or Position[i+q][j+q] == Opponent-2:
		    LR, SLR = q, q
		    break
		elif Position[i+q+1][j+q+1] == Self or Position[i+q+1][j+q+1] == Self-2:
		    LR, FirstNone2 = q, 0
		    continue
		else:
		    LR, SLR = q, q
		    break
	    if FirstNone2 == 0:
		SLR = q
		break
    for p in range(1, min(6, i+1, j+1)):
	OUL = p
	if Position[i-p][j-p] == Opponent or Position[i-p][j-p] == Opponent-2:
	    break
    for q in range(1, min(6, 17-i, 17-j)):
	OLR = q
        if Position[i+q][j+q] == Opponent or Position[i+q][j+q] == Opponent-2:
	    break
    if OUL+OLR < 6:
	Value -= 1
    else:
        if FirstNone1 == 0 and FirstNone2 == 0:
	    if SUL >= SLR:
		if i-SUL >= 1 and j-SUL >= 1:
		    if Position[i-SUL][j-SUL] == 0:
		        Up1 = Bonus(SUL+LR-2)
         	Value = Value+Price(SUL+LR-2)+Up1
	    else:
	        if i+SLR <= 15 and j+SLR <= 15:
		    if Position[i+SLR][j+SLR] == 0:
		        Up1 = Bonus(SLR+UL-2)
	        Value = Value+Price(SLR+UL-2)+Up1
        else:
            if i-SUL >= 1 and j-SUL >= 1 and i+SLR <= 15 and j+SLR <= 15:
	        if Position[i-SUL][j-SUL] == 0 and Position[i+SLR][j+SLR] == 0:
	            Up1 = Bonus(SUL+SLR+FirstNone1+FirstNone2-3)
            Value = Value + Price(SUL+SLR+FirstNone1+FirstNone2-3) + Up1
	    if FirstNone1 == 1 and FirstNone2 == 1:
		Value += 5

    FirstNone1 = 1
    for p in range(1, min(6, i+1, 17-j)):
        if Position[i-p][j+p] != Self and Position[i-p][j+p] != Self-2:
    	    if FirstNone1 == 1:
	        if i-p == 0 or j+p == 16:
		    LL, SLL = p, p
		    break
		if Position[i-p][j+p] == Opponent or Position[i-p][j+p] == Opponent-2:
		    LL, SLL = p, p
		    break
		elif Position[i-p-1][j+p+1] == Self or Position[i-p-1][j+p+1] == Self-2:
		    LL, FirstNone1 = p, 0
		    continue
		else:
		    LL, SLL = p, p
		    break
	    if FirstNone1 == 0:
		SLL = p
		break
    FirstNone2 = 1
    for q in range(1, min(6, 17-i, j+1)):
        if Position[i+q][j-q] != Self and Position[i+q][j-q] != Self-2:
    	    if FirstNone2 == 1:
	        if i+q == 16 or j-q == 16:
		    UR, SUR = q, q
		    break
		if Position[i+q][j-q] == Opponent or Position[i+q][j-q] == Opponent-2:
		    UR, SUR = q, q
		    break
		elif Position[i+q+1][j-q-1] == Self or Position[i+q+1][j-q-1] == Self-2:
		    UR, FirstNone2 = q, 0
		    continue
		else:
		    UR, SUR = q, q
		    break
	    if FirstNone2 == 0:
		SUR = q
		break
    for p in range(1, min(6, i+1, 17-j)):
	OLL = p
	if Position[i-p][j+p] == Opponent or Position[i-p][j+p] == Opponent-2:
	    break
    for q in range(1, min(6, 17-i, j+1)):
	OUR = q
        if Position[i+q][j-q] == Opponent or Position[i+q][j-q] == Opponent-2:
	    break
    if OLL+OUR < 6:
	Value -= 1
    else:
        if FirstNone1 == 0 and FirstNone2 == 0:
	    if SLL >= SUR:
		if i-SLL >= 1 and j+SLL <= 15:
		    if Position[i-SLL][j+SLL] == 0:
		        Up2 = Bonus(SLL+UR-2)
         	Value = Value+Price(SLL+UR-2)+Up2
	    else:
		if i+SUR <= 15 and j-SUR >= 1:
		    if Position[i+SUR][j-SUR] == 0:
		        Up2 = Bonus(SUR+LL-2)
	        Value = Value+Price(SUR+LL-2)+Up2
        else:
            if i-SLL >= 1 and j+SLL <= 15 and i+SUR <= 15 and j-SUR >= 1:
	        if Position[i-SLL][j+SLL] == 0 and Position[i+SUR][j-SUR] == 0:
	            Up2 = Bonus(SLL+SUR+FirstNone1+FirstNone2-3)
            Value = Value + Price(SLL+SUR+FirstNone1+FirstNone2-3) + Up2
	    if FirstNone1 == 1 and FirstNone2 == 1:
		Value += 5

    FirstNone1 = 1
    for p in range(1, min(6, i+1)):
        if Position[i-p][j] != Self and Position[i-p][j] != Self-2:
    	    if FirstNone1 == 1:
	        if i-p == 0:
		    L, SL = p, p
		    break
		if Position[i-p][j] == Opponent or Position[i-p][j] == Opponent-2:
		    L, SL = p, p
		    break
		elif Position[i-p-1][j] == Self or Position[i-p-1][j] == Self-2:
		    L, FirstNone1 = p, 0
		    continue
		else:
		    L, SL = p, p
		    break
	    if FirstNone1 == 0:
		SL = p
		break
    FirstNone2 = 1
    for q in range(1, min(6, 17-i)):
        if Position[i+q][j] != Self and Position[i+q][j] != Self-2:
    	    if FirstNone2 == 1:
	        if i+q == 16:
		    R, SR = q, q
		    break
		if Position[i+q][j] == Opponent or Position[i+q][j] == Opponent-2:
		    R, SR = q, q
		    break
		elif Position[i+q+1][j] == Self or Position[i+q+1][j] == Self-2:
		    R, FirstNone2 = q, 0
		    continue
		else:
		    R, SR = q, q
		    break
	    if FirstNone2 == 0:
		SR = q
		break
    for p in range(1, min(6, i+1)):
	OL = p
	if Position[i-p][j] == Opponent or Position[i-p][j] == Opponent-2:
	    break
    for q in range(1, min(6, 17-i)):
	OR = q
        if Position[i+q][j] == Opponent or Position[i+q][j] == Opponent-2:
	    break
    if OL+OR < 6:
	Value -= 1
    else:
        if FirstNone1 == 0 and FirstNone2 == 0:
	    if SL >= SR:
		if i-SL >= 1:
		    if Position[i-SL][j] == 0:
		        Up3 = Bonus(SL+R-2)
         	Value = Value+Price(SL+R-2)+Up3
	    else:
		if i+SR <= 15:
		    if Position[i+SR][j] == 0:
		        Up3 = Bonus(SR+L-2)
	        Value = Value+Price(SR+L-2)+Up3
        else:
            if i-SL >= 1 and i+SR <= 15:
	        if Position[i-SL][j] == 0 and Position[i+SR][j] == 0:
	            Up3 = Bonus(SL+SR+FirstNone1+FirstNone2-3)
            Value = Value + Price(SL+SR+FirstNone1+FirstNone2-3) + Up3
	    if FirstNone1 == 1 and FirstNone2 == 1:
		Value += 5

    FirstNone1 = 1
    for p in range(1, min(6, j+1)):
        if Position[i][j-p] != Self and Position[i][j-p] != Self-2:
    	    if FirstNone1 == 1:
	        if j-p == 0:
		    U, SU = p, p
		    break
		if Position[i][j-p] == Opponent or Position[i][j-p] == Opponent-2:
		    U, SU = p, p
		    break
		elif Position[i][j-p-1] == Self or Position[i][j-p-1] == Self-2:
		    U, FirstNone1 = p, 0
		    continue
		else:
		    U, SU = p, p
		    break
	    if FirstNone1 == 0:
		SU = p
		break
    FirstNone2 = 1
    for q in range(1, min(6, 17-j)):
        if Position[i][j+q] != Self and Position[i][j+q] != Self-2:
    	    if FirstNone2 == 1:
	        if j+q == 16:
		    D, SD = q, q
		    break
		if Position[i][j+q] == Opponent or Position[i][j+q] == Opponent-2:
		    D, SD = q, q
		    break
		elif Position[i][j+q+1] == Self or Position[i][j+q+1] == Self-2:
		    D, FirstNone2 = q, 0
		    continue
		else:
		    D, SD = q, q
		    break
	    if FirstNone2 == 0:
		SD = q
		break
    for p in range(1, min(6, j+1)):
	OU = p
	if Position[i][j-p] == Opponent or Position[i][j-p] == Opponent-2:
	    break
    for q in range(1, min(6, 17-j)):
	OD = q
        if Position[i][j+q] == Opponent or Position[i][j+q] == Opponent-2:
	    break
    if OU+OD < 6:
	Value -= 1
    else:
        if FirstNone1 == 0 and FirstNone2 == 0:
	    if SU >= SD:
		if j-SU >= 1:
		    if Position[i][j-SU] == 0:
		        Up4 = Bonus(SU+D-2)
         	Value = Value+Price(SU+D-2)+Up3
	    else:
		if j+SD <= 15:
		    if Position[i][j+SD] == 0:
		        Up4 = Bonus(SD+U-2)
	        Value = Value+Price(SD+U-2)+Up4
        else:
            if j-SU >= 1 and j+SD <= 15:
	        if Position[i][j-SU] == 0 and Position[i][j+SD] == 0:
	            Up4 = Bonus(SU+SD+FirstNone1+FirstNone2-3)
            Value = Value + Price(SU+SD+FirstNone1+FirstNone2-3) + Up4
	    if FirstNone1 == 1 and FirstNone2 == 1:
		Value += 5
    if UL+LR >= 6 or LL+UR >= 6 or U+D >= 6 or L+R >= 6:
        End = 1

    

    #Evaluate the value of our defense
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


def Evalpreserve(i, j, Self):
    Value = 0
    UR, UL, LL, LR, L, R, U, D, Up1, Up2, Up3, Up4, End= 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0
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
    if i-UL >= 1 and j-UL >= 1 and i+LR <= 15 and j+LR <= 15:
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
		CountAgain = 0
                for p in range(1, min(6, i+1, j+1)):
		    if Position[i-p][j-p] == Self:
			CountAgain = 1
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
		if CountAgain != 1:
		    if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
		        if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
		            Up1 = Bonus(UL+LR-1)
                    Value = Value + Price(UL+LR-1+BUL+BLR) + Up1
                
                CountAgain = 0
		for p in range(1, min(6, i+1, 17-j)):
                    if Position[i-p][j+p] != Self and Position[i-p][j+p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BLL == 0:
#			    BLL = -1
#			    continue
                        LL = p
                        break
                for q in range(1, min(6, 17-i, j+1)):
		    if Position[i+q][j-q] == Self:
			CountAgain = 1
                    if Position[i+q][j-q] != Self and Position[i+q][j-q] != Self-2:
 #                       if Position[i-q][j-q] == 0 and BUR == 0:
#			    BUR = -1
#			    continue
                        UR = q
                        break
		if CountAgain != 1:
		    if i-LL >= 1 and j+LL <= 15 and i+UR <=15 and j-UR >= 1:
		        if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
		            Up2 = Bonus(LL+UR-1)
                    Value = Value + Price(LL+UR-1+BUR+BLL) + Up2
                
                CountAgain = 0
		for p in range(1, min(6, i+1)):
		    if Position[i-p][j] == Self:
			CountAgain = 1
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
		if CountAgain != 1:
		    if i-L >= 1 and i+R <=15:
		        if Position[i-L][j] == 0 and Position[i+R][j] == 0:
		            Up3 = Bonus(L+R-1)
                    Value = Value + Price(L+R-1+BL+BR) + Up3
                
                CountAgain = 0
		for p in range(1, min(6, 17-j)):
                    if Position[i][j+p] != Self and Position[i][j+p] != Self-2:
#                        if Position[i-p][j-p] == 0 and BU == 0:
#			    BU = -1
#			    continue
                        U = p
                        break
                for q in range(1, min(6, j-1)):
                    if Position[i][j-q] == Self:
			CountAgain = 1
		    if Position[i][j-q] != Self and Position[i][j-q] != Self-2:
#                        if Position[i-q][j-q] == 0 and BD == 0:
#			    BD = -1
#			    continue
                        D = q
                        break
		if CountAgain != 1:
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
		
		CountAgain = 0
                for p in range(1, min(6, i+1, j+1)):
		    if Position[i-p][j-p] == Opponent:
			CountAgain = 1
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
		if CountAgain != 1:
		    if i-UL >= 1 and j-UL >= 1 and i+LR <=15 and j+LR <= 15:
		        if Position[i-UL][j-UL] == 0 and Position[i+LR][j+LR] == 0:
		            Up1 = Bonus(UL+LR-1)
                    Value = Value - Price(UL+LR-1+BUL+BLR) - Up1
                
		CountAgain = 0
                for p in range(1, min(6, i+1, 17-j)):
                    if Position[i-p][j+p] != Opponent and Position[i-p][j+p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BLL == 0:
#			    BLL = -1
#			    continue
                        LL = p
                        break
                for q in range(1, min(6, 17-i, j+1)):
		    if Position[i+q][j-q] == Opponent:
			CountAgain = 1
                    if Position[i+q][j-q] != Opponent and Position[i+q][j-q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BUR == 0:
#			    BUR = -1
#			    continue
                        UR = q
                        break
		if CountAgain != 1:
		    if i-LL >= 1 and j+UL <= 15 and i+UR <=15 and j-UR >= 1:
		        if Position[i-LL][j+LL] == 0 and Position[i+UR][j-UR] == 0:
		            Up2 = Bonus(LL+UR-1)
                    Value = Value - Price(LL+UR-1+BLL+BUR) - Up2
                
		CountAgain = 0
                for p in range(1, min(6, i+1)):
		    if Position[i-p][j] == Opponent:
			CountAgain = 1
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
		if CountAgain != 1:
		    if i-L >= 1 and i+R <=15:
		        if Position[i-L][j] == 0 and Position[i+R][j] == 0:
		            Up3 = Bonus(L+R-1)
                    Value = Value - Price(L+R-1+BL+BR) - Up3
                
		CountAgain = 0
                for p in range(1, min(6, 17-j)):
                    if Position[i][j+p] != Opponent and Position[i][j+p] != Opponent-2:
#                        if Position[i-p][j-p] == 0 and BU == 0:
#			    BU = -1
#			    continue
                        U = p
                        break
                for q in range(1, min(6, j+1)):
		    if Position[i][j-q] == Opponent:
			CountAgain = 1
                    if Position[i][j-q] != Opponent and Position[i][j-q] != Opponent-2:
#                        if Position[i-q][j-q] == 0 and BD == 0:
#			    BD = -1
#			    continue
                        D = q
                        break
		if CountAgain != 1:
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
    
    

Depth, MaxDepth, FirstVisit, BlackFirstMove, FirstAnalyze, OpponentFirstAnalyze = 0, 6, 1, 1, 9, 9
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
