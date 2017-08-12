f = open('hold','w')

f.write('b')
f.seek(1024*1024)
f.write('e')
