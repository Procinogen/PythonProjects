def main(n): #Declare main function, ask for the correct number of isotopes
    totalAtomicMass = 0 #Variable to hold the total atomic mass
    tempMass = 0 #Temporary variable used for adding
    for i in range(0, n):
        tempMass = float(input("Mass for isotope #" + str(i + 1) + ": ")) #Ask for the mass of the isotope
        tempMass *= (float(input("Abundance for the above isotope: ")) / 100) #Ask for the abundance (in percentage), and divide it by 100 to change it to a decimal, and multiply it by the current mass
        totalAtomicMass += tempMass #Add tempMass to the atomic mass
    print("Total mass: " + str(totalAtomicMass)) #Print it out when finished

main(int(input("How many isotopes?: ")))