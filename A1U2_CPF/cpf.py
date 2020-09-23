p1 = int(input())
p2 = int(input())
p3 = int(input())
x1 = p3 // 100 
x2 = (p3 // 10) - (x1 * 10) 
x3 = p3 - ((x1 * 100) + (x2 * 10))
p4 = x1 + x2 + x3
print('%03d.%03d.%03d-%02d' % (p1, p2, p3, p4))

