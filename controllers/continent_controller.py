from flask import Flask, render_template, request, redirect
from models.continent import Continent


import repositories.continent_repository as continent_repo


from flask import Blueprint

continents_blueprint = Blueprint("continents", __name__)


# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@continents_blueprint.route("/continents")
def continents():
    continents = continent_repo.select_all()
    return render_template("continents/index.html", all_continents = continents)

@continents_blueprint.route("/continents/new")
def new_continent():
    return render_template("continents/new.html")

@continents_blueprint.route("/continents", methods=['POST'])
def create_continent():
    continent_name = request.form['name']
    continent = Continent(continent_name)
    continent_repo.save(continent)
    return redirect('/continents')


@continents_blueprint.route("/continents/<id>/edit")
def edit_continent(id):
    selected_continent = continent_repo.select(id)
    return render_template("continents/edit.html", continent = selected_continent)

@continents_blueprint.route("/continents/<id>", methods=['POST'])
def update_continent(id):
    name = request.form['name']
    continent = Continent(name, id)
    continent_repo.update(continent)
    return redirect('/continents')

@continents_blueprint.route("/continents/<id>/delete", methods=['POST'])
def delete_continent(id):
    continent_repo.delete(id)
    return redirect('/continents')