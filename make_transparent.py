from PIL import Image, ImageSequence
import os

def make_transparent(input_path, output_path):
    try:
        im = Image.open(input_path)
        
        # Get the background color from the top-left pixel of the first frame
        bg_color = im.convert("RGB").getpixel((0, 0))
        print(f"Detected background color: {bg_color}")
        
        frames = []
        for frame in ImageSequence.Iterator(im):
            frame = frame.convert("RGBA")
            datas = frame.getdata()
            
            new_data = []
            tolerance = 10 # Tolerance for black/dark colors
            
            for item in datas:
                # Calculate distance from background color
                dist = sum([abs(c1 - c2) for c1, c2 in zip(item[:3], bg_color)])
                
                # If pixel is close to background color, make it transparent
                if dist < 60: # Increased tolerance for compressed GIFs
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            
            frame.putdata(new_data)
            frames.append(frame)
            
        # Save as GIF with transparency
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            disposal=2,
            duration=im.info.get('duration', 100),
            loop=0,
            transparency=0
        )
        print(f"Saved transparent GIF to {output_path}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Execution
path = "e:/git-personalização/augusto49/src/cat.gif"
new_path = "e:/git-personalização/augusto49/src/cat-transparent.gif"

if os.path.exists(path):
    make_transparent(path, new_path)
else:
    print("File not found.")
