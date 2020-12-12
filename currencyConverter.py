class exchangeRates:
    """This class is used to establish the formula used to convert the value"""
    def __init__(self, amount, rate):
        self.amount = amount
        self.rate = rate

    def exchangeEquation(self):
        return self.amount * self.rate

def importFile(valToEquate):
    """ This method inputs file and splits data into list"""
    infileName = input("Please enter the name of the file: ")
    infile = open(infileName, "r")
    for line in infile:
        valToEquate.append(line)
    return valToEquate


def outputFile(curVal):
    """This method pushes the newly converted amount to the output file"""
    outfileName = input("Please enter file name to output the new value to: ")
    outfile = open(outfileName, "w")
    print(curVal.exchangeEquation(), file=outfile)


def main ():
    valToEquate = []
    importFile(valToEquate)
    b4Val = valToEquate[1]
    b4Val = float(b4Val)
    """These if-else statements are used to determine which exchange rate should be applied
        to create an object using the exchangeRates class"""
    if "usd" in valToEquate[0] and "gbp" in valToEquate[2]:
        curVal = exchangeRates(b4Val, 0.75)
    
    elif "gbp" in valToEquate[0] and "usd" in valToEquate[2]:
        curVal = exchangeRates(b4Val, 1.34)

    elif "usd" in valToEquate[0] and "euro" in valToEquate[2]:    
        curVal = exchangeRates(b4Val, 0.83)
        
    elif "euro" in valToEquate[0] and "usd" in valToEquate[2]:   
        curVal = exchangeRates(b4Val, 1.21)
        
    elif "usd" in valToEquate[0] and "yuan" in valToEquate[2]:
        curVal = exchangeRates(b4Val, 6.54)
        
    elif "yuan" in valToEquate[0] and "usd" in valToEquate[2]:
        curVal = exchangeRates(b4Val, 0.15)
        
    elif "usd" in valToEquate[0] and "ruble" in valToEquate[2]:
        curVal = exchangeRates(b4Val, 73.83)
        
    elif "ruble" in valToEquate[0] and "usd" in valToEquate[2]:
        curVal = exchangeRates(b4Val, 0.014)
    else:
        print("That was the incorrect format. Please review your input file and try again.")

    outputFile(curVal)
main()

