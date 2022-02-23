import folium

from location import locate

def show_path(points):
    return '-->'.join(points)


def get_map_html(datas,distance, save_path):
    cols = ['green']*len(datas)
    cols[0] = 'red'
    cols[-1] = 'red'
    pops = ['<p>{0}:{1}</p>'.format(d[0], locate[d[0]]) for d in datas]
    pops[0] = '<b>Starting Point: {0}.</b>'.format(pops[0])
    pops[-1] = '<b>Ending Point: {0}.</b>'.format(pops[-1])
    # define the world map
    world_map = folium.Map()  
    points = []
    for i in range(len(datas)):
        d = datas[i]
        points.append(d[0])
        folium.Marker(location=locate[d[0]], popup=pops[i], icon=folium.Icon(color=cols[i], icon='map-marker')
        , control_scale=True
        ).add_to(world_map)
    ls = folium.PolyLine(locations=[locate[e] for e in points], color='blue').add_to(world_map)
    folium.Marker(location=[55.7505, -39.3860], popup="<h6>Diatance: {0}</h6></hr><h6>Path: {1}</h6>".format(distance, show_path(points)), icon=folium.Icon(color=cols[i], icon='info-sign')).add_to(world_map)
    world_map.add_child(folium.LatLngPopup())
    world_map.save(save_path)
    return world_map._repr_html_()