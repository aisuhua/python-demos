
import json
import pygal
from countries import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

# 展示世界各国人口分布图

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

with open('population_data.json') as file_object:
    pop_data = json.load(file_object)

    for pop_dict in pop_data:
        if pop_dict['Year'] != '2010':
            continue

        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            if population < 10000000:
                cc_pops_1[code] = population
            elif population < 1000000000:
                cc_pops_2[code] = population
            else:
                cc_pops_3[code] = population

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

base_style = LightColorizedStyle
style = RotateStyle('#336699', base_style=base_style)

world_map_chart = pygal.maps.world.World(style=style)
world_map_chart.title = 'World Population is 2010, by Country'
world_map_chart.add('0-10m', cc_pops_1)
world_map_chart.add('10m-1bn', cc_pops_2)
world_map_chart.add('>1bn', cc_pops_3)

world_map_chart.render_to_file('world_population.svg')

