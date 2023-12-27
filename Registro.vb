Imports MySql.Data.MySqlClient
Public Class Registro
    Dim conexion1 As New MySqlConnection
    Dim miconexion As New Conexion

    Private Sub Btn_Ingresar_Click(sender As Object, e As EventArgs) Handles Btn_Ingresar.Click
        Login.Show()
        Me.Close()
    End Sub

    Private Sub Btn_Registrar_Click(sender As Object, e As EventArgs) Handles Btn_Registrar.Click
        Dim rango As String
        rango = ComboBox1.SelectedItem.ToString
        Dim Fecha As String = DateTime.Now.ToString("yyyy-MM-dd")
        Try
            If txb_Usuario.Text = "" Or Mtbx_Contra.Text = "" Then
                MsgBox("Los campos no pueden estar vacios")
                Return
            End If

            If conexion1.State = ConnectionState.Closed Then
                conexion1 = Conexion.Conectar()
            End If

            Dim query As String = String.Empty
            query = "SELECT * FROM datauser WHERE usuario='" & txb_Usuario.Text & "' LIMIT 1;"

            Dim query2 As String = String.Empty
            query2 = "INSERT INTO `datauser`(`usuario`, `contraseña`, `rango`) VALUES ('" & txb_Usuario.Text & "','" & Mtbx_Contra.Text & "','" & rango & "')"

            Dim query3 As String = String.Empty
            query3 = "INSERT INTO `historial`(`fecha`, `hora`, `accion`, `usuario`) VALUES ('" & DateTime.Now.ToString("yyyyMMdd") & "','" & TimeOfDay & "','Registro','" & txb_Usuario.Text & "')"

            Dim mysqlcommand As MySqlCommand
            mysqlcommand = New MySqlCommand(query, conexion1)

            Dim mysqlcommand2 As MySqlCommand
            mysqlcommand2 = New MySqlCommand(query2, conexion1)

            Dim mysqlcommand3 As MySqlCommand
            mysqlcommand3 = New MySqlCommand(query3, conexion1)

            Dim cantidad As MySqlDataReader
            cantidad = mysqlcommand.ExecuteReader
            If cantidad.HasRows Then
                MsgBox("Usuario no disponible")
            Else
                conexion1.Close()
                conexion1.Open()
                mysqlcommand2.ExecuteNonQuery()
                mysqlcommand3.ExecuteNonQuery()
                MsgBox("Registro Completado")
                conexion1.Close()
            End If
        Catch ex As Exception
            MsgBox(ex.Message)

        Finally
            conexion1.Dispose()
        End Try
    End Sub
End Class