from flask import Flask, render_template, request, redirect
from models.country import Country

import repositories.continent_repository as continent_repo
import repositories.country_repository as country_repo



from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    continents = continent_repo.select_all()
    return render_template("countries/index.html", all_countries = countries, all_continents = continents )

@countries_blueprint.route("/countries/new")
def new_country():
    continents = continent_repo.select_all()
    return render_template("countries/new.html", all_continents = continents)

@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    country_name = request.form['name']
    continent = continent_repo.select(request.form['continent_id'])
    country = Country(country_name, continent)
    country_repo.save(country)
    return redirect('/countries')


@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    continents = continent_repo.select_all()
    selected_country = country_repo.select(id)
    return render_template("countries/edit.html", country = selected_country, all_continents = continents)

@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    continent = continent_repo.select(request.form['continent_id'])
    country = Country(name, continent, id)
    country_repo.update(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repo.delete(id)
    return redirect('/countries')