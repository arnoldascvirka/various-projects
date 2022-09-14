import json
import requests
import sqlite3

db = sqlite3.connect(":memory:")
cursor = db.cursor()

while True:
    q = 1
