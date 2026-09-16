P=int(input( " enter your port : " ))
if P==80  or P==443:
    print( "Web Traffic - Allowed" )
elif P==22:
    print( "SSH - Restricted Access" )
else :
    print( "Unknown Port - Blocked" )
