from PIL import Image, ImageSequence

def remove_watermark(input_path, output_path, crop_pixels=30):
    with Image.open(input_path) as im:
        width, height = im.size
        print(f"Processing {input_path} ({width}x{height})...")
        
        frames = []
        # Iterate over frames
        for frame in ImageSequence.Iterator(im):
            # Convert to RGBA to ensure alpha channel
            frame = frame.convert("RGBA")
            
            # Crop the bottom 'crop_pixels' amount
            # box = (left, upper, right, lower)
            box = (0, 0, width, height - crop_pixels)
            cropped_frame = frame.crop(box)
            
            frames.append(cropped_frame)
            
        # Save as new GIF
        print(f"Saving {len(frames)} frames to {output_path}...")
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=im.info.get('loop', 0),
            duration=im.info.get('duration', 100),
            optimize=False,
            disposal=2, # Background clearing
            transparency=0
        )
        print("Done!")

if __name__ == "__main__":
    remove_watermark("src/cat-transparent.gif", "src/cat-clean.gif", 60)
