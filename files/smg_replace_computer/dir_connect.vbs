Dim objNet, strUserName,chkname,ofs,oDrives,s,j
Dim AllDrives, AlreadyConnected, i
Dim shell

set objNet=CreateObject("Wscript.Network")

Set oFS = Wscript.CreateObject("Scripting.FileSystemObject") 
          'Loop thru A-Z. If found, exit early.     
Set oDrives = oFS.Drives 
Set AllDrives=objNet.EnumNetworkDrives()   



 Function isNetworkDrive (inDrive)
    isNetworkDrive = false
    For Each Drive in oDrives   
    	s =Drive.DriveLetter  
        s=ucase(s) & ":"   
        If s = inDrive then        
            j = Drive.DriveType
            if j= 3 then
              isNetworkDrive = true
            end if   
        end if    
    Next    
 End Function
 
 Function DriveExist (inDrive)  
     DriveExist=false
  	 For Each Drive in oDrives 
        s =Drive.DriveLetter  
        s=ucase(s) & ":"   
        If s = inDrive then 
         	DriveExist=true
        end if    
     Next    	               
End Function 


strUserName=objNet.Username   

'For amo_user1, amo_user2 and amo_user3
if ucase(strusername)="AMO_USER1" or ucase(strusername)="AMO_USER2" or ucase(strusername)="AMO_USER3"  then
	if DriveExist("Q:") then    
		if isNetworkDrive ("Q:") then    
   			objNet.RemoveNetworkDrive ("Q:") 
	   		objNet.MapNetworkDrive "Q:", "\\dcs001\datacenter" 
		   end if	
	else   	
		objNet.MapNetworkDrive "Q:", "\\dcs001\datacenter" 
	end if
	if DriveExist("M:") then    
		if isNetworkDrive ("M:") then    
   			objNet.RemoveNetworkDrive ("M:") 
	   		objNet.MapNetworkDrive "M:", "\\wvs001\tempdsk" 
		   end if	
	else   	
		objNet.MapNetworkDrive "M:", "\\wvs001\tempdsk" 
	end if
	WScript.Quit
end if



if DriveExist("F:") then    
   if isNetworkDrive ("F:") then    
   		objNet.RemoveNetworkDrive ("F:") 
   		objNet.MapNetworkDrive "F:", "\\wvs001\smgdata" 
   end if	
else   	
	objNet.MapNetworkDrive "F:", "\\wvs001\smgdata" 
end if   


   
if DriveExist("L:") then    
   if isNetworkDrive ("L:") then  
	objNet.RemoveNetworkDrive ("L:") 
   end if
end if	

if DriveExist("Z:") then    
   if isNetworkDrive ("Z:") then  
	objNet.RemoveNetworkDrive ("Z:") 
   end if
end if

if DriveExist("J:") then    
   if isNetworkDrive ("J:") then  
	objNet.RemoveNetworkDrive ("J:") 
   end if
end if	

   
if DriveExist("G:") then    
   if isNetworkDrive ("G:") then    
    		objNet.RemoveNetworkDrive ("G:") 
'    		objNet.MapNetworkDrive "G:", "\\inf01\met" 
   end if
end if	


if DriveExist("M:") then    
   if isNetworkDrive ("M:") then    
   		objNet.RemoveNetworkDrive ("M:") 
   		objNet.MapNetworkDrive "M:", "\\wvs001\tempdsk" 
   end if	
else   	
	objNet.MapNetworkDrive "M:", "\\wvs001\tempdsk" 
end if  


if DriveExist("V:") then    
   if isNetworkDrive ("V:") then    
   		objNet.RemoveNetworkDrive ("V:") 
   		objNet.MapNetworkDrive "V:", "\\wvs001\common" 
   end if	
else   	
	objNet.MapNetworkDrive "V:", "\\wvs001\common" 
end if  

if DriveExist("W:") then    
   if isNetworkDrive ("W:") then    
   		objNet.RemoveNetworkDrive ("W:") 
   		objNet.MapNetworkDrive "W:", "\\wvs001\gtsdata" 
   end if	
else   	
	objNet.MapNetworkDrive "W:", "\\wvs001\gtsdata" 
end if 

if (ucase(right(strusername,4)) <>"MAIN") or (ucase(strusername) <> "DANIEL")  or (ucase(strusername) <> "KENTAM") Then
	
	if DriveExist("Q:") then    
   		if isNetworkDrive ("Q:") then    
   			objNet.RemoveNetworkDrive ("Q:") 
   			objNet.MapNetworkDrive "Q:", "\\dcs001\datacenter" 
   		end if	
	else   	
		objNet.MapNetworkDrive "Q:", "\\dcs001\datacenter" 
	end If

end if

'if DriveExist("K:") then    
'   if isNetworkDrive ("K:") then    
'   		objNet.RemoveNetworkDrive ("K:") 
'   		objNet.MapNetworkDrive "K:", "\\wvs001\pdata" 
'   end if	
'else   	
'	objNet.MapNetworkDrive "K:", "\\wvs001\pdata" 
'end if

if DriveExist("X:") then    
   if isNetworkDrive ("X:") then    
   		objNet.RemoveNetworkDrive ("X:") 
   		objNet.MapNetworkDrive "X:", "\\wvs001\smgdata" 
   end if	
else   	
	objNet.MapNetworkDrive "X:", "\\wvs001\smgdata" 
end if
 
if ucase(right(strusername,4)) <> "MAIN"  THEN
 if DriveExist("B:") then    
    if isNetworkDrive ("B:") then    
    		objNet.RemoveNetworkDrive ("B:") 
    		objNet.MapNetworkDrive "B:", "\\wvs001\user$\" & strUsername
    end if	
 else   	
 	objNet.MapNetworkDrive "B:", "\\wvs001\user$\" & strUsername 
 end if
end if

if ucase(right(strusername,4)) <> "MAIN"  THEN
 if DriveExist("H:") then    
    if isNetworkDrive ("H:") then    
    		objNet.RemoveNetworkDrive ("H:") 
    		objNet.MapNetworkDrive "H:", "\\wvs001\userhome$\" & strUsername
    end if	
 else   	
 	objNet.MapNetworkDrive "H:", "\\wvs001\userhome$\" & strUsername 
 end if
end if


if ucase(strusername)= "VMTAM" or ucase(strusername)= "IMTANG" or ucase(strusername)="KCLEONG" or ucase(strUsername)="EVELYNLO" or ucase(strUsername)="YOLANDAC" or ucase(strUsername)="SFIAO" or ucase(strUsername)="KIWU" or ucase(strUsername)="CWLAM" or ucase(strUsername)="KHHO" THEN
 if DriveExist("R:") then    
    if isNetworkDrive ("R:") then    
    		objNet.RemoveNetworkDrive ("R:") 
    		objNet.MapNetworkDrive "R:", "\\wvs001\direccao$"
    end if	
 else   	
 	objNet.MapNetworkDrive "R:", "\\wvs001\direccao$" 
 end if
end if

if ucase(strusername)= "KENCHAN" or ucase(strusername)= "WKLEONG" or ucase(strusername)="TOMASANT" or ucase(strUsername)="JFSOARES"  or ucase(strUsername)="CKMAK" THEN
 if DriveExist("L:") then
    if isNetworkDrive ("L:") then
    		objNet.RemoveNetworkDrive ("L:")
    		objNet.MapNetworkDrive "L:", "\\dcs001\swfdata\earthquake"
    end if	
 else   	
 	objNet.MapNetworkDrive "L:", "\\dcs001\swfdata\earthquake"
 end if
end if

if ucase(strusername)="IMTANG" or ucase(strUsername)="ITLEE"  or ucase(strUsername)="CHCHAN" THEN
 if DriveExist("N:") then
    if isNetworkDrive ("N:") then
    		objNet.RemoveNetworkDrive ("N:")
    		objNet.MapNetworkDrive "N:", "\\dcs001\swfdata"
    end if	
 else   	
 	objNet.MapNetworkDrive "N:", "\\dcs001\swfdata"
 end if
end if

if ucase(strusername)="CILAM" or ucase(strusername)="KENCHAN" or ucase(strUsername)="ANDREC" or ucase(strUsername)="CODYCHAN" THEN 
 if DriveExist("P:") then    
    if isNetworkDrive ("P:") then    
    		objNet.RemoveNetworkDrive ("P:") 
    		objNet.MapNetworkDrive "P:", "\\WVS001\download$"
    end if	
 else   	
 	objNet.MapNetworkDrive "P:", "\\WVS001\download$" 
 end If
End If

if ucase(strusername)="KENCHAN" or ucase(strUsername)="ANDREC" or ucase(strUsername)="CODYCHAN" THEN
 if DriveExist("I:") then    
    if isNetworkDrive ("I:") then    
    		objNet.RemoveNetworkDrive ("I:") 
    		objNet.MapNetworkDrive "I:", "\\WVS001\inf"
    end if	
 else   	
 	objNet.MapNetworkDrive "I:", "\\WVS001\inf"
 end if
end if 

'set shell=createobject("wscript.shell")
'shell.run "av.bat"
'set shell=nothing


'------------- CCAA NAS Share Folder Mapping --------------

if ucase(strusername)="TNTONG" or ucase(strusername)="MCCHOI" or ucase(strUsername)="WWLAO" or ucase(strUsername)="AUGUSTOR" or ucase(strusername)="CTKUOK" or ucase(strusername)="DIANALAI" or ucase(strusername)="SWCHANG" THEN
 if DriveExist("O:") then    
    if isNetworkDrive ("O:") then    
    		objNet.RemoveNetworkDrive ("O:") 
    		objNet.MapNetworkDrive "I:", "\\WVS001\inf"
    end if	
 else   	
 	objNet.MapNetworkDrive "I:", "\\WVS001\inf"
 end if
end if 

'----------------------------------------------------------

WScript.Quit


