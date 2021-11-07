print('Resetting database...')
from server import db
# Reset the database
db.db.drop_all()
# Create the tables
db.db.create_all()
# Create a test entry which works somewhat
if (len(db.get()) == 0):
    db.create("Mr. Pumpkin Man", "This is a pretty bad movie", 4)
print('Database reset: success!')

