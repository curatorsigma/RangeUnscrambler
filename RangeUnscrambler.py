#
# !python3
# Range Unscrambler
# by Jonathan Schleucher (@Imathnathan)

from random import randint


class State(object):
    """Number of Dice"""
    def __init__(self, numofdicelist):
        super(State, self).__init__()
        self.numofdicelist = numofdicelist

    def calcmin(self):
        return sum(self.numofdicelist)

    def calcmax(self):
        res = 0
        for i in range(8, -1, -1):
            res += self.numofdicelist[i] * maxofdice[i]
        return res

    def calcexpect(self):
        res = 0
        for i in range(8, -1, -1):
            res += self.numofdicelist[i] * expectofdice[i]
        return res

    def calcvar(self):
        res = 0
        for i in range(8, -1, -1):
            res += self.numofdicelist[i]**2 * varofdice[i]
        return res

    def calcdev(self):
        res = 0
        for i in range(8, -1, -1):
            res += self.numofdicelist[i]**2 * varofdice[i]
        return res**0.5

    def transform(self, transformation):
        if all([x >= y for (x, y) in zip(self.numofdicelist, transformation.fromn.numofdicelist)]):
            # DEBUGprint("in transform: doing transformation")
            self.numofdicelist = [x - y for (x, y) in zip(self.numofdicelist, transformation.fromn.numofdicelist)]
            self.numofdicelist = [x + y for (x, y) in zip(self.numofdicelist, transformation.ton.numofdicelist)]
            return True
        else:
            return False


class Transform(object):
    """DataClass to hold the dice-transformation to reach minval."""
    def __init__(self, fromn, ton):
        super(Transform, self).__init__()
        self.fromn = fromn
        self.ton = ton


minval = 1
maxval = 2
percentilemode = True
verbosemode = False
maxofdice = (1, 2, 3, 4, 6, 8, 10, 12, 20)  # die type
numofdice = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # how many you have to roll
expectofdice = (1, 1.5, 2, 2.5, 3.5, 4.5, 5.5, 6.5, 10.5)  # E(die)
varofdice = (0, 0.25, 0.66, 1.25, 2.917, 5.25, 8.25, 11.92, 33.25)  # Var(die)

purge3 = [Transform(State([0, 1, 1, 0, 0, 0, 0, 0, 0]), State([1, 0, 0, 1, 0, 0, 0, 0, 0])),
          Transform(State([0, 0, 1, 1, 0, 0, 0, 0, 0]), State([1, 0, 0, 0, 1, 0, 0, 0, 0])),
          Transform(State([0, 0, 1, 0, 1, 0, 0, 0, 0]), State([1, 0, 0, 0, 0, 1, 0, 0, 0])),
          Transform(State([0, 0, 1, 0, 0, 1, 0, 0, 0]), State([1, 0, 0, 0, 0, 0, 1, 0, 0])),
          Transform(State([0, 0, 1, 0, 0, 0, 1, 0, 0]), State([1, 0, 0, 0, 0, 0, 0, 1, 0]))]
purge2 = [
          Transform(State([0, 11, 0, 0, 0, 0, 0, 0, 0]), State([10, 0, 0, 0, 0, 0, 0, 1, 0])),
          Transform(State([0, 9, 0, 0, 0, 0, 0, 0, 0]), State([8, 0, 0, 0, 0, 0, 1, 0, 0])),
          Transform(State([0, 7, 0, 0, 0, 0, 0, 0, 0]), State([6, 0, 0, 0, 0, 1, 0, 0, 0])),
          Transform(State([0, 5, 0, 0, 0, 0, 0, 0, 0]), State([4, 0, 0, 0, 1, 0, 0, 0, 0])),
          Transform(State([0, 3, 0, 0, 0, 0, 0, 0, 0]), State([2, 0, 0, 1, 0, 0, 0, 0, 0])),
          ]
chdict = {
    1: [Transform(State([0, 0, 0, 0, 0, 1, 0, 0, 0]), State([0, 0, 0, 2, 0, 0, 0, 0, 0])),
        Transform(State([0, 0, 0, 0, 0, 0, 0, 1, 0]), State([0, 0, 0, 0, 2, 0, 0, 0, 0])),
        Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([0, 0, 0, 0, 0, 0, 2, 0, 0])),
        Transform(State([0, 0, 0, 1, 0, 0, 0, 0, 0]), State([1, 0, 1, 0, 0, 0, 0, 0, 0])),
        Transform(State([0, 0, 0, 1, 0, 0, 0, 0, 0]), State([0, 2, 0, 0, 0, 0, 0, 0, 0])),
        Transform(State([0, 0, 0, 0, 1, 0, 0, 0, 0]), State([0, 0, 2, 0, 0, 0, 0, 0, 0]))],
    2: [Transform(State([0, 0, 0, 0, 1, 0, 0, 0, 0]), State([2, 0, 0, 1, 0, 0, 0, 0, 0])),
        Transform(State([0, 0, 0, 0, 0, 1, 0, 0, 0]), State([2, 0, 0, 0, 1, 0, 0, 0, 0])),
        Transform(State([0, 0, 0, 0, 0, 0, 1, 0, 0]), State([2, 0, 0, 0, 0, 1, 0, 0, 0])),
        Transform(State([0, 0, 0, 0, 0, 0, 0, 1, 0]), State([2, 0, 0, 0, 0, 0, 1, 0, 0])),
        Transform(State([0, 0, 0, 1, 0, 0, 0, 0, 0]), State([1, 1, 0, 0, 0, 0, 0, 0, 0]))],
    3: [Transform(State([0, 0, 0, 1, 0, 0, 0, 0, 0]), State([4, 0, 0, 0, 0, 0, 0, 0, 0]))],
    5: [Transform(State([0, 0, 0, 0, 1, 0, 0, 0, 0]), State([6, 0, 0, 0, 0, 0, 0, 0, 0]))],
    7: [Transform(State([0, 0, 0, 0, 0, 1, 0, 0, 0]), State([8, 0, 0, 0, 0, 0, 0, 0, 0]))],
    8: [Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([8, 0, 0, 0, 0, 0, 0, 1, 0]))],
    9: [Transform(State([0, 0, 0, 0, 0, 0, 1, 0, 0]), State([10, 0, 0, 0, 0, 0, 0, 0, 0]))],
    10: [Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([10, 0, 0, 0, 0, 0, 1, 0, 0]))],
    11: [Transform(State([0, 0, 0, 0, 0, 0, 0, 1, 0]), State([12, 0, 0, 0, 0, 0, 0, 0, 0]))],
    12: [Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([12, 0, 0, 0, 0, 1, 0, 0, 0]))],
    14: [Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([14, 0, 0, 0, 1, 0, 0, 0, 0]))],
    16: [Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([16, 0, 0, 1, 0, 0, 0, 0, 0]))],
    19: [Transform(State([0, 0, 0, 0, 0, 0, 0, 0, 1]), State([20, 0, 0, 0, 0, 0, 0, 0, 0]))]
}
possibchange = [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 16, 19]


def unscramble(minval, maxval, percentile=True):
    if percentile:  # compute offset and reroll for percentile.
        diff = maxval - minval
        if diff == 1:
            return (f"Roll 1d2 (1d4, even = 2, odd = 1) and add {minval - 1}."), None
        elif diff == 2:
            return (f"Roll 1d3 (1d6 with 1-2 = 1, 3-4 = 2, 5-6 = 3)"
                    + f" and add {minval-1}."), None
        elif diff < 4 and diff > 2:
            return (f"Roll 1d4 and add {minval - 1}. Reroll"
                    + f" if your unmodified roll is {diff + 2} or higher."), None
        elif diff < 6 and diff > 3:
            return (f"Roll 1d6 and add {minval - 1}. Reroll"
                    + f" if your unmodified roll is {diff + 2} or higher."), None
        elif diff < 10 and diff > 4:
            return (f"Roll 1d10 and add {minval - 1}. Reroll"
                    + f" if your unmodified roll is {diff + 2} or higher."), None
        elif diff < 12 and diff > 5:
            return (f"Roll 1d12 and add {minval - 1}. Reroll"
                    + f" if your unmodified roll is {diff + 2} or higher."), None
        elif diff < 20 and diff > 9:
            return (f"Roll 1d20 and add {minval - 1}. Reroll"
                    + f" if your unmodified roll is {diff + 2} or higher."), None
        elif diff < 100 and diff > 45:
            return (f"Roll 1d100 and add {minval - 1}. Reroll"
                    + f" if your unmodified roll is {diff + 2} or higher."), None

    if (maxval - minval) * 3 < maxval:
        numofdice[0] += (maxval - minval) * 2
    maxvaltemp = maxval
    # the following loop sets all dice to fit the maximum, with the smallest
    # number of dice possible.
    for i in range(8, -1, -1):
        numofdice[i] = int(maxvaltemp // maxofdice[i])  # set to max that fits
        maxvaltemp = maxvaltemp % maxofdice[i]  # reduce to remainder
    # we now change these numbers until the minimum can be reached.
    deficit = minval - sum(numofdice)  # how much is missing to get minval
    if deficit < 0:
        return f"Range can not be resolved. {randint(minval, maxval)} is a random number in it.", None
    elif deficit == 0:
        # DEBUGprint("instant fit (deficit == 0")
        return buildresult(State(numofdice)), State(numofdice)
    else:
        dicestate = State(numofdice)
        while deficit > 0:
            i = -1
            while i < len(possibchange) - 1:
                if possibchange[i + 1] > deficit:
                    break
                i += 1
                # search through all smaller transformations and take the biggest possible
            for j in range(i, -1, -1):  # search through all smaller transformations
                #DEBUGprint("changed j", j, chdict[possibchange[j]])
                for trans in chdict[possibchange[j]]:  # all trans. of given size
                    # Debugprint(trans.fromn.numofdicelist, trans.ton.numofdicelist, dicestate.numofdicelist, deficit, i, j)
                    tempflag = dicestate.transform(trans)  # transform
                    if tempflag:
                        # Debugprint("found possible transformation")
                        break
                else:
                    continue
                break
            else:
                return f"Range can not be resolved. {randint(minval, maxval)} is a random number in it."
            deficit = minval - dicestate.calcmin()
            continue
        purgehalfdice(dicestate)
        return buildresult(dicestate), dicestate


def buildresult(state):  # string representation of solution
    resultstring = []
    for i in range(1, 9):
        if state.numofdicelist[i]:
            resultstring.append(f"{state.numofdicelist[i]}d{maxofdice[i]}")
    if state.numofdicelist[0]:
        resultstring.append(f"{state.numofdicelist[0]}")
    return "Roll " + " + ".join(resultstring)


def purgehalfdice(state):
    if not state.numofdicelist[1]:
        if not state.numofdicelist[2]:
            return
        else:
            tempflag = True
            while tempflag:
                for trans in purge3:
                    tempflag = state.transform(trans)
                    if tempflag:
                        break
            tempflag = True
            while tempflag:
                for trans in purge3:
                    tempflag = state.transform(trans)
                    if tempflag:
                        break
            return

if __name__ == "__main__":
    print("Welcome to the Range Unscrambler. \n"
          "It can compute the dice needed to generate a specified Range "
          "with and without the use of Rerolls and "
          "if the range is impractical to roll for, it can give "
          "you a randomly generated Result. Enjoy!")

    while True:
        # read User input
        print("\n" * 2 + "Enter r to generate a solution for the last Range.")
        print("Enter q to quit.")
        tempstr = "allowed." if percentilemode else "not allowed."
        print("Rerolls are currentely " + tempstr + " Enter p to change.")
        tempstr = "" if verbosemode else "non"
        print("Unscrambler is currentely in the " + tempstr
               + "verbose mode. Press v to change.")
        instr = input("Enter the minimum and maximum Value to obtain, "
                      "seperated by a single space." + "\n")
        print("\n")
        if instr == "r" or instr == "R":    # generate random number
            print((minval, maxval), " is in the given Range.")
            continue
        elif instr == "p" or instr == "P":  # change percentilemode
            percentilemode = not percentilemode
            continue
        elif instr == "v" or instr == "V":
            verbosemode = not verbosemode
            continue
        elif instr == "q" or instr == "Q":
            quit()
        else:
            instr = instr.split(" ")
            try:
                minval = int(instr[0])
                maxval = int(instr[1])
                if minval > maxval:
                    continue
            except ValueError:
                minval = 1
                maxval = 2
                continue
            res = unscramble(minval, maxval, percentilemode)
            print(res[0])
            if verbosemode and res[1]:
                print(f"Standard Deviation: {res[1].calcdev()} \n"
                      f"Expectationvalue: {res[1].calcexpect()}")
