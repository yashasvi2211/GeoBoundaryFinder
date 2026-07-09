import streamlit as st
from search import search_location
from boundary import get_boundary
from map import show_map

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="GeoBoundary Finder",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🗺️ GeoBoundary Finder")
st.write("Search any place to display its location and administrative boundary.")

# ----------------------------
# Search Box
# ----------------------------
place = st.text_input(
    "Search Place",
    placeholder="Example: Ponda, Goa"
)

# ----------------------------
# Search Button
# ----------------------------
if place:

    result = search_location(place)

    if result:

        st.success(result["name"])

        st.write("📍 Latitude :", result["lat"])
        st.write("📍 Longitude:", result["lon"])

        # Get Administrative Boundary
        boundary = get_boundary(place)

        # Display Map
        show_map(
            result["lat"],
            result["lon"],
            boundary
        )

    else:

        st.error("❌ Location not found.")