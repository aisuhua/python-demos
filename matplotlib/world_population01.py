
import json
from countries import get_country_code

# 获取国家对应的的code

with open('population_data.json') as file_object:
    pop_data = json.load(file_object)

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))

            code = get_country_code(country_name)
            if code:
                print(code + ': ' + str(population))
            else:
                print('ERROR - ' + country_name)
