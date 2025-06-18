---
chunk_id: course_visualizing_network_data_with_kumu_000
source_url: https://tds.s-anand.net/#/visualizing-network-data-with-kumu
source_title: visualizing-network-data-with-kumu
content_type: course
tokens: 453
---

## Visualizing Network Data with Kumu

[**[Course Image: Visualizing network data with Kumu]** This instructional material explains how to represent a sparse matrix, which is a matrix where most elements are zero, using the Compressed Sparse Row (CSR) format for efficient memory usage, especially relevant when visualizing network data with Kumu where networks are often sparse. The CSR format uses three arrays: `V` to store non-zero values, `COL_INDEX` to store the column indices of these values, and `ROW_INDEX` to store the indices in `V` where each row starts. To extract a row from the sparse matrix, `row_start` and `row_end` are determined from the `ROW_INDEX` array, defining the slice of `V` and `COL_INDEX` arrays to be considered. This representation is crucial in network visualization as it allows efficient storage and processing of large, sparse network datasets in tools like Kumu, improving performance and reducing memory footprint, a key element in TDS projects involving network analysis. The example matrix provided shows how to translate a matrix into these CSR arrays, demonstrating the savings in memory compared to storing the entire matrix.izing network data in Kumu by using sparse matrices. It provides an example of a 4x4 sparse matrix and demonstrates how to represent it using three arrays: V (values), COL_INDEX (column indices), and ROW_INDEX (row indices). The explanation details how to extract a row from the sparse matrix representation using row indices to find the relevant slices in the V and COL_INDEX arrays. This helps in understanding how sparse matrices are structured and how their elements can be accessed for network data visualization. The concept of CSR (Compressed Sparse Row) format is introduced as a memory-saving technique when dealing with sparse matrices in network analysis.)](https://youtu.be/OndB17bigkc)

- [Kumu](https://kumu.io)
- [IMDB data](https://developer.imdb.com/non-commercial-datasets/)
- [Jupyter Notebook](https://colab.research.google.com/drive/1CHR68fw7lZC9H2JtVW4LXpUvNwfM_VE-?usp=sharing)
