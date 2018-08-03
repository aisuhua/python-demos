
import json
import pygal
from countries import get_country_code

# 展示世界各国人口分布图

cc_populations = {}

with open('population_data.json') as file_object:
    pop_data = json.load(file_object)

    for pop_dict in pop_data:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

world_map_chart = pygal.maps.world.World()
world_map_chart.title = 'World Population is 2010, by Country'
world_map_chart.add('2010', cc_populations)

world_map_chart.render_to_file('world_population.svg')

