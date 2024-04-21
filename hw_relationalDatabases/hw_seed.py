import logging

import faker
import random
import psycopg2
from psycopg2 import DatabaseError

fake = faker.Faker()

# Connecting to the DB
conn = psycopg2.connect(
  host="localhost", 
  database= "postgres", 
  user= "postgres",
  password= "12341234"
)
cur = conn.cursor()

# Adding Users
for _ in range (10):
  cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fake.name(), fake.email(),))

# Adding Statuses
cur.executemany("INSERT INTO status (name) VALUES (%s)", ([('new',), ('in progress',), ('completed',)]))

# Adding Tasks that link Users and Statuses
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

for _ in range(20):
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s) RETURNING id",
        (fake.word(), fake.text(), random.choice(status_ids), random.choice(user_ids))
    )

try:
  conn.commit()
except DatabaseError as e:
  logging.error(e)
  conn.rollback()
finally:
  cur.close()
  conn.close()