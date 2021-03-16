import data
import math

def hex2rgb(h):
    return ( (h & 0xff0000) >> 16
           , (h & 0x00ff00) >> 8
           , (h & 0x0000ff)
           )

def colordistance(h1, h2):
    r1,g1,b1 = hex2rgb(h1)
    r2,g2,b2 = hex2rgb(h2)
    return math.sqrt(pow(r2-r1, 2) + pow(g2-g1, 2) + pow(b2-b1, 2))

def find_minimal_distance(h):
    mcd = None
    for c in data.colors256:
        id = c['colorId']
        hx = int(c['hexString'][1:], base=16)
        cd = colordistance(h, hx)
        if not mcd or (mcd and cd < mcd[2]):
            mcd = (id,hx,cd)
    return mcd

for color in data.colors:
    r,g,b = hex2rgb(color)
    id,hx,cd = find_minimal_distance(color)
    print(id, hex(hx), cd)
