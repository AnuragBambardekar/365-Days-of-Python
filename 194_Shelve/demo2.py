import shelve

# inserting items in DB
data: dict={
    'a':1,'b':2,'c':3,'d':4
}

with shelve.open('194_Shelve/TestDB2') as db:
    db.update(data)
    print(dict(db))