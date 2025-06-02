from flask import Flask, render_template,request
import pickle
from recommend_logic import recommend_movies

app = Flask(__name__)

# Loading the Apriori Model
with open('movie_rules.pkl','rb') as f:
    rules = pickle.load(f)

# Making the recommendation web
@app.route("/")
def home():
    return render_template('index.html')

# giving the recommendation
@app.route('/recommend',methods=['POST'])
def recommed():
    user_input = request.form['movie'].lower()

    if not user_input:
        return render_template('index.html',recommendations=['Please enter movie name'])

    recommend_moive = recommend_movies(user_input,rules,top_n=3)
    return render_template('index.html',recommendations=recommend_moive)


# Getting the url and debugging
if __name__ == '__main__':
    app.run(debug=True)

