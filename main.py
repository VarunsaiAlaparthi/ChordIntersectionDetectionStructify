from intersections import countIntersections

def main():
    inp = input("If you want to update the text file enter yes If you want to give input from the command prompt type any key: ")
    if inp.lower() =="yes":
        with open('input.txt', 'r') as file:
            # Read the input from the file 
            textInput = file.readlines()
            radians = eval(textInput[0].strip())[0]
            identifiers = eval(textInput[1].strip())
    else:
        radians = input("Enter the list of Radians: ")
        identifiers = input("Enter the list of Identifiers: ")
        radians  = radians.split(",")
        identifiers = identifiers.split(",")
    
    radians = [float(item) for item in radians]
    

    intersections = countIntersections(radians, identifiers)

    print("Total number of Intersections for the given chords are: "+str(intersections))


if __name__=="__main__":
    main()


