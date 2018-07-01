def ceasar(c):
    if c.isalpha():
        return chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
    else:
        return c
        
a1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
b1 = str(list(map(ceasar, a1)))
