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

# New Project Save
print("SaveAs Project")
ems._FlagAsMethod("SaveAs")
ems.SaveAs('c:/works/cst/a11.cst','False')

# Define Solver(LF, HF, ... )
print("Define Solver")
setSolver = """
ChangeSolverType "LF Frequency Domain" 
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("change solver type", setSolver)

# Define Units
print("Define Units")
setUnits = """
With Units 
     .Geometry "mm" 
     .Frequency "kHz" 
     .Time "s" 
     .TemperatureUnit "Celsius" 
     .Voltage "V" 
     .Current "A" 
     .Resistance "Ohm" 
     .Conductance "Siemens" 
     .Capacitance "PikoF" 
     .Inductance "NanoH" 
     .SetResultUnit "frequency", "frequency", "" 
End With 
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define units", setUnits)

# Define Curve
print("Define Curve Circle")
setCurveCircle = """
With Circle
     .Reset 
     .Name "Inner_Loop" 
     .Curve "curve1" 
     .Radius "9.5" 
     .Xcenter "0" 
     .Ycenter "0" 
     .Segments "0" 
     .Create
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define curve circle", setCurveCircle)

print("Define Curve 3dpolygon")
setCurve3dpolygon = """
With Polygon3D 
     .Reset 
     .Version 10 
     .Name "Coil" 
     .Curve "curve1" 
     .Point "9.5", "0", "0" 
     .Point "22", "0", "0" 
     .Point "22", "0", "-1.25" 
     .Point "9.5", "0", "-1.25" 
     .Point "9.5", "0", "0" 
     .Create 
End With 
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define curve 3dpolygon", setCurve3dpolygon)

print("Define Coil")
setCoil = """
With Coil
     .Reset
     .Name "A11"
     .Type "Coil"
     .OperationMode "Current"
     .ConductorModel "Stranded"
     .ToolType "CurveCurve"
     .Value "1"
     .Phase "0.0"
     .NTurns "10"
     .Resistance "0.0"
     .CurrentDirection "Regular"
     .ProjectProfileToPathAdvanced "True"
     .ProfileName "curve1:Coil"
     .PathName "curve1:Inner_Loop"
     .Create
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define coil", setCoil)

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
     .Xrange "-24", "24" 
     .Yrange "-24", "24" 
     .Zrange "-2.26", "-1.26" 
     .Create
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define brick", setBrick1)

# Define LF solver frequency settings
print("define lf solver frequency settings")
setFrequency = """
With LFSolver
     .ResetFrequencySettings 
     .AddFrequency "100" 
     .AddFrequency "120" 
     .AddFrequency "140" 
     .AddFrequency "160" 
     .AddFrequency "180" 
     .AddFrequency "200" 
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define frequency", setFrequency)

# Define Background
print("define background")
setBackground = """
With Background 
     .ResetBackground 
     .XminSpace "100" 
     .XmaxSpace "100" 
     .YminSpace "100" 
     .YmaxSpace "100" 
     .ZminSpace "100" 
     .ZmaxSpace "100" 
     .ApplyInAllDirections "True" 
End With 

With Material 
     .Reset 
     .Rho "1.204"
     .ThermalType "Normal"
     .ThermalConductivity "0.026"
     .SpecificHeat "1005", "J/K/kg"
     .DynamicViscosity "1.84e-5"
     .Emissivity "0.0"
     .MetabolicRate "0.0"
     .VoxelConvection "0.0"
     .BloodFlow "0"
     .MechanicsType "Unused"
     .FrqType "all"
     .Type "Normal"
     .MaterialUnit "Frequency", "Hz"
     .MaterialUnit "Geometry", "m"
     .MaterialUnit "Time", "s"
     .MaterialUnit "Temperature", "Kelvin"
     .Epsilon "1.00059"
     .Mu "1.0"
     .Sigma "0.0"
     .TanD "0.0"
     .TanDFreq "0.0"
     .TanDGiven "False"
     .TanDModel "ConstSigma"
     .EnableUserConstTanDModelOrderEps "False"
     .ConstTanDModelOrderEps "1"
     .SetElParametricConductivity "False"
     .ReferenceCoordSystem "Global"
     .CoordSystemType "Cartesian"
     .SigmaM "0"
     .TanDM "0.0"
     .TanDMFreq "0.0"
     .TanDMGiven "False"
     .TanDMModel "ConstSigma"
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
     .Colour "0.6", "0.6", "0.6" 
     .Wireframe "False" 
     .Reflection "False" 
     .Allowoutline "True" 
     .Transparentoutline "False" 
     .Transparency "0" 
     .ChangeBackgroundMaterial
End With 
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define background", setBackground)

# Define Boundaries
print("define Boundaries")
setBoundary = """
With Boundary
     .Xmin "open"
     .Xmax "open"
     .Ymin "open"
     .Ymax "open"
     .Zmin "open"
     .Zmax "open"
     .Xsymmetry "none"
     .Ysymmetry "none"
     .Zsymmetry "none"
     .ApplyInAllDirections "True"
End With
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define boundaries", setBoundary)

# Define lf frequency domain solver parameters
print("define lf frequency domain solver parameters")
setSolverParameter = """
With LFSolver
     .Reset
     .Method "Tetrahedral Mesh"
     .Accuracy "1e-6"
     .CalcImpedanceMatrix "True"
     .StoreResultsInCache "False"
     .MeshAdaption "0"
     .EquationType "Magnetoquasistatic"
     .ValueScaling "rms"
     .TetAdaption "True"
     .TetAdaptionMinCycles "2"
     .TetAdaptionMaxCycles "6"
     .TetAdaptionAccuracy "0.01"
     .TetAdaptionRefinementPercentage "10"
     .SnapToGeometry "True"
     .MaxLinIter "0"
     .Preconditioner "ILU"
     .SetTreeCotreeGauging "True"
     .EnableDivergenceCheck "True"
     .LSESolverType "Auto"
     .BroadbandCalculation "False"
     .NonlinearEquivalentMu "False"
     .TetSolverOrder "2"
     .UseMaxNumberOfThreads "True"
     .MaxNumberOfThreads "128"
     .MaximumNumberOfCPUDevices "2"
     .UseDistributedComputing "False"
End With
UseDistributedComputingForParameters "False"
MaxNumberOfDistributedComputingParameters "2"
UseDistributedComputingMemorySetting "False"
MinDistributedComputingMemoryLimit "0"
UseDistributedComputingSharedDirectory "False"
"""
ems._FlagAsMethod("AddToHistory")
ems.AddToHistory("define solver parameter", setSolverParameter)

# Run Solver
print("Run Solver")
ems._FlagAsMethod("RunSolver")
ems.RunSolver()

# Project Save
print("Save Project")
ems._FlagAsMethod("Save")
ems.Save()

# Close Project
print("Close Project")
ems._FlagAsMethod("Quit")
ems.Quit()

# Quit CST STUDIO SUITE
print("Quit CST STUDIO SUITE")
time.sleep(5)
print("Good Bye")
cst.quit()
