import re

# UPDATE HTML
with open('index.html', 'r') as f:
    html_content = f.read()

html_content = html_content.replace('<img src="assets/OTI_ACAD_HORIZON.jpg" class="hero-bg-img" alt="">', '<div class="hero-bg-gradient"></div>')

with open('index.html', 'w') as f:
    f.write(html_content)

# UPDATE CSS
with open('auto_gradient.txt', 'r') as f:
    gradient_str = f.read().strip()

with open('style.css', 'r') as f:
    css_content = f.read()

css_block = f"""\.hero-bg-gradient {{
    position: absolute;
    width: 100vw;
    /* Ubah angka 140vh ini untuk mengatur ketebalan horizon (makin kecil=makin tipis) */
    height: 140vh; 
    top: 80vh; 
    left: 0;
    transform: translateY(-65.4%);
    background: {gradient_str};
}}"""

css_content = re.sub(r'\.hero-bg-img\s*\{[^}]+\}', css_block.replace("\\.", "."), css_content, flags=re.MULTILINE)

with open('style.css', 'w') as f:
    f.write(css_content)

print("Done updating index.html and style.css")
