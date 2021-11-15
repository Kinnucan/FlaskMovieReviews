from flask import Flask, render_template, request
from werkzeug.utils import redirect
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

# Homepage
@app.route('/')
def show_all_reviews():
    reviews = db.get()
    return render_template("home.html", reviews = reviews)

# Display the create review page
@app.route("/createreview")
def create_review():
    return render_template("review.html", review = None)

# Display the edit review page
@app.route("/editreview/<review_id>", methods=['GET', 'POST'])
def edit_review(review_id):
    review = db.get(review_id)
    return render_template("review.html", review = review)

# Create either a brand new review, or submit changes to a previous review
@app.route("/submitreview", methods=['GET', 'POST'])
def submit_review():
    if (request.form.get("review_id")):
        review_id = request.form.get("review_id")
        title = request.form.get("title")
        review_text = request.form.get("review_text")
        rating = request.form.get("rating")
        db.update(review_id, title, review_text, rating)
    else:
        title = request.form.get("title")
        review_text = request.form.get("review_text")
        rating = request.form.get("rating")
        db.create(title, review_text, rating)
    return redirect("/createreview")

# Deletes a given review and redirects to homepage
@app.route("/deletereview/<review_id>")
def delete_review(review_id):
    db.delete(review_id)
    return redirect("/")

# Displays a given review
@app.route("/displayreview/<review_id>")
def display_review(review_id):
    review = db.get(review_id)
    return render_template("display_review.html", review = review)

if __name__ == '__main__':
    app.run(debug=True)
