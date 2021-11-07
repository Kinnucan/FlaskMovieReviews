from flask import Flask
from database import Database

app = Flask(__name__)
app.config.from_pyfile('server.cfg')

"""
Use the following commands to interact with the database:
  db.get() to get all of the reviews
  db.get(id) to get a single review
  db.create(title, text, rating) to add a new review
  db.update(id, title, text, rating) to update a review
  db.delete(id) to delete a review
"""
db = Database(app)

@app.route('/')
def show_all_reviews():
    return 'Welcome to Movie Reviews!' 

if __name__ == '__main__':
    app.run(debug=True)
