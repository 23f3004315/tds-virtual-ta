---
chunk_id: course_archive_009
source_url: https://tds.s-anand.net/#/archive
source_title: archive
content_type: course
tokens: 437
---

/#quick-start) and [video](https://youtu.be/XVv6mJpFOb0)
- Learn about the [io module](https://pymotw.com/3/io/), [reference](https://docs.python.org/3/library/io.html) and [video](https://youtu.be/cIaOisyd7lE)

---

## Forecasting time series with Python

[**[Course Image: Forecasting time series with Python]** The image illustrates time series forecasting in Python, focusing on calculating and visualizing rolling means. Specifically, the code calculates rolling means for 5, 10, 15, and 20-day windows using `rolling_mean5`, `rolling_mean10`, etc., and assigns these values to new columns in the `data` DataFrame named 'moving_avg_5day', 'moving_avg_10day', 'moving_avg_15day', and 'moving_avg_20day' respectively. These moving averages are then plotted alongside the original time series data to smooth out fluctuations and identify trends. The use of `.dropna()` removes any rows with missing values that may have resulted from the rolling mean calculation, ensuring a clean dataset for further analysis or modeling. Finally, an autocorrelation plot of the 'new_cases' data is generated and displayed. and visualizing rolling means for time series forecasting in Python, specifically within a Jupyter Notebook environment. To smooth the data, it calculates rolling averages over 5, 10, 15, and 20 day windows, assigning these to new columns in a Pandas DataFrame called 'data'. The code then plots the rolling means alongside the original data to visualize trends and patterns, using lines to represent the rolling average for 15 and 20 day periods. The notebook uses `statsmodels` library for autocorrelation plots (ACF/PACF) to understand relationships within the data, and data cleaning is performed using `dropna` to handle missing values. Understanding rolling means helps to reduce noise and highlight underlying trends in time series data, which is essential for forecasting.)](https://youtu.be/aedA2javxvE)
