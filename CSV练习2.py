# import json
# filename='population_data.json'
# with open(filename) as f:
#     pop_data=json.load(f)
#     for pop_dict in pop_data:
#         if pop_dict['Year']=='2010':
#             country_name=pop_dict['Country Name']
#             population=int(float(pop_dict['Value']))
#             print(country_name+':'+str(+population))
### 国别码的获取，需要pygal当中的il8n模块，
# from pygal_maps_world.i18n import COUNTRIES
# def get_country_code(country_name):
#     for code,name in COUNTRIES.items():
#         if name==country_name:
#             return code
#     return None
# print(get_country_code('China'))

###将json文件中的国名换成国别

# import json
# from pygal_maps_world.i18n import COUNTRIES
# filename='population_data.json'
# def get_country_code(country_name):
#      for code,name in COUNTRIES.items():
#         if name==country_name:
#             return code
#      return None
# with open(filename) as f:
#     pop_data=json.load(f)
#     for pop_dict in pop_data:
#         if pop_dict['Year']=='2010':
#             country_name=pop_dict['Country Name']
#             population=int(float(pop_dict['Value']))
#             code=get_country_code(country_name)
#             if code:
#                 print(code+':'+str(population))
#             else:
#                 print('Error-'+country_name+':'+str(population))



###制作世界地图
# import pygal_maps_world.maps
# wm=pygal_maps_world.maps.WORLD_MAP()
# wm.title='North, Central, and South America'
# wm.add('North America',['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.add('Asia',['cn'])
# wm.render_to_file('chinas.svg')
# wm=pygal_maps_world.maps .World()
# wm.title='North, Central, and South America'
# wm.add('North America',['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.add('Asia',['cn'])
# wm.render_to_file('chinas.svg')
# import pygal_maps_world.maps
# wm=pygal_maps_world.maps.World()
# wm.title='populations in countries of North America'
# wm.add('North America',{'ca':100000,'us':12000,'mx':130000})
# wm.render_to_file('na_population.svg')
import json
import pygal_maps_world.maps
import pygal_maps_world.i18n
filename='population_data.json'
cc_population={}
def get_country_code(country_name):
    for code,name in pygal_maps_world.i18n.COUNTRIES.items():
        if country_name==name:
            return code
        else:
            return None
with open(filename) as f:
    pop_data=json.load(f)
    for pop_dict in pop_data:
        if pop_dict['year']=='2010':
            country_name=pop_dict['Country Name']
            population=int(float(pop_dict['Value']))
            code=get_country_code(country_name)
            if code :
                cc_population[code]=population