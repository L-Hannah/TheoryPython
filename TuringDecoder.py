class TuringDecoder:
    def __init__(self):
        self.inputMachine()
    def checkMachine(self):
        if (self.machine==""):
            return False
        elif self.machine[0]!="0":
            return False
        else:
            return self.parseMachine()

    def parseMachine(self):
        #print("Parsing machine: "+machine)
        #print("Using alphabet:" +','.join(alphabet))
        #machine[0]=="0" by default as a check is done. Reduce string
        self.machine=self.machine[1:]
        #Get string alphabet
        splitMac = self.machine.split("0")
        zeroIndex = splitMac.index("")
        self.newStringAlph = [self.alphabet[x.count("1")-1] for x in splitMac[:zeroIndex]]
        splitMac = splitMac[zeroIndex+1:]
        self.getMoves(splitMac)
        return self.buildString()

    def getMoves(self,splitMac):
        self.moves=[]
        while len(splitMac)>1:
            zeroIndex=splitMac.index("")
            move = [x for x in splitMac[:zeroIndex]]
            self.moves.append(move)
            splitMac=splitMac[zeroIndex+1:]

    def getMoveStr(self,move):
        q,character,r,newChar,D = move
        result=""+\
        self.getState(q)+\
        self.alphabet[character.count("1")-1]+\
        "→"+\
        self.getState(r)+\
        self.alphabet[newChar.count("1")-1]+\
        ["R","L","S"][D.count("1")-1]
        return result

            
    def getState(self,stateStr):
        n = stateStr.count("1")
        if (n<3):
            return ["ha","hr"][n-1]
        return "q"+str(n-3)

    def buildString(self):
        result=""+\
        "The Turing machine uses string alphabet: Σ = {"+','.join(self.newStringAlph)+"}\n"+\
        "The Turing machine uses tape alphabet: Γ = {"+','.join(self.alphabet)+"}\n"+\
        "Possible moves:\n\t"+\
        '\n\t'.join([self.getMoveStr(x) for x in self.moves])
        return result


    def inputMachine(self):
        self.machine = input("Enter encoded Turing machine:\n")
        self.alphabet = []
        while True:
            newLetter = input("Enter a"+str(len(self.alphabet)+1)+"(\"empty\" for empty character): ")
            if newLetter == "":
                break
            if (newLetter not in self.alphabet):
                if (newLetter=="empty"):
                    self.alphabet.append("∆")
                else:
                    self.alphabet.append(newLetter)
        print()
        if (len(self.alphabet)>0):
            print(self.checkMachine())
            print("\n\n")
            self.inputMachine()
        else:
            print("Tape alphabet cannot be empty.")
            self.inputMachine()
turingDecoder = TuringDecoder()
