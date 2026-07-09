import osmnx as ox


def get_boundary(place):

    try:

        gdf = ox.geocode_to_gdf(place)

        return gdf

    except Exception:

        return None