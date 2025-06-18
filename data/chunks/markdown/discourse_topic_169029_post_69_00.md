---
chunk_id: discourse_topic_169029_post_69_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/69
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 192
username: 22f3001307
post_number: 69
topic_id: 169029
---

## Post #69 by 22f3001307

**Direct Link**: [Post #69](https://discourse.onlinedegree.iitm.ac.in/t/169029/69)

Hi,

In GA 2, q5, this is the code i got in the question.

`import numpy as np
from PIL import Image
from google.colab import files
import colorsys

# There is a mistake in the line below. Fix it
image = Image.open(list(files.upload().keys)[0])

rgb = np.array(image) / 255.0
lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
light_pixels = np.sum(lightness &gt; 0.554)
print(f'Number of pixels with lightness &gt; 0.554: {light_pixels}')
`
Is this the code for others as well?

Thanks
