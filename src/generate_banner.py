import random

def generate_banner():
    width = 800
    height = 300
    
    # Cores baseadas no tema Tokyo Night / Dark
    bg_color = "#0d1117" # GitHub Dark Dimmed Background
    text_color = "#38bdae" # Cyan/Teal do tema
    particle_colors = ["#38bdae", "#7aa2f7", "#bb9af7", "#ffffff"]
    
    svg_header = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            @keyframes float {{
                0% {{ transform: translateY(0px) translateX(0px); opacity: 0; }}
                50% {{ opacity: 0.8; }}
                100% {{ transform: translateY(-100px) translateX(50px); opacity: 0; }}
            }}
            .particle {{
                opacity: 0;
                animation: float 10s infinite linear;
            }}
            .text-title {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 40px;
                font-weight: bold;
                fill: {text_color};
                text-anchor: middle;
                dominant-baseline: middle;
                filter: url(#glow);
            }}
            .text-subtitle {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 20px;
                fill: #a9b1d6;
                text-anchor: middle;
                dominant-baseline: middle;
            }}
        </style>
        <filter id="noise">
            <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
            <feColorMatrix type="saturate" values="0"/>
        </filter>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <!-- Background -->
    <rect width="100%" height="100%" fill="{bg_color}"/>
    
    <!-- Particles -->
    '''
    
    particles_svg = ""
    for _ in range(50):
        cx = random.randint(0, width)
        cy = random.randint(height // 2, height + 100) # Start from bottom half
        r = random.randint(1, 4)
        color = random.choice(particle_colors)
        duration = random.randint(5, 15)
        delay = random.uniform(0, 10)
        
        particles_svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" class="particle" style="animation-duration: {duration}s; animation-delay: {delay}s;"/>\n'
        
    # Grain Overlay
    grain_svg = f'''
    <rect width="100%" height="100%" filter="url(#noise)" opacity="0.07"/>
    '''
    
    # Text
    text_svg = f'''
    <text x="{width/2}" y="{height/2 - 20}" class="text-title">Augusto Ferreira</text>
    <text x="{width/2}" y="{height/2 + 30}" class="text-subtitle">Full Stack Developer • Flutter • Web</text>
    '''
    
    svg_footer = "</svg>"
    
    content = svg_header + particles_svg + grain_svg + text_svg + svg_footer
    
    with open("src/banner.svg", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_banner()
