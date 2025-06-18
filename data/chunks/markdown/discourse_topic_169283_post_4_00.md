---
chunk_id: discourse_topic_169283_post_4_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169283/4
source_title: Graded assignment 6
content_type: discourse
tokens: 223
username: 23f2005138
post_number: 4
topic_id: 169283
---

## Post #4 by 23f2005138

**Direct Link**: [Post #4](https://discourse.onlinedegree.iitm.ac.in/t/169283/4)

@Jivraj @Saransh_Saini

I have similar concern

For Q1, I used the following code:

`print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
 pearson_corr = kk['price_retention'].corr(kk[col])
 print(f'\t{col:25} : {pearson_corr:.2f}')
`
And got the following output:

`Pearson correlation for Karnataka between price retention and column
	Mileage (km/l) : 0.03
	Avg Daily Distance (km) : -0.06
	Engine Capacity (cc) : -0.04
`
Whereas options are below where none of them are correct.
