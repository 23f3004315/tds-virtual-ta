---
chunk_id: course_unicode_001
source_url: https://tds.s-anand.net/#/unicode
source_title: unicode
content_type: course
tokens: 390
---

 as f:
 text = f.read()

# Handling encoding errors
import pandas as pd
df = pd.read_csv('data.csv', encoding='utf-8', errors='replace')

# Detecting file encoding
import chardet
with open('unknown.txt', 'rb') as f:
 result = chardet.detect(f.read())
print(result['encoding'])
```

---

[**[Course Image: Code Pages, Character Encoding, Unicode, UTF-8 and the BOM - Computer Stuff They Didn't Teach You #2 (17 min)]** This image introduces fundamental concepts in computer science related to text encoding, specifically code pages, character encoding, Unicode, UTF-8, and the Byte Order Mark (BOM). It's part of a broader discussion about "Computer Stuff They Didn't Teach You," implying it covers essential knowledge often omitted from formal education. The video aims to equip students with an understanding of how computers represent text, addressing common pitfalls and misconceptions related to character encoding. Comprehending these concepts is crucial for data science tasks involving text processing, ensuring data is correctly interpreted and manipulated, especially when dealing with diverse character sets. Mastery of these topics enables effective handling of text data in various TDS projects and assignments.of Unicode, UTF-8, and the BOM (Byte Order Mark) in the context of character encoding, building upon foundational knowledge of code pages and character sets. The material presented aims to bridge the gap in "computer stuff they didn't teach you," highlighting the importance of understanding these encoding standards for handling text correctly in various applications. Understanding Unicode, UTF-8, and BOM can help you avoid common errors related to character display and data interpretation, particularly when working with diverse language sets. Mastering these topics is crucial for TDS projects that involve text processing, data storage, or communication with external systems.)](https://youtu.be/jeIBNn5Y5fI)
