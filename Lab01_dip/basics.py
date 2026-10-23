
# Exercise 1: Variables and Data Types
width = 640
height = 480
image_name = "sample.png"
is_color = True

print("Width:", width, type(width))
print("Height:", height, type(height))
print("Image Name:", image_name, type(image_name))
print("Is Color:", is_color, type(is_color))
print("Total Pixels:", width * height)


# Exercise 2: if, elif and else
intensities = [-1, 0, 127, 128, 255, 256]

for pixel in intensities:
    if pixel < 0 or pixel > 255:
        label = "Invalid"
    elif pixel >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"

    print(pixel, ":", label)


# Exercise 3: for and while loops
pixels = [20, 130, 255]

for pixel in pixels:
    if pixel >= 128:
        print(pixel, ": Bright pixel")
    else:
        print(pixel, ": Dark pixel")

counter = 0

while counter < 3:
    print(counter)
    counter += 1


# Exercise 4: Functions
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print(is_bright(127))
print(is_bright(128))
print(is_bright(200, 210))


# Exercise 5: Lists and Tuples
pixels = [0, 128, 255]

print("First item:", pixels[0])

pixels[1] = 150
pixels.append(64)

print("Updated list:", pixels)
print("Length:", len(pixels))

size = (640, 480)
width, height = size

print("Width:", width)
print("Height:", height)

# Lists are mutable, but tuples are immutable.


# Exercise 6: Dictionaries and Sets
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print("Width:", image["width"])
print("Mode:", image["mode"])

labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)

print("Unique labels:", unique_labels)
print("Number of unique labels:", len(unique_labels))
