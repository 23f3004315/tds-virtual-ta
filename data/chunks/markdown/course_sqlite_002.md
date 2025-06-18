---
chunk_id: course_sqlite_002
source_url: https://tds.s-anand.net/#/sqlite
source_title: sqlite
content_type: course
tokens: 421
---

.user_id
WHERE o.status = 'pending';
```

Python Integration:

```python
import sqlite3
from pathlib import Path
import pandas as pd

async def query_database(db_path: Path, query: str) -> pd.DataFrame:
 """Execute SQL query and return results as DataFrame.

Args:
 db_path: Path to SQLite database
 query: SQL query to execute

---

Returns:
 DataFrame with query results
 """
 try:
 conn = sqlite3.connect(db_path)
 return pd.read_sql_query(query, conn)
 finally:
 conn.close()

# Example usage
db = Path('data.db')
df = await query_database(db, '''
 SELECT date, COUNT(*) as count
 FROM events
 GROUP BY date
''')
```

Common Operations:

1. **Database Management**

```sql
 -- Backup database
 .backup 'backup.db'

-- Import CSV
 .mode csv
 .import data.csv table_name

-- Export results
 .headers on
 .mode csv
 .output results.csv
 SELECT * FROM table;
 ```

2. **Performance Optimization**

```sql
 -- Create index
 CREATE INDEX idx_user_email ON users(email);

-- Analyze query
 EXPLAIN QUERY PLAN
 SELECT * FROM users WHERE email LIKE '%@example.com';

-- Show indexes
 SELECT * FROM sqlite_master WHERE type='index';
 ```

3. **Data Analysis**

```sql
 -- Time series aggregation
 SELECT
 date(timestamp),
 COUNT(*) as events,
 AVG(duration) as avg_duration
 FROM events
 GROUP BY date(timestamp);

-- Window functions
 SELECT *,
 AVG(amount) OVER (
 PARTITION BY user_id
 ORDER BY date
 ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
 ) as moving_avg
 FROM transactions;
 ```

Tools to work with SQLite:

- [SQLiteStudio](https://sqlitestudio.pl/): Lightweight GUI
- [DBeaver](https://dbeaver.io/): Full-featured GUI
- [sqlite-utils](https://sqlite-utils.datasette.io/): CLI tool
- [Datasette](https://datasette.io/): Web interface
