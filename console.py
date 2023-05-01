from models.continent import Continent
from models.country import Country
from models.city import City
from models.visit import Visit


import repositories.continent_repository as continent_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.visit_repository as visit_repository

continent_repository.delete_all()
country_repository.delete_all()
city_repository.delete_all()
visit_repository.delete_all()


continent1 = Continent("Africa")
continent2 = Continent("North America")
continent3 = Continent("South America")
continent4 = Continent("Europe")
continent5 = Continent("Asia")
continent6 = Continent("Antarctica")
continent7 = Continent("Australia")




country1 = Country("Ghana", continent1)
country2 = Country("Egypt", continent1)
country3 = Country("France", continent4)
country4 = Country("Isreal", continent5)
country5 = Country("United States", continent2)


city1 = City("Accra", country1)
city2 = City("Cairo", country2)
city3 = City("Paris", country3)
city4 = City("Jerusalem", country4)
city5 = City("New York", country5)

visit1 = Visit(city1,True, "2023-01-11")
visit2 = Visit(city2,False)
visit3 = Visit(city3,True, "2022-11-20")
visit4 = Visit(city4,False)
visit5 = Visit(city5,True, "2022-08-29")

continent_repository.save(continent1)
continent_repository.save(continent2)
continent_repository.save(continent3)
continent_repository.save(continent4)
continent_repository.save(continent5)
continent_repository.save(continent6)
continent_repository.save(continent7)

country_repository.save(country1)
country_repository.save(country2)
country_repository.save(country3)
country_repository.save(country4)
country_repository.save(country5)


city_repository.save(city1)
city_repository.save(city2)
city_repository.save(city3)
city_repository.save(city4)
city_repository.save(city5)


visit_repository.save(visit1)
visit_repository.save(visit2)
visit_repository.save(visit3)
visit_repository.save(visit4)
visit_repository.save(visit5)

visit_repository.delete(visit1.id)

visit_selected = visit_repository.select(visit2.id)
print(f"{visit_selected.city.name}")
