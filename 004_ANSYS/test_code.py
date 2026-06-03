import sys

sys.path.append(r"C:\Program Files\AnsysEM\AnsysEM20.2\Win64")

sys.path.append(r"C:\Program Files\AnsysEM\AnsysEM20.2\Win64\PythonFiles\DesktopPlugin")

import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()

oProject = oDesktop.NewProject()

oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")

oDesign = oProject.SetActiveDesign("HFSSDesign1")

oEditor = oDesign.SetActiveEditor("3D Modeler")

oEditor.CreateRectangle(

    [

        "NAME:RectangleParameters",

        "IsCovered:= ", True,

        "XStart:= ", "-0.2mm",

        "YStart:= ", "-3mm",

        "ZStart:= ", "0mm",

        "Width:= ", "0.8mm",

        "Height:= ", "1.2mm",

        "WhichAxis:= ", "Z"

    ],

    [

        "NAME:Attributes",

        "Name:= ", "Rectangle1",

        "Flags:= ", "",

        "Color:= ", "(132 132 193)",

        "Transparency:= ", 0,

        "PartCoordinateSystem:=", "Global",

        "UDMId:= ", "",

        "MaterialValue:= ", "\"vacuum\"",

        "SolveInside:= ", True

    ])

oDesign.SetDesignSettings(
    ['NAME:Design Settings Data', 'Allow Material Override:=', True, 'Calculate Lossy Dielectrics:=', True])

oEditor.SetModelUnits(['NAME:Units Parameter', 'Units:=', 'mil', 'Rescale:=', False])

ScriptEnv.Shutdown()