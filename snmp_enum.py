# snmp_enum.py
from pysnmp.hlapi import *

def snmp_walk(target, community, oid):
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(community),
                              UdpTransportTarget((target, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):
        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    community_str = input("Enter SNMP community string: ")
    oid = input("Enter OID to walk (e.g., 1.3.6.1.2.1.1): ")
    snmp_walk(target_ip, community_str, oid)
