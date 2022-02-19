offPeakE = float(input("Enter kwh during Off Peak Period :")) # My name is Jasneetpal Singh, and this is the home power consumption program I made
if offPeakE < 1 : #so if input is less than 1 it finishes the code
    exit()
offPeakECost = offPeakE*0.085

onPeakE = float(input("Enter kwh during On Peak Period :")) # for the user input
onPeakECost = onPeakE*0.176
if onPeakE < 150.00 :      # for the on peak discount
     discount = onPeakECost*0.05
else :
    discount = 0.00

midPeakE = float(input("Enter kwh during Mid Peak Period :"))
midPeakECost = midPeakE*0.119

TOTAL_USAGE = (offPeakE+onPeakE+midPeakE) #total usage discount, made constants which are used later on, just so it is easier
TOTAL_USAGE_COST = (offPeakECost+onPeakECost+midPeakECost)
if TOTAL_USAGE < 400 and onPeakE > 150.00 : # if on peak is greater than 150 then total usage discount can be applied
     discount = TOTAL_USAGE_COST*0.04
else:
    discount = 0.00

Senior = str(input("Is owner senior ?(Y,y,N,n):")) # this is the senior discount
if Senior.lower() in ['y' , 'Y'] : # so it only responds to y, Y, n, N
     discount = TOTAL_USAGE_COST * 0.11
else:
    Senior.lower() in ['n , N']
    discount = 0.00

totalCost = TOTAL_USAGE_COST - discount # calculating cost before taxes but after discount
tax = totalCost*0.13 # calculating tax
ElectricityCost = totalCost + tax #calclulating end result
print("Electricity cost : $ %.2f " %(ElectricityCost))
