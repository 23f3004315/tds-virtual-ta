---
chunk_id: course_transforming_images_004
source_url: https://tds.s-anand.net/#/transforming-images
source_title: transforming-images
content_type: course
tokens: 537
---

 -gravity center -extent 200x200 thumb.jpg

# Normalize image for ML training
convert input.jpg -normalize -strip output.jpg

# Extract dominant colors
convert input.jpg -colors 5 -unique-colors txt:

# Generate image statistics
identify -verbose input.jpg | grep -E "Mean|Standard|Kurtosis"
```

Batch Processing:

---

```bash
# Convert all images in a directory
mogrify -format jpg *.png

# Resize multiple images
mogrify -resize 800x600 -path output/ *.jpg

# Add watermark to images
for f in *.jpg; do
 convert "$f" -gravity southeast -draw "text 10,10 'Copyright'" "watermarked/$f"
done
```

Advanced Features:

```bash
# Apply image effects
convert input.jpg -blur 0x3 blurred.jpg
convert input.jpg -sharpen 0x3 sharp.jpg
convert input.jpg -edge 1 edges.jpg

# Create image montage
montage *.jpg -geometry 200x200+2+2 montage.jpg

# Extract image channels
convert input.jpg -separate channels_%d.jpg

# Composite images
composite overlay.png -gravity center base.jpg output.jpg
```

Watch this ImageMagick tutorial (16 min):

[**[Course Image: ImageMagick Introduction (16 min)]** This image introduces ImageMagick, a powerful command-line tool for image manipulation within the "transforming-images" curriculum. It serves as a starting point for understanding ImageMagick's capabilities. To get started with ImageMagick and learn about its basic functions, the image links to a 16-minute introductory video. The surrounding context includes example commands like "te overlay.png -gravity center base.jpg output.jpg", which demonstrates overlaying images using ImageMagick. This video helps students grasp the fundamental concepts of using ImageMagick to transform images and provides a foundation for more advanced image processing techniques. a powerful command-line tool for manipulating images. It serves as a visual entry point to a 16-minute tutorial video designed to familiarize you with ImageMagick's capabilities within the "transforming-images" curriculum. The video likely covers fundamental concepts and operations, preparing you to use ImageMagick for more complex image transformations later in the course. By watching the video, you'll gain a basic understanding of how to use ImageMagick to process and modify images, which is a prerequisite for subsequent lessons. ImageMagick is commonly used in projects and assignments involving automated image processing.)](https://youtu.be/wjcBOoReYc0)

Tools:
