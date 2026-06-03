import sys
import pygame
from pygame.locals import *
import ode

screen_width = 1920
screen_height = 1080

def coord(x,y):
	# "convert world coords to screen (pixel) coords"
	return int(screen_width/2.+screen_width/4.*x), int(screen_height/1.5-screen_height/4.*y)

def coordx(x):
	return int(screen_width/2.+screen_width/4.*x)

def coordy(y):
	int(screen_height/1.5-screen_height/4.*y)

def buildObjects():
	world = ode.World()
	world.setGravity((0,-9.81,0))
	space = ode.Space()
	geoms = []
	floor = ode.GeomPlane(space, (0,1,0), -2)
	geoms.append(floor)

	mass1 = ode.Body(world)
	M = ode.Mass()
	M.setSphere(2500, 0.05)
	mass1.setMass(M)
	mass1.setPosition((1,2,0))

	mass2 = ode.Body(world)
	M = ode.Mass()
	M.setSphere(2500, 0.1)
	mass2.setMass(M)
	mass2.setPosition((2,2,0))
	mass2.shape = "sphere"
	mass2.spheresize = 0.1
	geom1 = ode.GeomSphere(space, mass2.spheresize)
	geom1.setBody(mass2)
	geoms.append(geom1)

	joint1 = ode.HingeJoint(world)
	joint1.attach(mass1, ode.environment)
	joint1.setAnchor((0,2,0))
	joint1.setAxis((0,0,1))

	joint2 = ode.HingeJoint(world)
	joint2.attach(mass1,mass2)
	joint2.setAnchor((1,2,0))
	joint2.setAxis((0,0,1))

	wall = ode.Body(world)
	M = ode.Mass()
	M.setBox(50,1,4,1)
	wall.setMass(M)
	wall.setPosition((-1,0,0))
	wall.shape = "box"
	wall.boxsize = (1,4,1)
	geom2 = ode.GeomBox(space,lengths=wall.boxsize)
	geom2.setBody(wall)
	geoms.append(geom2)
	# wall.setGravityMode(False)

	contactgroup = ode.JointGroup()

	return world, mass1, mass2, joint1, joint2, wall, space, contactgroup, geoms

def near_callback(args, geom1, geom2):
	contacts = ode.collide(geom1, geom2)

	world,contactgroup = args
	for c in contacts:
		c.setBounce(0.2)
		c.setMu(5000)
		j = ode.ContactJoint(world, contactgroup, c)
		j.attach(geom1.getBody(), geom2.getBody())

def simulate(world, mass1, mass2, wall, space, contactgroup, geoms):
	pygame.init()
	dsply = pygame.display.set_mode((screen_width,screen_height))
	clk = pygame.time.Clock()

	fps = 50
	dt = 1./fps
	loopFlag = True
	while loopFlag:
		events = pygame.event.get()
		for e in events:
			if e.type == QUIT:
				loopFlag = False

		#clear
		dsply.fill((255,255,255))
		x1,y1,z1 = mass1.getPosition()
		x2,y2,z2 = mass2.getPosition()
		x3,y3,z3 = wall.getPosition()

		bodyColor = (0,0,0)
		r = 20
		lw = 2
		pygame.draw.circle(dsply, bodyColor, coord(x1,y1), int(0.05*screen_width/4.), 0)
		pygame.draw.circle(dsply, bodyColor, coord(x2,y2), int(mass2.spheresize*screen_width/4.), 0)
		pygame.draw.line(dsply, bodyColor, coord(0,2), coord(x1,y1), lw)
		pygame.draw.line(dsply, bodyColor, coord(x1,y1), coord(x2,y2), lw)
		pygame.draw.line(dsply, bodyColor, coord(x3,y3-2), coord(x3,y3+2), int(1*screen_width/4.))
		# box = pygame.Rect(coordx(x3-1/2.),coordy(y3-4/2.),1*screen_width/4.,4*screen_height/4.)
		# pygame.draw.rect(dsply, bodyColor, box, 0)

		pygame.display.flip() #update display

		space.collide((world,contactgroup),near_callback)
		world.step(dt)
		clk.tick(fps)
		contactgroup.empty()

world, mass1, mass2, joint1, joint2, wall, space, contactgroup, geoms = buildObjects()
simulate(world, mass1, mass2, wall, space, contactgroup, geoms)
