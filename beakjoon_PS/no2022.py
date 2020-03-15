import math

x, y, c = map(float, input().split())
d = 1.0
high = min(x, y)
low = 0.0

while(low+0.001) <= high:
    d = (high + low) / 2.0
    e = math.sqrt((x**2)-(d**2))
    f = math.sqrt((y**2)-(d**2))
    if c == round((f*e)/(f+e), 4):
        break
    elif c > (f*e)/(f+e):
        high = d
    elif c < (f*e)/(f+e):
        low = d

print('%.03f' % d)
