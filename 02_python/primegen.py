import numpy as np
import matplotlib.pyplot as plt
# Python program to print all
# prime number in an interval
import matplotlib as mpl
mpl.rcParams['lines.markersize'] = 3
import time
from math import sqrt
start_time = time.time()

start = 1
end = 10000
pi = 3.1415927

allz = []
allz = np.linspace(start = 0, stop = 10000, num = 10001)
allzsol = []
#plt.polar(allz, allz, 'k.',)
for val in allz:
    if(val % 2 != 0) and (val % 11 != 0):
        #continue
        allzsol.append(val)
#    elif(val % 11 != 0):
#        continue
        #allzsol.append(val)
#    elif(val % 71 == 0):
#        continue
        #allzsol.append(val)
#print(allzsol);
#print(allzsol[:10])
#allzsol = [x + 44 for x in allzsol]


#44+2n=0  -> n
plt.polar(allzsol, allzsol, "r.",)


primes = []
###############################################
for val in range(start, end + 1):

   # If num is divisible by any number
   # between 2 and val, it is not prime
   if val > 1:
       for n in np.arange(2, sqrt(val)):
           if (val % n) == 0:
               break
       else:
           #plt.polar(val, val, 'b.')
           print(val)
           if(val == 4 or val == 121):
               continue
           primes.append(val)
           plt.polar(val, val,  "b.",)

print("--- %s seconds ---" % (time.time() - start_time))

#>>> S1 = set(L1)
#>>> S2 = set(L2)
#>>> S1.intersection(S2)
#set([2])
S1 = set(allzsol)
S2 = set(primes)
collisions = S1.intersection(S2)
collision = list(collisions)
print(collision)
plt.show()
