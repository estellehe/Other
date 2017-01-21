# May 27, 2015
# Estelle(Wei) He
# Final project
# Canopy
# The bullet is shot horizontally to the right

# Setting
from numpy import arange
from pylab import plot,xlabel,ylabel,show
from math import atan, pi, sqrt

# Constants
g = 9.81    # Acceleration due to gravity (m/s^2)
k = 30     # Spring constant (N/m)
t = 0       # Initial time (s)
m = 0.1     # Mass of bullet (kg)
dt = 0.001   # Time step (s)
tmax = 0.6   # Time maximum (s)

# Variables
# Set the opening of the gun as origin, downward and right as positive direction
xpos0 = input("What is the horizontal coordinate/position of the block?(0.2-0.7)")  
ypos0 = input("What is the vertical coordinate/position of the block?(0.1-0.2)")    # Enter position of the block in meters  
time = []
accx = []
accy = []
velx = []
vely = []
posx = []
posy = []
enK = []
enU = []
enM = []
drange = arange(0.1, 0.3, 0.01)

# Part 1
# Functions
def dis(x, y):     # Use the position of block to find the compressed distance
    ty = sqrt(y*2/g)
    vx = x/ty
    dspring = sqrt(m*vx**2/k)
    return dspring

def value(distance, y):       # Find all values for a specific compressed distance with same final height
    E = 0.5*distance**2*k     # Total Mechanic Energy
    t = sqrt(y*2/g)
    vx = sqrt(E*2/m)
    vy = sqrt(2*g*y)
    v = sqrt(vx**2+vy**2)     # Final velocity
    x = t*vx                  # Final horizontal position 
    ang = atan(vy/vx)         # Direction of velocity
    print distance, "\t\t\t", round(x, 2), "\t\t\t\t", round(E, 2), "\t\t", round(v, 2), "\t\t", round(ang/pi*180, 2)
    
# Calculation
print "\nFor the final position (", xpos0, ",", ypos0, "), the compressed distance of the spring is:", dis(xpos0 ,ypos0), "m"

# Main loop
print "\nFor a block that is", ypos0, "m below the gun:"
print "Compressed Distance\tHorizontal Final Position\tTotal Energy\tFinal Velocity\tVelocity Direction"

for d in drange :
    value(d, ypos0)

# Part 2    
# Graphs 
print "\nTo plot graphs for a specific compressed distance of spring:"
dis = input("What is the compressed distance of the spring?(0.2-0.5)")   # Set a specific compressed distance for the spring

x = -dis    # Set initial condition of the bullet
y = 0
px = 0
py = 0

    
while t<tmax:
    if x<=0:        # When bullet is still attached to the spring
        Fs = k*dis
        ax = Fs/m
        ay = 0
        Fg = 0
        U = 0.5*k*dis**2
    else:           # When bullet leaves the gun
        Fs = 0
        ax = 0
        ay = g
        Fg = m*g
        U = -m*g*y
    px+=Fs*dt
    py+=Fg*dt
    vx = px/m
    vy = py/m
    x +=vx*dt
    y +=vy*dt
    v = sqrt(vx**2+vy**2)
    K = 0.5*m*v**2
    M = K+U
    time.append(t)
    accx.append(ax)
    accy.append(ay)
    velx.append(vx)
    vely.append(vy)
    posx.append(x)
    posy.append(y)
    enK.append(K)
    enU.append(U)
    enM.append(M)
    t+=dt
    dis = -x

'''                      # Four graphs are comment out here
plot(time, accx)
plot(time, accy)
xlabel("Time(s)")
ylabel("Acceleration(m/s**2)")
show()
'''

'''
plot(time, velx)
plot(time, vely)
xlabel("Time(s)")
ylabel("Velocity(m/s)")
show()
'''

'''
plot(time, posx)
plot(time, posy)
xlabel("Time(s)")
ylabel("Position(m)")
show()
'''

'''
plot(time, enK)
plot(time, enU)
plot(time, enM)
xlabel("Time(s)")
ylabel("Energy(J)")
show()
'''
    
