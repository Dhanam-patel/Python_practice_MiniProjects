import os
a = os.listdir("python/Clear The Clutter/images")
# The below code will rename all the images to ordered name
temp = 1
for i in a:
    if i.endswith(".jpg"):
        os.rename(f"python/Clear The Clutter/images/{i}", f"python/Clear The Clutter/images/{temp}.jpg")
        temp = temp + 1
    
    if i.endswith(".png"):
        os.rename(f"python/Clear The Clutter/images/{i}", f"python/Clear The Clutter/images/{temp}.png")
        temp = temp + 1

    if i.endswith(".webp"):
        os.rename(f"python/Clear The Clutter/images/{i}", f"python/Clear The Clutter/images/{temp}.webp")
        temp = temp + 1