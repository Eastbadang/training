import numpy as np
from numpy import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import sys
import os
import subprocess
import image
#import ImageChops
from mayavi import mlab
import pandas as pd

filename = sys.argv[1]

def show(i):
	global uu, NX, NY, NZ
	mlab.figure(mlab.gcf,bgcolor=(0,0,0),size=(800,800))
	vol = mlab.pipeline.volume(mlab.pipeline.scalar_field(uu[i]),vmin=-0.1, vmax=0.8)
	mlab.view(azimuth=0, elevation=90, distance=100, focalpoint='auto')
	# mlab.pipeline.scalar_cut_plane(mlab.pipeline.scalar_field(uu[i]),plane_orientation='z_axes',contours=20)
	# mlab.contour3d(uu[i,:,:,1],vmin=-0.1, vmax=0.8)
	mlab.surf(uu[i,:,:,1],vmin=-0.1, vmax=0.8, opacity=0.1,representation='wireframe',warp_scale=2.0)
	engine=mlab.get_engine()
	array_source = engine.scenes[0].children[1]
	array_source.origin = array([0,0,0])
	mlab.show()

def animate(start=15,di=5,end=1000,output="out"):
	global T, NX, NY, NZ
	if (T < end):
		end = T
	for i in range(start,end,di):
		mlab.figure(mlab.gcf,bgcolor=(0,0,0),size=(800,800))
		vol = mlab.pipeline.volume(mlab.pipeline.scalar_field(uu[i]), vmin=-0.1, vmax=0.8)
		# mlab.view(azimuth=45, elevation=45, distance=100, focalpoint=(NX/2,NY/2,NZ/2))
		# mlab.view(azimuth=0, elevation=90, distance=100, focalpoint='auto')
		# mlab.contour3d(uu[i,:,:,1],vmin=-0.1, vmax=0.8)
		mlab.surf(uu[i,:,:,1],vmin=-0.1, vmax=0.8, opacity=0.1,representation='wireframe',warp_scale=2.0)
		engine=mlab.get_engine()
		scene = engine.scenes[0]
		scene.scene.parallel_projection = True
		array_source = engine.scenes[0].children[1]
		array_source.origin = array([0,0,0])
		vol.scene.anti_aliasing_frames = 0
		mlab.savefig("output/"+ output + "%03d.png" % i)
		mlab.clf()
		# f.scene.render()
		# yield

def import_shape(shapename):
	global fin
	print ("Importing geometry from " + shapename + "...")
	im = Image.open(shapename,'r')
	pix_val = np.array(im.getdata())
	print ("Shape size: " + str(np.shape(pix_val)[0]))
	pix_val.tofile(fin,sep="\n",format="%d")
	fin.write("\n256\n")

if len(sys.argv) == 3:
	print ("ERROR!")
	print ("Need to know how many z layers there are...")
	sys.exit(0)

if len(sys.argv) == 4:
	fin = open('shape.dat','w+')
	shapename = sys.argv[2]
	num_layers = sys.argv[3]
	print ("Importing geometry from " + shapename + "...")
	
	# im = Image.open(shapename,'r')
	# f = open('shape.dat','w+')
	bashCommand = "rm shape/input_shape-*"
	os.system(bashCommand)
	bashCommand = "convert " + shapename + ".gif shape/input_shape.png"
	os.system(bashCommand)
	for i in range(int(num_layers)):
		import_shape("shape/input_shape-"+str(i)+".png")
	# pix_val = np.array(im.getdata())*10/255
	# print "Shape size: " + str(np.shape(pix_val)[0])
	# pix_val.tofile(f,sep="\n",format="%d")
	# f.close()

print ("Compiling " + filename + ".c...")
# bashCommand = "gcc " + filename + ".c -o " + filename + " -lm"
# os.system(bashCommand)
p =subprocess.Popen(['gcc', '-o', filename, filename+".c"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output=p.communicate()

if (output[0]):
	print ("******** ERROR COMPILING ********")
	print (output[0])
else:
	print ("Executing "+filename+".o...")
	p =subprocess.Popen(["./"+filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	# p.wait()
	output=p.communicate()
	print(output[0])
	# if (not output[0]):
	# 	print "******** RUNTIME ERROR ********"
	# 	print output[0]
	# else:

	# bashCommand = "./"+filename
	# os.system(bashCommand)

	datafile = "data.dat"
	print ("Importing data from " + datafile + "...")
	print ("Using comma delimiter")

	f = open(datafile,'r')
	header = f.readline()
	header = header.strip().split("\t")
	NX = int(header[0])
	NY = int(header[1])
	NZ = int(header[2])
	T = int(header[3])-1
	# NZ = int(header[3])-1
	# T = int(header[2])
	
	
	# NX = 40
	# NY = 40
	# # T = 100-1
	# NZ = 199
	# x,y = np.loadtxt(datafile, delimiter = ',')

	# uu = np.array(pd.read_csv('data.dat',header=None,skiprows=1,delim_whitespace=True,skipinitialspace=True,usecols=[1]))
	# uu = np.loadtxt('data.dat',skiprows=1)#.reshape(T,NX,NY)

	uu = zeros([T,NX,NY,NZ])
	for n in range(T):
		for k in range(NZ):
			for j in range(NY):
				for i in range(NX): 
					uu[n,i,j,k] = f.readline().strip()

	print ("Domain size: " + str(size(uu)))
	# uu = uu.reshape(T,NX,NY)
	set_printoptions(threshold=nan)
	# print shape(uu)
	# uu = uu.reshape(T,NZ,NY,NX)
	# uu = np.swapaxes(uu,1,3)
	f.close()

	# uu = np.rollaxis(uu,1,4)
	# uu = np.rollaxis(uu,0,3)
	# uu2 = np.swapaxes(uu,1,2)
	
	# print shape(uu2)
	# print shape(uu)
	# uu = np.genfromtxt('data.dat', delimiter=',')[:,:-1]
	# data = data.T

	# print uu

	# x, y = meshgrid(arange(NX),arange(NY))
	# show(50)

	
	# s = mlab.mesh(x, y, uu[40,x,y])
	
	# mlab.options.offscreen = True
	# for i in range(15,T,2):
	# 	mlab.figure(mlab.gcf,bgcolor=(0,0,0),size=(800,800))
	# 	vol = mlab.pipeline.volume(mlab.pipeline.scalar_field(uu[i]), vmin=-0.1, vmax=0.8)
	# 	# vol = mlab.pipeline.iso_surface(mlab.pipeline.scalar_field(uu[i]), contours=50, vmin=-.56, vmax=0.12,opacity=0.3)
	# 	mlab.savefig("pw_dipole_" + str(i) + ".png")
	# 	# mlab.draw()
	# 	mlab.clf()
	
	# i = 83
	# mlab.figure(mlab.gcf,bgcolor=(0,0,0),size=(800,800))
	# vol = mlab.pipeline.volume(mlab.pipeline.scalar_field(uu[i]), vmin=-0.1, vmax=0.8)
	# # mlab.pipeline.scalar_cut_plane(mlab.pipeline.scalar_field(uu[i]),plane_orientation='z_axes',contours=20)
	# mlab.show()

	# fig = plt.figure()
	# # ax = Axes3D(fig)
	# # # ax.set_zlim(-0,0.05)
	# ax = plt.axes(xlim=(0,NX), ylim=(0,NY))

	# # wireframe = ax.plot_surface(x, y, uu[0,1,x,y], rstride=2, cstride=2,cmap=cm.hot)
	# # wireframe = ax.plot_wireframe(x, y, uu[0,1,x,y],color="black",rstride=1, cstride=1)
	# wireframe = ax.contourf(x, y, uu[0,x,y],1)


	 
	# # # animation function.  This is called sequentially
	# def animate(i, ax, fig):
	# 	global x,y,uu
	# 	ax.cla()
	# 	# wireframe = ax.plot_surface(x, y, uu[i,x,y], rstride=2, cstride=2,cmap=cm.hot)
	# 	# wireframe = ax.plot_wireframe(x, y, uu[i,x,y],color="black",rstride=1, cstride=1)
	# 	# wireframe = ax.contourf(x, y, uu[i,x,y],100)
	# 	wireframe = ax.contourf(x, y, uu[i,1,x,y],100,vmin=amin(uu),vmax=amax(uu))
	# 	# ax.set_zlim(-0.0,0.05)
	# 	return wireframe,


	# anim = animation.FuncAnimation(fig, animate, frames=NZ, fargs=(ax, fig), interval=5)
	 
	# # # anim.save('3d_fdtd_nopml.gif', writer='imagemagick', fps=30)
	 
	# plt.show()
