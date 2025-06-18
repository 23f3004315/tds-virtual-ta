---
chunk_id: discourse_topic_169283_post_4_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169283/4
source_title: Graded assignment 6
content_type: discourse
tokens: 263
username: 23f2005138
post_number: 4
topic_id: 169283
---

 it is challenging to ascertain the exact problem the student is trying to solve." alt="image" data-base62-sha1="nPaaIWtriJMunrro5mxPkkzgs0I" width="281" height="219">image281×219 9.1 KB

---

Whereas for Q2 (Punjab and Yamaha) I used the following code:

`print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') &amp; (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
 pearson_corr = pb['price_retention'].corr(pb[col])
 print(f'\t{col:25} : {pearson_corr:.2f}')
`
and got the following answers:

`Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l) : 0.24
	Avg Daily Distance (km) : -0.06
	Engine Capacity (cc) : -0.08
`
The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).
