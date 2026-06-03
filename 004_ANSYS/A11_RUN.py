import sys
#sys.path.append(r"C:/Anaconda3/envs/py38/")
sys.path.append(r"C:/Program Files/AnsysEM/AnsysEM20.2/Win64")

from win32com import client

oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
oDesktop = oAnsoftApp.GetAppDesktop()
oProject = oDesktop.NewProject()
oProject.SaveAs("C:\\Works\\ANSOFT\\2020R2\\test.aedt", True)
oProject.InsertDesign("Maxwell 3D", "Maxwell3DDesign1", "Magnetostatic", "")
oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0.4mm",
		"ZStart:="		, "0mm",
		"Width:="		, "0.6mm",
		"Height:="		, "-0.1mm",
		"WhichAxis:="		, "X"
	],
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "A11_COIL"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers",
				"A11_COIL:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0mm",
					"Y:="			, "10mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:YSize",
					"Value:="		, "22mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "-1.25mm"
				]
			]
		]
	])
oEditor.SweepAroundAxis(
	[
		"NAME:Selections",
		"Selections:="		, "A11_COIL",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:AxisSweepParameters",
		"DraftAngle:="		, "0deg",
		"DraftType:="		, "Round",
		"CheckFaceFaceIntersection:=", False,
		"SweepAxis:="		, "Z",
		"SweepAngle:="		, "360deg",
		"NumOfSegments:="	, "0"
	])
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "A11_COIL"
	],
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"A11_COIL"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 64
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-25mm",
		"YPosition:="		, "-25mm",
		"ZPosition:="		, "-1.25mm",
		"XSize:="		, "50mm",
		"YSize:="		, "50mm",
		"ZSize:="		, "-1mm"
	],
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Shielding_Sheet"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Shielding_Sheet"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"ferrite\""
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Shielding_Sheet"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 0,
					"B:="			, 0
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers",
				"A11_COIL:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "12mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-100mm",
		"YPosition:="		, "-100mm",
		"ZPosition:="		, "-100mm",
		"XSize:="		, "200mm",
		"YSize:="		, "200mm",
		"ZSize:="		, "200mm"
	],
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Region"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Region"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 255,
					"B:="			, 255
				]
			]
		]
	])
oEditor.Section(
	[
		"NAME:Selections",
		"Selections:="		, "A11_COIL",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:SectionToParameters",
		"CreateNewObjects:="	, True,
		"SectionPlane:="	, "YZ",
		"SectionCrossObject:="	, False
	])
oEditor.Split(
	[
		"NAME:Selections",
		"Selections:="		, "A11_COIL_Section1",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:SplitToParameters",
		"SplitPlane:="		, "ZX",
		"WhichSide:="		, "PositiveOnly",
		"ToolType:="		, "PlaneTool",
		"ToolEntityID:="	, -1,
		"SplitCrossingObjectsOnly:=", False,
		"DeleteInvalidObjects:=", True
	])
oDesign.SetSolutionType("EddyCurrent")
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWindingGroup(
	[
		"NAME:Winding1",
		"Type:="		, "Current",
		"IsSolid:="		, False,
		"Current:="		, "(1*10) A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.AssignCoilTerminal(
	[
		"NAME:CoilTerminal1",
		"Objects:="		, ["A11_COIL_Section1"],
		"Conductor number:="	, "10",
		"Point out of terminal:=", False
	])
oModule.AddWindingTerminals("Winding1", ["CoilTerminal1"])
oModule = oDesign.GetModule("MaxwellParameterSetup")
oModule.AssignMatrix(
	[
		"NAME:Matrix1",
		[
			"NAME:MatrixEntry",
			[
				"NAME:MatrixEntry",
				"Source:="		, "Winding1"
			]
		]
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("EddyCurrent",
	[
		"NAME:Setup1",
		"Enabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"MaximumPasses:="	, 20,
		"MinimumPasses:="	, 2,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"SolveFieldOnly:="	, False,
		"PercentError:="	, 0.5,
		"SolveMatrixAtLast:="	, True,
		"CacheSaveKind:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "100kHz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
		"UseMuLink:="		, False
	])
oProject.Save()
oDesign.Analyze("Setup1")
oProject.Save()
oDesktop.CloseProject("test")

oDesktop.QuitApplication()
