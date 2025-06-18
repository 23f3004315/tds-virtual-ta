---
chunk_id: course_transforming_images_003
source_url: https://tds.s-anand.net/#/transforming-images
source_title: transforming-images
content_type: course
tokens: 569
---

https://pillow.readthedocs.io/): Complete API reference
- [Python Image Processing Tutorial](https://realpython.com/image-processing-with-the-python-pillow-library/): In-depth guide
- [Sample Images Dataset](https://www.kaggle.com/datasets/lamsimon/celebs): Test images for practice

Watch these tutorials for hands-on demonstrations:

---

[**[Course Image: Image Processing Tutorial for beginners with Python PIL in 30 mins]** This image introduces the concept of "PYTHON IMAGE PROCESSING" within the "transforming-images" module of the TDS course. It signals the start of learning how to manipulate and modify images using Python. The image is a title card designed to prepare you for a deep dive into practical image processing techniques using Python, likely using libraries like PIL (Pillow). Mastering image processing with Python will allow students to transform images for various applications within their TDS projects. The surrounding content suggests hands-on tutorials will accompany this introduction.introducing the topic of image processing with Python. It signals a tutorial or lesson focused on manipulating and analyzing images using the Python programming language, likely leveraging libraries such as PIL (Pillow). The main goal is to equip beginners with the foundational knowledge and skills to perform basic image processing tasks. In the broader context of "transforming-images," this introduction likely covers essential techniques like resizing, color adjustments, filtering, and other manipulations achievable through Python code. Students should understand that Python, along with libraries like PIL, provides powerful tools for image transformation.)](https://youtu.be/dkp4wUhCwR4)

### Image Processing with ImageMagick

[ImageMagick](https://imagemagick.org/) is a powerful command-line tool for image manipulation, offering features beyond what's possible with Python libraries. It's particularly useful for:

- Batch processing large image collections
- Complex image transformations
- High-quality format conversion
- Creating image thumbnails
- Adding text and watermarks

Basic Operations:

```bash
# Format conversion
convert input.png output.jpg

# Resize image (maintains aspect ratio)
convert input.jpg -resize 800x600 output.jpg

# Compress image quality
convert input.jpg -quality 85 output.jpg

# Rotate image
convert input.jpg -rotate 90 output.jpg
```

Common Data Science Tasks:

```bash
# Create thumbnails for dataset preview
convert input.jpg -thumbnail 200x200^ -gravity center -extent 200x200 thumb.jpg

# Normalize image for ML training
convert input.jpg -normalize -strip output.jpg

# Extract dominant colors
convert input.jpg -colors 5 -unique-colors txt:

# Generate image statistics
identify -verbose input.jpg | grep -E "Mean|Standard|Kurtosis"
```

Batch Processing:
