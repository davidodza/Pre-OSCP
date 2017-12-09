#!/bin/bash
#Detects your IP and netdiscover your whole range.

ip route get 8.8.8.8|grep src>ip.txt
ipLengthTest=$(cat ip.txt)
ipLengthTest=${ipLengthTest: -4}

# Fourth octet has 3 digits
if [[ $ipLengthTest =~ ^[0-9]{3} ]];
then
        myIP=$(tail -c 17 ip.txt)
        myIP=${myIP::-4}
        myIP+="0/24"  
else		
# Fourth octet has 2 digits
if [[ $ipLengthTest =~ ^[.][0-9]{2} ]]; 
then
        myIP=$(tail -c 16 ip.txt)
        myIP=${myIP::-3}
        myIP+="0/24"    
else
# Fourth octet has 1 digit
if [[ $ipLengthTest =~ ^[0-9][.][0-9] ]];
then
        myIP=$(tail -c 15 ip.txt)
        myIP=${myIP::-2}
        myIP+="0/24"  
fi
fi
fi
netdiscover -r $myIP

