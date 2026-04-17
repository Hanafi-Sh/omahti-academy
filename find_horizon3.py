import sys
try:
    from PIL import Image
    img = Image.open('assets/Horizon_Horizontal.png')
    img = img.convert('L')
    width, height = img.size
    
    max_brightness = -1
    horizon_y = -1
    for y in range(height):
        row_sum = 0
        for x in range(width):
             row_sum += img.getpixel((x, y))
        avg = row_sum / width
        if avg > max_brightness:
            max_brightness = avg
            horizon_y = y
            
    print(f"Image Size: {width}x{height} (Aspect Ratio: {width/height:.2f})")
    print(f"Horizon is at Y: {horizon_y} ({horizon_y/height * 100:.2f}%)")
except Exception as e:
    print("Error:", e)
