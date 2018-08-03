import requests
import pygal
from pygal.style import LightenStyle, LightColorizedStyle

# 添加自定义工具提示：显示项目描述和超链接

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    description = repo_dict['description']
    if not description:
        description = 'No description provided.'
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 图表样式
my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

# 图表配置
my_config = pygal.Config()
my_config.show_legend = False
my_config.x_label_rotation = 45
my_config.show_y_guides = False
my_config.truncate_label = 15

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Started Python project in GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repo.svg')
