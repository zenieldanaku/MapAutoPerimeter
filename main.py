from pygame import image, mask, draw, Surface

cross = image.load('data/cross.png')  # a simple 3x3 cross
ene = image.load('data/ene.png')  # an "L" shape
ele = image.load('data/ele.png')  # an "n" shape

# select the image here.
chosen = cross

mask_elem = mask.from_surface(chosen)
chosen.fill((255, 0, 0))

coords = []
# this is the first part of the alogorithm.
# it looks at the image-mask and gets all the valid vertices.
# since the pixels are squares, each one has 4 vertices.
# repeated vertices are ignored.
for y in range(3):
    for x in range(3):  # I used "3" here because the images are 3x3px; for simplicity
        if mask_elem.get_at((x, y)):
            for dx, dy in [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]:
                if (dx, dy) not in coords:
                    coords.append((dx, dy))

vertex = coords[0]
vertices = []
# this part analizes the vertices and puts them in order, to trace the perimeter of the figure.
# It tries to go right from the start, then down, then left, then up to return to the original
# start point.
while len(coords):
    x, y = vertex

    # movement directions.
    right = x + 1, y
    left = x - 1, y
    up = x, y - 1
    down = x, y + 1

    if right in coords and right not in vertices:
        vertices.append(coords.pop(coords.index(right)))
        vertex = right

    elif down in coords and down not in vertices:
        vertices.append(coords.pop(coords.index(down)))
        vertex = down
    # Spanish
    # el problema parece estar acá. Con este orden, "cross" funciona pero "ene" es rotado 90º.
    # si pongo primero arriba y después izquierda, "ene" se renderiza bien, pero cross queda
    # en un loop infinito.

    # English
    # The problem seems to be here. With this order, "cross" works well, but "ene" is rotated 90º.
    # if I invert the order (up then left), "ene" renderizes correctly, but "cross" loops indefinitely.
    elif left in coords and left not in vertices:
        vertices.append(coords.pop(coords.index(left)))
        vertex = left

    elif up in coords and up not in vertices:
        vertices.append(coords.pop(coords.index(up)))
        vertex = up


# Here the result is rendered in a 32x32px image to make it more visible.
img = Surface((32, 32))
img.fill((255, 0, 0))

# the lines drawn are not antialialized. We want to see the pixeles.
draw.lines(img, (255, 255, 255), 1, [(x * 10, y * 10) for x, y in vertices])

# Here the image is saved. It always gets the same name to avoid wasting space.
image.save(img, 'result.png')
