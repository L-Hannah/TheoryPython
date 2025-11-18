def checkMachine(machine,alphabet):
    if (machine==""):
        return False
    elif machine[0]!="0":
        return False
    else:
        return parseMachine(machine,alphabet)

def parseMachine(machine,alphabet):
    #print("Parsing machine: "+machine)
    #print("Using alphabet:" +','.join(alphabet))
    #machine[0]=="0" by default as a check is done. Reduce string
    machine=machine[1:]
    #Get string alphabet
    splitMac = machine.split("0")
    zeroIndex = splitMac.index("")
    newStringAlph = [alphabet[x.count("1")-1] for x in splitMac[:zeroIndex]]
    splitMac = splitMac[zeroIndex+1:]
    moves = getMoves(splitMac)
    return buildString(alphabet,newStringAlph,moves)

def getMoves(splitMac):
    moves=[]
    while len(splitMac)>1:
        zeroIndex=splitMac.index("")
        move = [x for x in splitMac[:zeroIndex]]
        moves.append(move)
        splitMac=splitMac[zeroIndex+1:]
    return moves

def getMoveStr(move,alphabet):
    q,character,r,newChar,D = move
    result=""+\
    getState(q)+\
    alphabet[character.count("1")-1]+\
    "→"+\
    getState(r)+\
    alphabet[newChar.count("1")-1]+\
    ["R","L","S"][D.count("1")-1]
    return result

        
def getState(stateStr):
    n = stateStr.count("1")
    if (n<3):
        return ["ha","hr"][n-1]
    return "q"+str(n-3)

def buildString(alphabet,newStringAlph,moves):
    result=""+\
    "The Turing machine uses string alphabet: Σ = {"+','.join(newStringAlph)+"}\n"+\
    "The Turing machine uses tape alphabet: Γ = {"+','.join(alphabet)+"}\n"+\
    "Possible moves:\n\t"+\
    '\n\t'.join([getMoveStr(x,alphabet) for x in moves])
    return result


def inputMachine():
    machine = input("Enter encoded Turing machine:\n")
    alphabet = []
    while True:
        newLetter = input("Enter a"+str(len(alphabet)+1)+"(\"empty\" for empty character): ")
        if newLetter == "":
            break
        if (newLetter not in alphabet):
            if (newLetter=="empty"):
                alphabet.append("∆")
            else:
                alphabet.append(newLetter)
    print()
    if (len(alphabet)>0):
        print(checkMachine(machine,alphabet))
    else:
        print("Tape alphabet cannot be empty.")
        inputMachine()
inputMachine()
