text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "map"
input = ''.join([chr(x) for x in range(97,123)])
output = ''.join([chr((x - 97 + 2)%26 + 97) for x in range(97,123)])

print(url.translate(''.maketrans(input, output)))

#ocr


#cleaner
import string 
translation_table = ''.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(text.translate(translation_table))


