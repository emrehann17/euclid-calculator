
import time
import math

def euclid():
    a = float(input("Enter first x coordinate:"))
    b = float(input("Enter second x coordinate:"))
    c = float(input("Enter first y coordinate:"))
    d = float(input("Enter second y coordinate:"))
    
    print("Calculating..")
    time.sleep(0.6)

    resx = (a-b)**2
    resy = (c-d)**2

    res_euc = math.sqrt(resx + resy)
    return res_euc

print(euclid())