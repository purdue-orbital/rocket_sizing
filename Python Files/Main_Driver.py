# Main Driver for Optimization Software

from GLOW_Optimization_Driver import GLOW_Optimization_Driver

Num_Stages = 2
MinVelocitySplit = 25
MaxVelocitySplit = 75
Isp = [250, 300]
Altitude = 150000
PayloadMass = 1.33

GLOW, VelocitySplit = GLOW_Optimization_Driver(Num_Stages, MinVelocitySplit, MaxVelocitySplit, Isp, Altitude, PayloadMass)

print(GLOW)
print(VelocitySplit)


