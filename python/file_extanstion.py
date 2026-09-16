File=input("enter your  file extension : ")
if File==".exe"  or  File==".bat":
    print( "High Risk - Scan Required" )
elif File==".pdf" or File==".docx":
    print( "Medium Risk - Check Macros")
else:
    print( "Low Risk" )