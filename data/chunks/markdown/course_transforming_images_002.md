---
chunk_id: course_transforming_images_002
source_url: https://tds.s-anand.net/#/transforming-images
source_title: transforming-images
content_type: course
tokens: 501
---

': ImageFilter.SHARPEN,
 'edge': ImageFilter.FIND_EDGES,
 'emboss': ImageFilter.EMBOSS
 }

return {name: img.filter(effect)
 for name, effect in effects.items()}
```

### Drawing and Text

Add text, shapes, and overlays to images:

```python
from PIL import Image, ImageDraw, ImageFont

---

async def add_watermark(
 img: Image.Image,
 text: str,
 font_size: int = 30
) -> Image.Image:
 """Add text watermark to image."""
 draw = ImageDraw.Draw(img)
 font = ImageFont.truetype("arial.ttf", font_size)

# Calculate text size and position
 text_bbox = draw.textbbox((0, 0), text, font=font)
 text_width = text_bbox[2] - text_bbox[0]
 text_height = text_bbox[3] - text_bbox[1]

# Position text at bottom-right
 x = img.width - text_width - 10
 y = img.height - text_height - 10

# Add text with shadow
 draw.text((x+2, y+2), text, font=font, fill='black')
 draw.text((x, y), text, font=font, fill='white')

return img
```

### Memory-Efficient Processing

Handle large images without loading them entirely into memory:

```python
from PIL import Image
import os

async def process_large_images(
 input_dir: str,
 output_dir: str,
 max_size: tuple[int, int]
) -> None:
 """Process multiple large images efficiently."""
 os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
 if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
 continue

input_path = os.path.join(input_dir, filename)
 output_path = os.path.join(output_dir, filename)

with Image.open(input_path) as img:
 # Process in chunks using thumbnail
 img.thumbnail(max_size)
 img.save(output_path, optimize=True)
```

Practice with these resources:

- [Pillow Documentation](https://pillow.readthedocs.io/): Complete API reference
- [Python Image Processing Tutorial](https://realpython.com/image-processing-with-the-python-pillow-library/): In-depth guide
- [Sample Images Dataset](https://www.kaggle.com/datasets/lamsimon/celebs): Test images for practice

Watch these tutorials for hands-on demonstrations:
