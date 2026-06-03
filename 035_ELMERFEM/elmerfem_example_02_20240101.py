# Minimal sif file example Check Keywords Warn
Header :: Mesh DB "." "square"

Simulation
    Max Output Level = 5
    Coordinate System = Cartesian
    Simulation Type = Steady
    Output Intervals (1) = 1
    Steady State Max Iterations = 1
    Post File = "case.vtu"
End

Body 1
    Equation = 1
    Material = 1
End

Equation 1
    Active Solvers (1) = 1
End

Solver 1
    Equation = "HeatEq"
    Variable = "Temperature"
    Procedure = "HeatSolve" "HeatSolver"
    Linear System Solver = Direct
End

Material 1
    Heat Conductivity = 1.0
End

Boundary Condition 1
    Name = "Fixed"
    Target Boundaries (1) = 1
    Temperature = 0.0
End

Boundary Condition 2
    Name = "Flux"
    Target Boundaries (1) = 2
    Heat Flux = 1.0
End