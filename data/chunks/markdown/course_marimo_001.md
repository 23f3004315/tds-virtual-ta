---
chunk_id: course_marimo_001
source_url: https://tds.s-anand.net/#/marimo
source_title: marimo
content_type: course
tokens: 369
---


 # Add interactive widgets
 slider = mo.ui.slider(1, 100)
 # Create dynamic Markdown
 mo.md(f"{slider} {"🟢" * slider.value}")
 ```

3. **Version Control**
 - Keep notebooks are Python files
 - Use Git to track changes
 - Publish on [marimo.app](https://marimo.app/) for collaboration

---

[**[Course Image: "marimo: an open-source reactive notebook for Python" - Akshay Agrawal (Nbpy2024)]** This image showcases the interactive data exploration capabilities within a marimo notebook. A user has selected a subset of images (likely handwritten digits) and the notebook dynamically displays both a preview of the selected images and associated data in a tabular format, including "index," "x," "y," and "digit" values. Histograms provide a visual summary of the distribution of these data columns. This demonstrates marimo's reactive nature, where data selection triggers automatic updates in both visual representations and data tables. By connecting UI elements (checkboxes next to each row) with data visualizations, marimo enables users to explore and understand datasets more intuitively.tion and visualization within a marimo notebook, specifically using an image dataset. The top portion displays a preview of images that have been selected, likely from a larger dataset of handwritten digits (the digit "2" is shown repeatedly). Below the preview, tabular data associated with the selected images is presented, including "index", "x", "y" coordinates, and the "digit" classification. Bar charts above each column provide a quick overview of the distribution of values for the selected data, allowing for interactive exploration and filtering of the dataset within the marimo environment.)](https://youtu.be/9R2cQygaoxQ)
