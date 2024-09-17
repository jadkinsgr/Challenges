import os

num = 10
while num < 100:
    pdir = '/Users/joshua.adkins/Github/100-days-code-challenge/'
    num += 1
    com = pdir+'Day'+str(num)
    os.mkdir(com)
    #print(com)
