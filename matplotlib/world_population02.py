
import pygal

world_map_chart = pygal.maps.world.World()
world_map_chart.title = 'North, Central and South America'

world_map_chart.add('North America', ['ca', 'mx', 'us'])
world_map_chart.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
world_map_chart.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

world_map_chart.render_to_file('america.svg')
