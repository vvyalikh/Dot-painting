import colorgram
#extract colors from colorgram for Hirst dot painting
colors = colorgram.extract("dots.jpg", 30)
print(colors)

random_rgb = []
for color in colors:
     r = color.rgb.r
     g = color.rgb.g
     b = color.rgb.b
     colors_rgb = (r, g, b)
     random_rgb.append(colors_rgb)

print(random_rgb)
