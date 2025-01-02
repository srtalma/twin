import pyvista as pv
import streamlit as st
from streamlit_pyvista import st_pyvista

# App Title
st.title("3D Digital Twin of the Marketing Company")
st.subheader("Explore the company structure and processes in 3D!")

# Sidebar Input
st.sidebar.header("Interactive Settings")
model_color = st.sidebar.color_picker("Choose Model Color", "#add8e6")  # Default: Light blue
show_axes = st.sidebar.checkbox("Show Axes", value=True)
lighting = st.sidebar.selectbox("Lighting Mode", ["Flat", "Gouraud", "Phong"])

# Load the 3D Model
st.sidebar.header("Model File")
uploaded_file = st.sidebar.file_uploader("Upload your 3D model file (.obj, .stl, .gltf)", type=["obj", "stl", "gltf"])

if uploaded_file:
    # Read the uploaded model
    mesh = pv.read(uploaded_file)

    # Create a Pyvista plotter
    plotter = pv.Plotter(off_screen=True)
    
    # Customize plotter
    plotter.add_mesh(mesh, color=model_color, smooth_shading=True if lighting != "Flat" else False)
    if show_axes:
        plotter.show_axes()
    
    # Render the 3D Model
    st_pyvista(plotter, key="3d_model_view")
else:
    st.warning("Please upload a 3D model file to view the Digital Twin.")
