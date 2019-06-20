from numpy import*
import numpy
arr1=loadtxt('KE-3D.dat')
arr2=loadtxt('Enstrophy-3D.dat')
t=arr1[:,0]
t1=arr1[:,0]*1.99
r=len(arr1)
c=len(arr1[0])
h=arr1[1][0]-arr1[0][0];
kerate=0.0
Enrate=0.0
n=0.01                                              #kinematic viscosity
l2=[]
l3=[]
for i in range(0,r):
   if i==0:
      kerate=-(arr1[1][1]-arr1[0][1])/h
      l2.append(kerate)
   elif i==r-1:
      kerate=-(arr1[i-1][1]-arr1[i][1])/(h)
      l2.append(kerate)
   else:
      kerate=-(arr1[i+1][1]-arr1[i-1][1])/(2*h)
      l2.append(kerate)
   Enrate=2*n*arr2[i][1]
   l3.append(Enrate)
DataOut = column_stack((t,l2))
DataOut1=column_stack((t,l3))
savetxt('KErate_3D.dat',DataOut)
savetxt('Enstrophyrate_3D.dat',DataOut1)
