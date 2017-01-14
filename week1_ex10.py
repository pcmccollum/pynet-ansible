from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cryptomapf = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES-SHA")

for i in cryptomapf:
    print
    print i.text
    print

