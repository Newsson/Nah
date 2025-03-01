import csv 
import string
s=["fff","hhh","rrr","uuu"]
with open ("mac.csv","w",newline="")as csvfile:
    k=csv.writer(csvfile,delimiter=",")
    k.writerow(["ii","yr","hrfg","jjfd"])
    k.writerow(["eeet","iuiui","hrytrfg","yrert"])
    k.writerow(s)
