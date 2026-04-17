import sys
from PIL import Image

try:
    img = Image.open('assets/OTI_ACAD_HORIZON.jpg')
    img = img.convert('RGB')
    width, height = img.size
    cx = width // 2
    
    # We want a 100% accurate gradient.
    # To avoid 1308 stops, we can select stops intelligently or just output 50 evenly spaced stops + dense stops around the horizon
    
    stops = []
    
    y_vals = []
    # space top
    y_vals.extend(range(0, 700, 50))
    # near horizon
    y_vals.extend(range(700, 950, 5)) 
    # below horizon
    y_vals.extend(range(950, 1308, 50))
    # ensure 1307
    if 1307 not in y_vals: y_vals.append(1307)
    
    y_vals = sorted(list(set(y_vals)))
    
    for y in y_vals:
        r, g, b = img.getpixel((cx, y))
        pct = y / height * 100
        stops.append(f"rgb({r},{g},{b}) {pct:.2f}%")
        
    gradient = "linear-gradient(\n  to bottom,\n  " + ",\n  ".join(stops) + "\n);"
    
    with open('auto_gradient.txt', 'w') as f:
        f.write(gradient)
        
    print("Gradient written to auto_gradient.txt")
except Exception as e:
    print("Error:", e)

