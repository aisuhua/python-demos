import requests
import pygal
from pygal.style import LightenStyle, LightColorizedStyle

# 使用直方图表示最受欢迎的项目

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LightenStyle('#333366', base_style=LightColorizedStyle)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Started Python project in GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repo.svg')
