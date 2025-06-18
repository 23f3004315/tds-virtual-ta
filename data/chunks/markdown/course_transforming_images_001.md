---
chunk_id: course_transforming_images_001
source_url: https://tds.s-anand.net/#/transforming-images
source_title: transforming-images
content_type: course
tokens: 571
---

800))

# Apply enhancements
 img = (ImageEnhance.Contrast(img)
 .enhance(1.2))

return img.filter(ImageFilter.SHARPEN)

if __name__ == "__main__":
 import asyncio
 img = asyncio.run(process_image("input.jpg"))
 img.save("output.jpg", quality=85)
```

Key features and techniques you'll learn:

---

- **Image Loading and Saving**: Handle various formats with automatic conversion
- **Basic Operations**: Resize, rotate, crop, and flip images
- **Color Manipulation**: Adjust brightness, contrast, and color balance
- **Filters and Effects**: Apply blur, sharpen, and other visual effects
- **Drawing**: Add text, shapes, and overlays to images
- **Batch Processing**: Handle multiple images efficiently
- **Memory Management**: Process large images without memory issues

### Basic Image Operations

Common operations for resizing, cropping, and rotating images:

```python
from PIL import Image

async def transform_image(
 path: str,
 size: tuple[int, int],
 rotation: float = 0
) -> Image.Image:
 """Transform image with basic operations."""
 with Image.open(path) as img:
 # Resize with anti-aliasing
 img = img.resize(size, Image.LANCZOS)

# Rotate around center
 if rotation:
 img = img.rotate(rotation, expand=True)

# Auto-crop empty edges
 img = img.crop(img.getbbox())

return img
```

### Color and Enhancement

Adjust image appearance with built-in enhancement tools:

```python
from PIL import ImageEnhance, ImageOps

async def enhance_image(
 img: Image.Image,
 brightness: float = 1.0,
 contrast: float = 1.0,
 saturation: float = 1.0
) -> Image.Image:
 """Apply color enhancements to image."""
 enhancers = [
 (ImageEnhance.Brightness, brightness),
 (ImageEnhance.Contrast, contrast),
 (ImageEnhance.Color, saturation)
 ]

for Enhancer, factor in enhancers:
 if factor != 1.0:
 img = Enhancer(img).enhance(factor)

return img
```

### Filters and Effects

Apply visual effects and filters to images:

```python
from PIL import ImageFilter

def apply_effects(img: Image.Image) -> Image.Image:
 """Apply various filters and effects."""
 effects = {
 'blur': ImageFilter.GaussianBlur(radius=2),
 'sharpen': ImageFilter.SHARPEN,
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
