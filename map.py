import folium
from streamlit_folium import st_folium


def show_map(lat, lon, boundary=None):

    m = folium.Map(
        location=[lat, lon],
        zoom_start=13
    )

    folium.Marker(
        [lat, lon],
        popup="Selected Location"
    ).add_to(m)

    if boundary is not None:

        folium.GeoJson(
            boundary.__geo_interface__,
            name="Boundary",
            style_function=lambda x: {
                "color": "red",
                "weight": 3,
                "fillOpacity": 0.2
            }
        ).add_to(m)

    folium.LayerControl().add_to(m)

    st_folium(m, width=900, height=600)