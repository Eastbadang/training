Sub Main()
    Dim i As Integer
    Dim iSum As Integer

    for i=1 to 100 step 2
        iSum=iSum+i
    Next i
    MsgBox "1~100 중 홀수의 합 =" & iSum
End Sub
