---
chunk_id: course_image_compression_001
source_url: https://tds.s-anand.net/#/image-compression
source_title: image-compression
content_type: course
tokens: 451
---

p

# Optimize PNG
pngquant --quality=65-80 image.png

# Optimize JPEG
jpegoptim --strip-all --all-progressive --max=85 image.jpg

# Convert and resize
convert input.jpg -resize 800x600 output.jpg

# Batch convert
mogrify -format webp -quality 85 *.jpg
```

---

Watch this video on modern image formats and optimization (15 min):

[**[Course Image: Modern Image Optimization (15 min)]** This material introduces the concept of image compression through a video resource titled "Image compression deep-dive" from web.dev LIVE, which will guide you through modern image formats and optimization techniques. The primary goal is to teach students about efficiently reducing image file sizes without significant quality loss, which is crucial for web performance and storage efficiency. This deep dive explores how different compression algorithms work, providing practical insights applicable in TDS projects where optimized image delivery is essential. You'll gain an understanding of choosing the right image format and compression settings for various use cases, enabling you to improve website loading times and user experience. A key takeaway is to avoid common pitfalls like excessive compression that degrades image quality, while striving for the optimal balance between file size and visual fidelity.web.dev LIVE" video focusing on a deep-dive into the topic of image compression. It introduces the concept of optimizing images for web use. The video likely explores various techniques and tools used to reduce image file sizes without significantly sacrificing visual quality, which is crucial for improving website loading speeds and user experience. Students can expect to learn about modern image formats, compression algorithms, and practical optimization strategies applicable to their projects. The video likely addresses common misconceptions about image compression and provides guidance on choosing the most appropriate methods for different scenarios.)](https://youtu.be/F1kYBnY6mwg)

Tools for image optimization:

- [squoosh.app](https://squoosh.app/): Browser-based compression
- [ImageOptim](https://imageoptim.com/): GUI tool for Mac
- [sharp](https://sharp.pixelplumbing.com/): Node.js image processing
- [Pillow](https://python-pillow.org/): Python imaging library
