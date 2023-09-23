import folium
import math

def functionone():
    i = int(input("Pressure(psi):"))
    Npm = i*6894.76
    rad = float(input("Rad B7 bolt:"))
    Ar = (3.14)*(rad**2)
    m = float(input("Mass:"))

    v_ini = Npm*Ar/(m*(10**(1/2)))

    r = (v_ini**2)/9.8
    return r/1000


# Create a map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Define marker coordinates and popup labels
marker_data = [
    {"location": [22.331667, 69.747222], "label": "Vadinar Refinery"},
    {"location": [20.247639, 86.598194], "label": "Paradip Refinery"},
    {"location": [13.160444, 80.277528], "label": "Manali Refinery"},
    {"location": [22.048028, 88.106528], "label": "Haldia Refinery"},
    {"location": [27.390833, 95.618611], "label": "Digboi Refinery"},
    # Add more markers as needed
]

# Add markers to the map
for marker in marker_data:
    folium.Marker(
        location=marker["location"],
        popup=marker["label"],
        icon=folium.Icon(icon="cloud"),
    ).add_to(india_map)


# Define circular areas (buffers)
circle_data = [
    {"location": [22.331667, 69.747222], "radius": functionone(), "color": "blue", "fill": True},
    {"location": [20.247639, 86.598194], "radius": functionone(), "color": "green", "fill": True},
    {"location": [13.160444, 80.277528], "radius": functionone(), "color": "red", "fill": True},
    {"location": [22.048028, 88.106528], "radius": functionone(), "color": "purple", "fill": True},
    {"location": [27.390833, 95.618611], "radius": functionone(), "color": "purple", "fill": True},
    # Add more circular areas as needed
]

# Add circular areas to the map
for circle in circle_data:
    folium.Circle(
        location=circle["location"],
        radius=circle["radius"],
        color=circle["color"],
        fill=circle["fill"],
        fill_opacity=0.4,  # Adjust the fill opacity as needed
    ).add_to(india_map)


# Display the map
india_map.save("india_map.html")

