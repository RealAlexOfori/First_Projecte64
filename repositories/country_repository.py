from db.run_sql import run_sql
import repositories.continent_repository as continent_repo

from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name, continent_id) VALUES ( %s, %s ) RETURNING id"
    values = [country.name, country.continent.id]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        continent = continent_repo.select(row['continent_id'])
        country = Country(row['name'], continent, row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        continent = continent_repo.select(result['continent_id'])
        country = Country(result['name'], continent, result['id'])
    return country

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def update(country):
    sql = "UPDATE countries SET (name, continent_id) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent.id, country.id]
    run_sql(sql, values)

def countries_by_continent(continent):
    countries = []
    sql = "SELECT * FROM countries WHERE continent_id = %s"
    values = [continent.id]
    results = run_sql(sql, values)

    for row in results:
        country = Country(row['name'], continent, row['id'])
        countries.append(country)
    return countries