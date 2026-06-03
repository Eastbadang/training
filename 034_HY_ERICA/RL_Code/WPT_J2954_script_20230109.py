# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 13:17:43  8 29, 2018
# ----------------------------------------------
import ScriptEnv
from Ferrite_choose import cube_count, Ferrite_change

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oDesktop.OpenProject("C:/Users/eunso/Desktop/WPT_J2954/1Barrak/base_model.aedt")
oProject = oDesktop.SetActiveProject("base_model")
oDesign = oProject.SetActiveDesign("1) CR WPT")
oEditor = oDesign.SetActiveEditor("3D Modeler")


# #############################################################################################
# until now, fixed code. we don't have to change upper code.
##############################################################################################
# explanation of this code
# target : we will get the number of cub(cube_number)
# 			and the index of Ferrite cubes (Ferrite_change). + RGB determination
# we should change the cubes to ferrite material from vacuum.
##############################################################################################

for i in range(cube_count):
    if Ferrite_change[i] == 0:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core1", "VA_core1_1", "VA_core1_2", "VA_core1_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core1", "VA_core1_1", "VA_core1_2", "VA_core1_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 1:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core2", "VA_core2_1", "VA_core2_2", "VA_core2_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core2", "VA_core2_1", "VA_core2_2", "VA_core2_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 2:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core3", "VA_core3_1", "VA_core3_2", "VA_core3_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core3", "VA_core3_1", "VA_core3_2", "VA_core3_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 3:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core4", "VA_core4_1", "VA_core4_2", "VA_core4_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core4", "VA_core4_1", "VA_core4_2", "VA_core4_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 4:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core5", "VA_core5_1", "VA_core5_2", "VA_core5_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core5", "VA_core5_1", "VA_core5_2", "VA_core5_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 5:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core6", "VA_core6_1", "VA_core6_2", "VA_core6_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core6", "VA_core6_1", "VA_core6_2", "VA_core6_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 6:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core7", "VA_core7_1", "VA_core7_2", "VA_core7_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core7", "VA_core7_1", "VA_core7_2", "VA_core7_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 7:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core8", "VA_core8_1", "VA_core8_2", "VA_core8_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core8", "VA_core8_1", "VA_core8_2", "VA_core8_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 8:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core9", "VA_core9_1", "VA_core9_2", "VA_core9_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core9", "VA_core9_1", "VA_core9_2", "VA_core9_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 9:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core10", "VA_core10_1", "VA_core10_2", "VA_core10_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core10", "VA_core10_1", "VA_core10_2", "VA_core10_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 10:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core11", "VA_core11_1", "VA_core11_2", "VA_core11_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core11", "VA_core11_1", "VA_core11_2", "VA_core11_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 11:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core12", "VA_core12_1", "VA_core12_2", "VA_core12_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core12", "VA_core12_1", "VA_core12_2", "VA_core12_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 12:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core13", "VA_core13_1", "VA_core13_2", "VA_core13_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core13", "VA_core13_1", "VA_core13_2", "VA_core13_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 13:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core14", "VA_core14_1", "VA_core14_2", "VA_core14_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core14", "VA_core14_1", "VA_core14_2", "VA_core14_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 14:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core15", "VA_core15_1", "VA_core15_2", "VA_core15_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core15", "VA_core15_1", "VA_core15_2", "VA_core15_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 15:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core16", "VA_core16_1", "VA_core16_2", "VA_core16_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core16", "VA_core16_1", "VA_core16_2", "VA_core16_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 16:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core17", "VA_core17_1", "VA_core17_2", "VA_core17_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core17", "VA_core17_1", "VA_core17_2", "VA_core17_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 17:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core18", "VA_core18_1", "VA_core18_2", "VA_core18_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core18", "VA_core18_1", "VA_core18_2", "VA_core18_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 18:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core19", "VA_core19_1", "VA_core19_2", "VA_core19_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core19", "VA_core19_1", "VA_core19_2", "VA_core19_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 19:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core20", "VA_core20_1", "VA_core20_2", "VA_core20_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core20", "VA_core20_1", "VA_core20_2", "VA_core20_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 20:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core21", "VA_core21_1", "VA_core21_2", "VA_core21_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core21", "VA_core21_1", "VA_core21_2", "VA_core21_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 21:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core22", "VA_core22_1", "VA_core22_2", "VA_core22_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core22", "VA_core22_1", "VA_core22_2", "VA_core22_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 22:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core23", "VA_core23_1", "VA_core23_2", "VA_core23_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core23", "VA_core23_1", "VA_core23_2", "VA_core23_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

    elif Ferrite_change[i] == 23:
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "VA_core24", "VA_core24_1", "VA_core24_2", "VA_core24_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Material",
                            "Value:="	, "\"ferrite\""
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
                        "VA_core24", "VA_core24_1", "VA_core24_2", "VA_core24_3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 143,
                            "G:="		, 143,
                            "B:="		, 175
                        ]
                    ]
                ]
            ])

# #############################################################################################
# ############################# end for #############################
# #############################################################################################

oProject = oDesktop.SetActiveProject("base_model")
oProject.SaveAs("C:/Users/SPEC/Desktop/WPT_J2954/1Barrak/model_result.aedt", True)
oProject = oDesktop.SetActiveProject("model_result")
oDesign = oProject.SetActiveDesign("1) CR WPT")
oModule = oDesign.GetModule("Optimetrics")
oModule.SolveSetup("Alignment")
oModule.SolveSetup("Misalignment")

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("L Plot 1", "EddyCurrent", "Rectangular Plot", "Setup1 : LastAdaptive",
                     [
                         "Context:=", "Matrix1"
                     ],
                     [
                         "Freq:="	, ["All"],
                         "a_bt:="		, ["Nominal"],
                         "b_bt:="		, ["Nominal"],
                         "d_bt:="		, ["Nominal"],
                         "a_btmm:="		, ["Nominal"],
                         "Hferrite_bt:="		, ["Nominal"],
                         "Xcoiltotal_bt:="	, ["Nominal"],
                         "Ycoiltotal_bt:="	, ["Nominal"],
                         "line_bt:="		, ["Nominal"],
                         "y_bt:="		, ["Nominal"],
                         "z_bt:="		, ["Nominal"],
                         "w_bt:="		, ["Nominal"],
                         "x_bt:="		, ["Nominal"],
                         "Xfetotal_bt:="		, ["Nominal"],
                         "Xhous_bt:="		, ["Nominal"],
                         "Yhous_bt:="		, ["Nominal"],
                         "Hhous_bt:="		, ["Nominal"],
                         "I1:="			, ["Nominal"],
                         "I2:="			, ["Nominal"],
                         "interval_Vs:="		, ["Nominal"],
                         "LITZTRAY_Vs:="		, ["Nominal"],
                         "Ldia_Vs:="		, ["Nominal"],
                         "Htray_Vs:="		, ["Nominal"],
                         "line_Vs:="		, ["Nominal"],
                         "Linter_Vs:="		, ["Nominal"],
                         "Yferrite_Vs:="		, ["Nominal"],
                         "Xferrite_Vs:="		, ["Nominal"],
                         "Zferrite_Vs:="		, ["Nominal"],
                         "Zalu_Vs:="		, ["Nominal"],
                         "Hhous_Vs:="		, ["Nominal"],
                         "Xalu_Vs:="		, ["Nominal"],
                         "Yalu_Vs:="		, ["Nominal"],
                         "dz:="			, ["All"],
                         "dx:="			, ["All"],
                         "dy:="			, ["All"]
                     ],
                     [
                         "X Component:="		, "Freq",
                         "Y Component:="		, ["abs(L(VA,GA))"]
                     ])
oModule.ExportToFile("L Plot 1", "C:/Users/SPEC/Desktop/WPT_J2954/1Barrak/M.csv")
oProject.SaveAs("C:/Users/SPEC/Desktop/WPT_J2954/1Barrak/model_result.aedt", True)

oDesktop.CloseProject("model_result")
oDesktop.QuitApplication()