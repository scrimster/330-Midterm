from flask import Flask, render_template

app = Flask(__name__)

# Dictionary for recommendations
recommendations_dict = {
    "action": ["Terminator 2", "The Matrix", "Jujutsu Kaisen 0"],
    "thriller": ["No Country for Old Men", "Inception", "The Dark Knight"],
    "horror": ["The Blair Witch Project", "The Shining", "Alien"],
    "sci-fi": ["Dune", "The Martian", "2001: A Space Odyssey"]
}

@app.route('/')
def index():
    genres = recommendations_dict.keys()  # Pass genres to the template
    return render_template("home.html", genres=genres)

@app.route('/movies/<genre>')
def home(genre):
    movies = recommendations_dict.get(genre, ["No movies found for this genre."])
    return render_template("index.html", genre=genre, movies=movies)

@app.route('/movie/<movie>')
def movie_page(movie):
    return render_template("movie.html", movie=movie)

## Im dumb and pushed to main and need to modify the files under a feature branch so I'm adding this here
