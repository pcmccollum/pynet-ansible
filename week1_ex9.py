from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cryptomapf = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for i in cryptomapf:
    print
    print i.text
    print

