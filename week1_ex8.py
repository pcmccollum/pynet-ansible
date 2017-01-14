from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cryptomapf = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in cryptomapf:
    print
    print i.text
    for child in i.children:
        print child.text
    print

