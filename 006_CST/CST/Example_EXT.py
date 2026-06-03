import win32com.client
import comtypes
#import win32com.client.gencache

import win32com.client as com
import threading
import pythoncom

import os
import os.path
import datetime
import time

#import sys


# Run CST STUDIO SUITE
cst = win32com.client.Dispatch('CSTStudio.application')

# New PROJECT
print("New Project")
ems = cst.NewEMS()

# Define Active Project
print("Define Active Project")
# CST Microwave Studio, CST EM Studio, CST Particle Studio,
# CST Mphysics Studio or CST Cable Studio project.
cst.Active3D
# CST Design Studio project.
# ems.ActiveDS

# New Project Save
print("SaveAs Project")
ems._FlagAsMethod("SaveAs")
ems.SaveAs('c:/works/cst/a11E.cst','False')

# Define Prameter Handling

ss_x = 10;
ss_y = 10;
ss_z =1;

ems._FlagAsMethod("StoreParameter")
ems.StoreParameter("ss_x", str(ss_x))
ems._FlagAsMethod("StoreParameter")
ems.StoreParameter("ss_y", str(ss_y))
ems._FlagAsMethod("StoreParameter")
ems.StoreParameter("ss_z", str(ss_z))

print("Define Material")
setMaterialFerrite = """
With Material 
     .Reset 
     .Name "Ferrite"
     .Folder ""
     .Rho "0.0"
     .ThermalType "Normal"
     .ThermalConductivity "0"
     .SpecificHeat "0", "J/K/kg"
     .DynamicViscosity "0"
     .Emissivity "0"
     .MetabolicRate "0.0"
     .VoxelConvection "0.0"
     .BloodFlow "0"
     .MechanicsType "Unused"
     .FrqType "all"
     .Type "Normal"
     .MaterialUnit "Frequency", "kHz"
     .MaterialUnit "Geometry", "mm"
     .MaterialUnit "Time", "s"
     .MaterialUnit "Temperature", "Celsius"
     .Epsilon "1"
     .Mu "3000"
     .Sigma "0"
     .TanD "0.0"
     .TanDFreq "0.0"
     .TanDGiven "False"
     .TanDModel "ConstTanD"
     .EnableUserConstTanDModelOrderEps "False"
     .ConstTanDModelOrderEps "1"
     .SetElParametricConductivity "False"
     .ReferenceCoordSystem "Global"
     .CoordSystemType "Cartesian"
     .SigmaM "0"
     .TanDM "0.0"
     .TanDMFreq "0.0"
     .TanDMGiven "False"
     .TanDMModel "ConstTanD"
     .EnableUserConstTanDModelOrderMu "False"
     .ConstTanDModelOrderMu "1"
     .SetMagParametricConductivity "False"
     .DispModelEps  "None"
     .DispModelMu "None"
     .DispersiveFittingSchemeEps "Nth Order"
     .MaximalOrderNthModelFitEps "10"
     .ErrorLimitNthModelFitEps "0.1"
     .UseOnlyDataInSimFreqRangeNthModelEps "False"
     .DispersiveFittingSchemeMu "Nth Order"
     .MaximalOrderNthModelFitMu "10"
     .ErrorLimitNthModelFitMu "0.1"
     .UseOnlyDataInSimFreqRangeNthModelMu "False"
     .UseGeneralDispersionEps "False"
     .UseGeneralDispersionMu "False"
     .NLAnisotropy "False"
     .NLAStackingFactor "1"
     .NLADirectionX "1"
     .NLADirectionY "0"
     .NLADirectionZ "0"
     .Colour "0", "1", "1" 
     .Wireframe "False" 
     .Reflection "False" 
     .Allowoutline "True" 
     .Transparentoutline "False" 
     .Transparency "0" 
     .Create
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define material", setMaterialFerrite)

# New Component
print("new component")
setNewComponent = """
Component.New "component1" 
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("new component", setNewComponent)

# Define Brick
print("define brick")
setBrick1 = """
With Brick
     .Reset 
     .Name "Shielding Sheet" 
     .Component "component1" 
     .Material "Ferrite" 
     .Xrange "-ss_x/2", "ss_x/2" 
     .Yrange "-ss_y/2", "ss_y/2" 
     .Zrange "-ss_z", "0" 
     .Create
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define brick", setBrick1)