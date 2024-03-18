Uses https://github.com/nolanbconaway/underground/tree/main

1. Create and .env file
2. Add MTA_API_KEY="Your mta api key"

Sub RemoveSpecificRowsFromDailyColumns()
    Dim ws As Worksheet
    Dim rng As Range
    Dim dailyColumn As Range
    Dim titleRow As Long
    Dim removeRows() As Integer
    Dim i As Integer
    
    ' Loop through each worksheet
    For Each ws In ThisWorkbook.Worksheets
        ' Find the title row containing "Daily"
        On Error Resume Next ' Resume next in case "Daily" is not found
        titleRow = ws.Rows(1).Find("Daily", LookIn:=xlValues, lookat:=xlWhole).Row
        On Error GoTo 0 ' Turn off error handling
        
        ' If "Daily" is found in the title row
        If titleRow > 0 Then
            ' Set the range for the entire column containing "Daily"
            Set dailyColumn = ws.Columns(titleRow)
            
            ' Loop through each cell in the column starting from row 2 (assuming row 1 is the title row)
            For Each rng In dailyColumn.Offset(1).Resize(ws.Cells(ws.Rows.Count, titleRow).End(xlUp).Row - 1)
                ' Check if the cell value meets the condition to be removed
                If rng.Value = "SpecificValueToRemove" Then
                    ' Record the row index to remove
                    ReDim Preserve removeRows(1 To i + 1)
                    removeRows(i + 1) = rng.Row
                    i = i + 1
                End If
            Next rng
            
            ' Delete the rows containing the specific value to remove
            If Not IsEmpty(removeRows) Then
                For i = UBound(removeRows) To LBound(removeRows) Step -1
                    ws.Rows(removeRows(i)).Delete
                Next i
            End If
        End If
    Next ws
End Sub

