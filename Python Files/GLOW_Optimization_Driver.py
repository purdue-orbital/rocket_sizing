# Optimization Function
# Iterates through Velocity split range
#
# Inputs:
# 1. Number of Stages
# 2. Lower velocity split bound
# 3. Upper velocity split bound
# 4. Array of Isp
# 5. Altitude
# 6. PayloadMass
#
# Output
# 1. Minimum GLOW
# 2. Configuration used for minimum

import Rocket
import numpy as np

def GLOW_Optimization_Driver(NumStages, VelocitySplitmin, VelocitySplitMax, Isp, Altitude, PayloadMass):

    #Determines Ideal Velocity
    Videal = 1.2 * np.sqrt(3.9857E14/Altitude)

    #Initialize Minimum GLOW value
    Min_GLOW = None

    #Loop through range of Velocity Splitd
    for split in range(VelocitySplitmin, VelocitySplitMax):
        DeltaVsplit = [Videal*split/100, Videal*(100 - split)/100]
        rocket = Rocket.Rocket(NumStages, Isp, DeltaVsplit, PayloadMass)
        rocket.optimize()

        if Min_GLOW == None:
            Min_GLOW = rocket.GLOW
            VelocitySplit = split
        elif Min_GLOW > rocket.GLOW:
            Min_GLOW = rocket.GLOW
            VelocitySplit = split

    return Min_GLOW, VelocitySplit


