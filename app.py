#--------------Import files-------------#
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

#--------------Config-------------#
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


#--------------Home Page-------------#
@app.route("/")
@app.route("/home")
def home():
    recipes = list(mongo.db.recipes.find())
    return render_template("home.html", recipes=recipes) 


#--------------Search Recipe-------------#
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipe.html", recipes=recipes)


@app.route("/recipe/<categories>")
def recipe(categories):
    # Show recipes of that specific category
    if categories == "all":
        recipes = list(mongo.db.recipes.find())
    elif categories == "snacks":
        recipes = list(mongo.db.recipes.find({"category_name": "Snacks"}))
    elif categories == "main_course":
        recipes = list(mongo.db.recipes.find({"category_name": "Main_Course"}))
    elif categories == "dessert":
        recipes = list(mongo.db.recipes.find({"category_name": "Dessert"}))
    elif categories == "drinks":
        recipes = list(mongo.db.recipes.find({"category_name": "Drinks"}))

    return render_template(
        "recipe.html", recipes=recipes, categories=categories)

#--------------User signup-------------#
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("mypage", username=session["user"]))

    return render_template("signup.html")


#--------------Users login-------------#
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                            "mypage", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


#--------------Mypage(Profile)-------------#
@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    if not session.get("user"):
        return render_template("error_handlers/404.html")
        
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        if session["user"] == "admin@gmail.com":
            user_recipes = list(mongo.db.recipes.find())
        else:
            user_recipes = list(
                mongo.db.recipes.find({"username": session["user"]}))
        return render_template(
            "mypage.html", username=username, user_recipes=user_recipes)
    return redirect(url_for("login"))


#--------------Logout-------------#
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


#--------------Contact Page-------------#
@app.route("/contact")
def contact():
    return render_template("contact.html")


#--------------Recipes description-------------#
@app.route("/recipes/<recipe_id>")
def recipes(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not recipe:
        return render_template("error_handlers/404.html")
        
    return render_template("recipes.html", recipe=recipe)


#--------------Add new recipe to db-------------#
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if not session.get("user"):
        return render_template("error_handlers/404.html")

    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "chef": request.form.get("chef"),
            "image": request.form.get("image"),
            "serving": request.form.get("serving"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "total_time": request.form.get("total_time"),
            "ingredients": request.form.get("ingredients"),
            "directions": request.form.get("directions"),
            "username": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe is successfully added")
        return redirect(url_for("mypage", username=session['user']))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_recipe.html", categories=categories)


#--------------Edit recipe from db-------------#
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    
    if not session.get("user"):
        return render_template("error_handlers/404.html")

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "chef": request.form.get("chef"),
            "image": request.form.get("image"),
            "serving": request.form.get("serving"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "total_time": request.form.get("total_time"),
            "ingredients": request.form.get("ingredients"),
            "directions": request.form.get("directions"),
            "username": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


#--------------Delete recipe-------------#
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("mypage"))


#--------------Newsletter-------------#
@app.route("/newsletter", methods=["GET", "POST"])
def newsletter():
    if request.method == "POST":
        existing_user = mongo.db.newsletter.find_one(
            {"email_id": request.form.get("email_id").lower()})

        if existing_user:
            flash("Already Subscribed")
            return redirect(url_for("contact"))

        newsletter = {
            "email_id": request.form.get("email_id").lower(),
        }
        mongo.db.newsletter.insert_one(newsletter)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)