from PIL import Image

img = Image.open("input.jpg")
pixels = img.load()

key = 50

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixels[i, j]

        pixels[i, j] = (
            (r + key) % 256,
            (g + key) % 256,
            (b + key) % 256
        )

img.save("encrypted.jpg")
print("Image encrypted successfully")