import sys
import numpy as np

min_t, max_t, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
print(", ".join(map(str, np.round(np.geomspace(min_t, max_t, n)).astype(int)))) #-> np.geomspace generates logarithmically spaced values between min_t and max_t

## Run code as: /Applications/PsychoPy.app/Contents/MacOS/python LOGSPACE.py 11 350 6 -r <-- insert whatever numbers you want. 