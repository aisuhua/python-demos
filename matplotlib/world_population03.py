
import pygal

world_map_chart = pygal.maps.world.World()
world_map_chart.title = 'Population of Countries in North America'

world_map_chart.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

world_map_chart.render_to_file('america.svg')
