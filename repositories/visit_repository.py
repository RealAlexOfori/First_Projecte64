from db.run_sql import run_sql

from models.visit import Visit
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import pdb

def save(visit):
    sql = "INSERT INTO visits (city_id, visited, visit_date ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [visit.city.id, visit.visited, visit.visit_date]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit


def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])

        visit = Visit(city, row['visited'], row['visit_date'], row['id'])
        visits.append(visit)
    return visits

def select(id):
    visit = None
    sql = "SELECT * FROM visits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        city = city_repository.select(result['city_id'])
        visit = Visit(city, result['visited'], result['visit_date'], result['id'])
    return visit



def city(visit):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [visit.city.id]
    country = country_repository.select(visit.city.country.id)
    results = run_sql(sql, values)[0]
    city = City(results['name'], country, results['id'])
    return city



def update(visit):
    sql = "UPDATE visits SET (city_id, visited, visit_date ) = (%s, %s, %s, %s) WHERE id = %s"
    values = [visit.city.id, visit.visited, visit.visit_date, visit.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM visits"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)