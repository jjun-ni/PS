n = int(input())

def point(n):
    if n == 1:
        return['*']

    stars = point(n//3)
    L = []

    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+' '*(n//3)+star)
    for star in stars:
        L.append(star*3)

    return L

print('\n'.join(point(n)))