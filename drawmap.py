import csv
from PIL import Image, ImageDraw

pixels = []
positions = []

for j in range(0, 100):
    for k in range(0, 100):
        positions.append((k, j))

newimg = Image.new('RGBA', (100, 100), color=0)

csvFile = open("drawmap.csv", "r")
reader = csv.reader(csvFile)
grid = []
for i in range(100):
    internal = []
    for j in range(100):
        internal.append(0)
    grid.append(internal)

for line in reader:
    index = int(line[0])
    offset = int(line[1])
    grid[index][offset] += 1

maximum = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] >= maximum:
            maximum = grid[i][j]

for i in range(100):
    for j in range(100):
        grid[i][j] = grid[i][j] / float(maximum)
        grid[i][j] *= 10
        if grid[i][j] > 1:
            grid[i][j] = 1
        grid[i][j] = int(grid[i][j] * 255)
        pixels.append((grid[i][j], 0, 0, 255))

for i in range(10000):
    newimg.putpixel(positions[i], pixels[i])

newimg.save("generate.png", 'PNG')
