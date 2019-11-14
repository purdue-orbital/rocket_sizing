# Stages Class
# Calculates mass of an individual stage
#
# Inputs:
# 1. Isp
# 2. Propellant Mass Fraction
# 3. Payload Mass
# 4. Velocity
# 5.
#
# Outputs:
# 1. Propellant mass
# 2. Inert Mass
# 3.


class Stages:
    # Constructor
    def Stages(self, Isp, PropellantMassFract, PayloadMass,TotalDeltaV, VelocitySplit):
        self.Isp = Isp
        self.PropellantMassFract = PropellantMassFract
        self.PayloadMass = PayloadMass
        self.DeltaV = VelocitySplit * TotalDeltaV
        self.PropellantMass = None
        self.InertMass = None
        self.FlightTime = None
