# ElmerGrid를 사용하여 메시 생성
ElmerGrid 14 2
coil -autoclean

# ElmerSolver 입력 파일 작성
Header
    CHECK KEYWORDS Warn
    Mesh DB "." "."
    Include Path ""
    Results Directory ""
End

Simulation
    Max Output Level = 4
    Coordinate System = Cartesian
    Coordinate Mapping(3) = 1 2 3
    Simulation Type = Steady state
    Steady State Max Iterations = 1
    Output Intervals = 1
    Timestepping Method = BDF
    BDF Order = 1
    Solver Input File = case.sif
    Post File = case.ep
End

Body 1
    Equation = 1
    Material = 1
    Body Force = 1
End

Solver 1
    Equation = Result Output
    Procedure = "ResultOutputSolve" "ResultOutputSolver"
    Output File Name = case
    Output Format = Vtu
    Scalar Field 1 = Potential
    Vector Field 1 = Current Density
    Vector Field 2 = Magnetic Flux Density
End

Equation 1
    Active Solvers(2) = 1 2
End

Material 1
    Relative Permeability = 1.0
    Electric Conductivity = 5.96e7
    Heat expansion Coefficient = 0
    Heat Conductivity = 1
    Heat Capacity = 1
    Density = 1
    Relative Permittivity = 1
End

Body Force 1
    Current Density 1 = Real MATC "8.68e6*tx"
End