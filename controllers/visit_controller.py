from flask import Flask, render_template, request, redirect
from models.visit import Visit

import repositories.visit_repository as visit_repo
import repositories.city_repository as city_repo



from flask import Blueprint

visits_blueprint = Blueprint("visits", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@visits_blueprint.route("/visits")
def visits():
    visits = visit_repo.select_all()
    return render_template("visits/index.html", all_visits = visits)


@visits_blueprint.route("/visits", methods=['POST'])
def create_visit():
    city_id = request.form['city_id']
    city = city_repo.select(city_id)
    #I put a new visit code below
    visited = request.form['visited']
    visit_date = request.form['visit_date']
    visit = Visit(city, visited, visit_date)
    visit_repo.save(visit)
    return redirect('/visits')


@visits_blueprint.route("/visits/<id>/edit")
def edit_visit(id):
    visit = visit_repo.select(id)
    cities = city_repo.select_all()
    return render_template("visits/edit.html", visit = visit, all_cities = cities)

@visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
def delete_visit(id):
    visit_repo.delete(id)
    return redirect('/visits')