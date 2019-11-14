# Rocket Class
# Holds array of stages and other information about the rocket
#
# Inputs:
# 1. Number of stages
# 2. Array of Isp
#
# Output
# 1. GLOW


import Stages


class Rocket:
    #Constructor
    def __init__(self, num_Stages, Isp, DeltaVsplit, PayloadMass):
        self.num_Stages = num_Stages
        self.Isp = Isp
        self.DeltaVsplit = DeltaVsplit
        self.PayloadMass = PayloadMass
        self.Stages = []
        self.GLOW = None
