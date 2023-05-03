from db.run_sql import run_sql
import repositories.country_repository as country_repo

from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES ( %s, %s) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql( sql, values )
    city.id = results[0]['id']


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repo.select(row['country_id'])
        city = City(row['name'], country, row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repo.select(result['country_id'])
        city = City(result['name'], country, result['id'])
    return city

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def update(city):
    sql = "UPDATE cities SET (name, country_id) = (%s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.id]
    run_sql(sql, values)
    

