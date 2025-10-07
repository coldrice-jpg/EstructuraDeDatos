# Lee los valores s y t
linea_st = input().split()
s = int(linea_st[0])
t = int(linea_st[1])

linea_ab = input().split()
a = int(linea_ab[0])
b = int(linea_ab[1])

linea_mn = input().split()
m = int(linea_mn[0])
n = int(linea_mn[1])

# Lee las distancias
apples = [int(dist) for dist in input().split()]
oranges = [int(dist) for dist in input().split()]

apples_on_house = sum(1 for apple in apples if s <= a + apple <= t)
oranges_on_house = sum(1 for orange in oranges if s <= b + orange <= t)

print(apples_on_house)
print(oranges_on_house)