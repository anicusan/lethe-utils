###########################################################
# File : calculate_dissipation_rate.py
#---------------------------------------------------------
# Calculates the dissipation rate from the kinetic energy
# using a second order finite difference approximation
###########################################################


import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Arguments for calculation of the dissipation rate')
parser.add_argument("-i", "--input", type=str, help="Name of the input file", required=True)
args, leftovers=parser.parse_known_args()

fname=args.input

arr1=np.loadtxt(fname,skiprows=1)

t=arr1[:,0]

r=len(arr1)

h=arr1[1][0]-arr1[0][0];

kerate=0.0
l2=[]
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
DataOut = np.column_stack((t,l2))

np.savetxt('KErate_3D.dat',DataOut)