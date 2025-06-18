---
chunk_id: course_transforming_images_000
source_url: https://tds.s-anand.net/#/transforming-images
source_title: transforming-images
content_type: course
tokens: 502
---

## Transforming Images

### Image Processing with PIL (Pillow)

[**[Course Image: Python Tutorial: Image Manipulation with Pillow (16 min)]** This content introduces image processing techniques using the PIL (Pillow) library in Python, a fundamental tool for transforming images. Students will learn how to manipulate images programmatically, which is essential for various TDS projects involving image analysis or modification. The learning outcome is to gain proficiency in using Pillow for tasks like resizing, cropping, and applying filters to images. Mastery of these techniques will enable students to programmatically alter images according to project requirements. Prior knowledge of basic Python syntax is recommended before diving into image manipulation with Pillow.ython and the Pillow library for image manipulation, a fundamental aspect of "transforming-images". Pillow is a powerful Python library that allows for a wide range of image processing tasks, including resizing, cropping, color adjustments, and applying filters. The image highlights the importance of understanding how to use Pillow to modify images programmatically, enabling students to automate image transformations for various applications. Mastering Pillow's functionalities is crucial for TDS projects involving image analysis, computer vision, and content creation where automated image processing is required. This prepares students to apply these skills in real-world projects involving image data.)](https://youtu.be/6Qs3wObeWwc)

[Pillow](https://python-pillow.org/) is Python's leading library for image processing, offering powerful tools for editing, analyzing, and generating images. It handles various formats (PNG, JPEG, GIF, etc.) and provides operations from basic resizing to complex filters.

Here's a minimal example showing common operations:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow"]
# ///

from PIL import Image, ImageEnhance, ImageFilter

async def process_image(path: str) -> Image.Image:
 """Process an image with basic enhancements."""
 with Image.open(path) as img:
 # Convert to RGB to ensure compatibility
 img = img.convert('RGB')

# Resize maintaining aspect ratio
 img.thumbnail((800, 800))

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
