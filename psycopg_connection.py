import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect("dbname=maria_flix user=postgres password=esquecer host=localhost")

conn.autocommit = True

cursor = conn.cursor(cursor_factory=RealDictCursor)

