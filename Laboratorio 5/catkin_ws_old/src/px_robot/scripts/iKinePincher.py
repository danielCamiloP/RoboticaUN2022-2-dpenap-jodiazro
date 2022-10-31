from array import array
from operator import concat
import numpy as np

def iKine(x,y,z,theta):
    t2 = np.cos(theta)
    t3 = np.sin(theta)
    t4 = x**2
    t5 = y**2
    t6 = z**2
    t8 = z*2.06e+2
    t24 = z*8.99641890121408e-3
    t7 = t2**2
    t9 = -t4
    t10 = -t5
    t11 = -t6
    t12 = t3*1.1e+2
    t13 = -t8
    t14 = t4+t5
    t15 = t3*z*2.2e+2
    t16 = t3*2.266e+4
    t20 = t4/2.2898e+4
    t21 = t5/2.2898e+4
    t22 = t6/2.2898e+4
    t26 = -t24
    t27 = t3*z*9.607826011005328e-3
    t28 = t3*9.896060791335488e-1
    t17 = -t15
    t18 = -t16
    t19 = t7*1.21e+4
    t23 = np.sqrt(t14)
    q1 = np.arctan2(-((t2*1.1e+2-t23)*y)/t23,-((t2*1.1e+2-t23)*x)/t23)

    t25 = t12+z-1.03e+2
    t29 = -t28
    t30 = t2*t23*2.2e+2
    t32 = t2*t23*9.607826011005328e-3
    t31 = -t30
    t33 = -t32
    t40 = t8+t9+t10+t11+t16+t17+t30+1.89e+2
    t34 = t14+t19+t31
    t38 = t6+t13+t14+t15+t18+t31+2.2709e+4
    t41 = t40**2
    t45 = t20+t21+t22+t26+t27+t29+t33-8.25399598218185e-3
    t35 = 1.0/np.sqrt(t34)
    t39 = 1.0/t38
    t42 = -t41
    t46 = np.arccos(t45)
    t36 = t25*t35
    t43 = t42+5.24318404e+8
    t37 = np.arctan(t36)
    t44 = np.sqrt(t43)
    t47 = t39*t44
    t48 = np.arctan(t47)
    q2 = t37+t48-np.pi/2.0


    q3 = -t46


    q4 = -t37+t46-t48
    return np.array([q1, q2, q3, q4])

def lineInterp(n, xi, yi, xf, yf):
    x = np.linspace(xi,xf,n)
    y = np.linspace(yi,yf,n)
    return np.array((x,y))

def arcInterp(n, R, xi, yi, xf, yf, isCCW):
    center = getCenter(R, xi, yi, xf, yf, isCCW)
    xc = center[0]
    yc = center[1]
    ti = np.arctan2(yi-yc,xi-xc)
    tf = np.arctan2(yf-yc,xf-xc)

    t = np.linspace(ti,tf,n)
    x = R*np.cos(t) + xc
    y = R*np.sin(t) + yc
    
    return np.array((x,y))
    
def getQLine(n, xi, yi, xf, yf,z):
    in_points = lineInterp(n, xi, yi, xf, yf)
    print(in_points.shape)
    auxq = iKine(in_points[0,:],in_points[1,:],z,0)
    return auxq

def getQArc(n, R, xi, yi, xf, yf,z,isCCW):
    in_points = arcInterp(n, R, xi, yi, xf, yf, isCCW)
    print(in_points.shape)
    auxq = iKine(in_points[0,:],in_points[1,:],z,0)
    return auxq

def getCenter(R,x0,y0,x1,y1,isOnLeft):
    aux = np.sqrt((4*R**2-(x0-x1)**2-(y0-y1)**2)/((x0-x1)**2+(y0-y1)**2))
    if isOnLeft:
        xc = (x0+x1+y0*aux-y1*aux)/2
        yc = (y0+y1-x0*aux+x1*aux)/2
    else:
        xc = (x0+x1-y0*aux+y1*aux)/2
        yc = (y0+y1+x0*aux-x1*aux)/2
    return (xc,yc)

aux = getQArc(4,100,100,0,0,100,80,True)
print(np.mod(7,3))
