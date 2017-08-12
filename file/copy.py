try:
    f = open('3.gif','r')
    f1 = open('/home/linux/7/python/3.gif','w')
except:
    print "open failed"

while True:
    s = f.readline()
    if not s:
        break
    f1.write(s)
