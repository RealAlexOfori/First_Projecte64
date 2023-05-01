from flask import Flask, render_template, request, redirect
from models.city import City

import repositories.city_repository as city_repo
import repositories.country_repository as country_repo




from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@cities_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all()
    countries = country_repo.select_all()
    return render_template("cities/index.html", all_cities = cities, all_countries = countries)

@cities_blueprint.route("/cities/new")
def new_city():
    countries = country_repo.select_all()
    return render_template("cities/new.html", all_countries = countries)

@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
     city_name = request.form['name']
     country = country_repo.select(request.form['country_id'])
     visited   = request.form.get('visited') == 'visited'
     city = City(city_name, country, visited)
     city_repo.save(city)
     return redirect('/cities')



@cities_blueprint.route("/cities/<id>/show")
def show_city(id):
    selected_city = city_repo.select(id)
    return render_template("cities/show.html", city = selected_city)


@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    countries = country_repo.select_all()
    selected_city = city_repo.select(id)
    return render_template("cities/edit.html", city = selected_city, all_countries = countries)

# @cities_blueprint.route("/cities/<id>", methods=['POST'])
# def update_city(id):
#     name = request.form['name']
#     country = country_repo.select(request.form['country_id'])
#     city = City(name, country, id)
#     city_repo.update(city)
#     return redirect('/cities')

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repo.delete(id)
    return redirect('/cities')