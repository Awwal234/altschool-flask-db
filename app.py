from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "letyepwyendhkkiw"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(20), nullable=False, default="N/A")

    def __repr__(self):
        return f"BlogPost {self.title} by {self.author}"


@app.route("/")
def home():
    posts = BlogPost.query.all()

    context = {
        'posts': posts
    }
    return render_template("base.html", **context)

# creating book_db


@app.route("/posts", methods={'POST'})
def create_book():
    username = request.form.get('username')
    title = request.form.get('title')
    author = request.form.get('author')

    new_post = BlogPost(username=username, title=title, author=author)

    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
