' sample

Sub Main ()


'## Merged Block - define units
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Units 
     .Geometry "mm" 
     .Frequency "GHz" 
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

'## Merged Block - change solver type
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
ChangeSolverType "HF Frequency Domain"

'## Merged Block - new component: component1
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
Component.New "component1"

'## Merged Block - define brick: component1:GROUND
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Brick
     .Reset 
     .Name "GROUND" 
     .Component "component1" 
     .Material "PEC" 
     .Xrange "-size_x/2", "size_x/2" 
     .Yrange "-size_y/2", "size_y/2" 
     .Zrange "-h-t_pec", "-h" 
     .Create
End With

'## Merged Block - define brick: component1:LINE
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Brick
     .Reset 
     .Name "LINE" 
     .Component "component1" 
     .Material "PEC" 
     .Xrange "-dw/2", "dw/2" 
     .Yrange "dg/2", "dl/2" 
     .Zrange "t", "t" 
     .Create
End With

'## Merged Block - transform: mirror component1:LINE
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Transform 
     .Reset 
     .Name "component1:LINE" 
     .Origin "Free" 
     .Center "0", "0", "0" 
     .PlaneNormal "0", "1", "0" 
     .MultipleObjects "True" 
     .GroupObjects "False" 
     .Repetitions "1" 
     .MultipleSelection "False" 
     .Destination "" 
     .Material "" 
     .Transform "Shape", "Mirror" 
End With

'## Merged Block - pick edge
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
Pick.PickEdgeFromId "component1:LINE_1", "4", "4"

'## Merged Block - pick edge
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
Pick.PickEdgeFromId "component1:LINE", "4", "4"

'## Merged Block - define discrete face port: 1
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With DiscreteFacePort 
     .Reset 
     .PortNumber "1" 
     .Type "SParameter" 
     .Label "" 
     .Folder "" 
     .Impedance "50.0" 
     .VoltagePortImpedance "0.0" 
     .VoltageAmplitude "1.0" 
     .CurrentAmplitude "1.0" 
     .SetP1 "True", "0", "-1", "0" 
     .SetP2 "True", "0", "1", "0" 
     .LocalCoordinates "False" 
     .InvertDirection "False" 
     .CenterEdge "True" 
     .Monitor "True" 
     .UseProjection "False" 
     .ReverseProjection "False" 
     .FaceType "Linear" 
     .Create 
End With

'## Merged Block - define frequency range
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
Solver.FrequencyRange "2.9", "3.1"

'## Merged Block - define background
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Background 
     .ResetBackground 
     .XminSpace "0.0" 
     .XmaxSpace "0.0" 
     .YminSpace "0.0" 
     .YmaxSpace "0.0" 
     .ZminSpace "0.0" 
     .ZmaxSpace "0.0" 
     .ApplyInAllDirections "True" 
End With 
With Material 
     .Reset 
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
     .MaterialUnit "Frequency", "Hz"
     .MaterialUnit "Geometry", "m"
     .MaterialUnit "Time", "s"
     .MaterialUnit "Temperature", "Kelvin"
     .Epsilon "1.0"
     .Mu "1.0"
     .Sigma "0"
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

'## Merged Block - define boundaries
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Boundary
     .Xmin "periodic"
     .Xmax "periodic"
     .Ymin "expanded open"
     .Ymax "expanded open"
     .Zmin "expanded open"
     .Zmax "expanded open"
     .Xsymmetry "none"
     .Ysymmetry "electric"
     .Zsymmetry "none"
     .ApplyInAllDirections "False"
     .OpenAddSpaceFactor "0.5"
     .XPeriodicShift "0.0"
     .YPeriodicShift "0.0"
     .ZPeriodicShift "0.0"
     .PeriodicUseConstantAngles "True"
     .SetPeriodicBoundaryAngles "theta", "0.0"
     .SetPeriodicBoundaryAnglesDirection "outward"
End With

'## Merged Block - set mesh properties (Tetrahedral)
StartVersionStringOverrideMode "2020.7|29.0.1|20200710" 
With Mesh 
     .MeshType "Tetrahedral" 
     .SetCreator "High Frequency"
End With 
With MeshSettings 
     .SetMeshType "Tet" 
     .Set "Version", 1%
     'MAX CELL - WAVELENGTH REFINEMENT 
     .Set "StepsPerWaveNear", "4" 
     .Set "StepsPerWaveFar", "4" 
     .Set "PhaseErrorNear", "0.02" 
     .Set "PhaseErrorFar", "0.02" 
     .Set "CellsPerWavelengthPolicy", "automatic" 
     'MAX CELL - GEOMETRY REFINEMENT 
     .Set "StepsPerBoxNear", "12" 
     .Set "StepsPerBoxFar", "8" 
     .Set "ModelBoxDescrNear", "maxedge" 
     .Set "ModelBoxDescrFar", "maxedge" 
     'MIN CELL 
     .Set "UseRatioLimit", "0" 
     .Set "RatioLimit", "100" 
     .Set "MinStep", "0" 
     'MESHING METHOD 
     .SetMeshType "Unstr" 
     .Set "Method", "0" 
End With 
With MeshSettings 
     .SetMeshType "Tet" 
     .Set "CurvatureOrder", "1" 
     .Set "CurvatureOrderPolicy", "automatic" 
     .Set "CurvRefinementControl", "NormalTolerance" 
     .Set "NormalTolerance", "22.5" 
     .Set "SrfMeshGradation", "1.5" 
     .Set "SrfMeshOptimization", "1" 
End With 
With MeshSettings 
     .SetMeshType "Unstr" 
     .Set "UseMaterials",  "1" 
     .Set "MoveMesh", "0" 
End With 
With MeshSettings 
     .SetMeshType "All" 
     .Set "AutomaticEdgeRefinement",  "0" 
End With 
With MeshSettings 
     .SetMeshType "Tet" 
     .Set "UseAnisoCurveRefinement", "1" 
     .Set "UseSameSrfAndVolMeshGradation", "1" 
     .Set "VolMeshGradation", "1.5" 
     .Set "VolMeshOptimization", "1" 
End With 
With MeshSettings 
     .SetMeshType "Unstr" 
     .Set "SmallFeatureSize", "0" 
     .Set "CoincidenceTolerance", "1e-06" 
     .Set "SelfIntersectionCheck", "1" 
     .Set "OptimizeForPlanarStructures", "0" 
End With 
With Mesh 
     .SetParallelMesherMode "Tet", "maximum" 
     .SetMaxParallelMesherThreads "Tet", "1" 
End With 
StopVersionStringOverrideMode 
End Sub
