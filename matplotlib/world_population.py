
import json

with open('population_data.json') as file_object:
    pop_data = json.load(file_object)

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))

            print(country_name, population)
