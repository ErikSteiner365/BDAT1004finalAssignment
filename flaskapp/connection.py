import pyodbc as dbc

connection = """Driver={SQL Server Native Client 11.0};Server=bdat1004.database.windows.net;Database=finalassignmentdjango;UID=BDATuser;PWD=I76VS6Pun?;"""
#connection = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:bdat1004.database.windows.net,1433;Database=finalassignmentdjango;Uid=BDATuser;Pwd=I76VS6Pun?;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

conn = dbc.connect(connection)
cursor =  conn.cursor()
