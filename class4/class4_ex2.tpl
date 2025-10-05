Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\d+)
Value DUPLEX (\w+)
Value SPEED (\w+)
Value PORT_TYPE (\S+)



Start
  ^Port.*Type\s*$$ -> ShowIntStatus

ShowIntStatus
  ^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE}\s*$$ -> Record

EOF



#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX


#FSM Table:
#['PORT_NAME', 'STATUS', 'VLAN', 'DUPLEX', 'SPEED', 'PORT_TYPE']
#['Gi0/1/0','notconnect','1','auto','auto','10/100/1000BaseTX']
#['Gi0/1/1','notconnect','1','auto','auto','10/100/1000BaseTX']
#['Gi0/1/2','notconnect','1','auto','auto','10/100/1000BaseTX']
#['Gi0/1/3','notconnect','1','auto','auto','10/100/1000BaseTX']

