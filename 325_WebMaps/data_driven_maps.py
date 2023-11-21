import folium
import json
import os

m= folium.Map(location=[42.3601, -71.0589], zoom_start=12)

tooltip = "Click For More"

vis = os.path.join('data','vis.json')

folium.Marker([42.363600, -71.099500],
              popup='<strong>Location One</strong>',
              tooltip=tooltip,).add_to(m)

folium.Marker([42.363600, -71.109500],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon="cloud")).add_to(m)

folium.Marker([42.377600, -71.062500],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color="purple")).add_to(m)

folium.Marker([42.374600, -71.122500],
              popup='<strong>Location Four</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon="cloud", color="green")).add_to(m)

folium.Marker([42.315140, -71.072450],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(
                  open(vis)
              ), height=250, width=450))
              ).add_to(m)

# can add custom images as well

# circle marker
folium.CircleMarker(
    location=[40.52348305305064, -74.45880781296992],
    radius=50,
    popup='My Alma Mater',
    color="#428bca",
    fill=True,
    fill_color='#428bca'
).add_to(m)

m.save("map.html")