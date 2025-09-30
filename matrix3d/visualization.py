"""
3D Visualization Module.

This module provides utilities for visualizing 3D objects and transformations
using Matplotlib and PyOpenGL.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import List, Tuple, Optional, Union

from .matrix3d import Matrix3D

def plot_3d_points(points: np.ndarray, 
                  ax: Optional[plt.Axes] = None,
                  color: str = 'b',
                  marker: str = 'o',
                  label: Optional[str] = None) -> plt.Axes:
    """Plot 3D points using Matplotlib.
    
    Args:
        points: Nx3 array of 3D points
        ax: Optional 3D axis to plot on
        color: Color of the points
        marker: Marker style
        label: Label for the points
        
    Returns:
        The 3D axis used for plotting
    """
    if ax is None:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], 
              c=color, marker=marker, label=label)
    
    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Points Visualization')
    
    # Equal aspect ratio
    max_range = np.array([points[:, 0].max()-points[:, 0].min(), 
                         points[:, 1].max()-points[:, 1].min(), 
                         points[:, 2].max()-points[:, 2].min()]).max() / 2.0
    
    mid_x = (points[:, 0].max() + points[:, 0].min()) * 0.5
    mid_y = (points[:, 1].max() + points[:, 1].min()) * 0.5
    mid_z = (points[:, 2].max() + points[:, 2].min()) * 0.5
    
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    if label:
        ax.legend()
    
    return ax

def plot_3d_mesh(vertices: np.ndarray, 
                faces: List[Tuple[int, int, int]],
                ax: Optional[plt.Axes] = None,
                color: str = 'cyan',
                alpha: float = 0.5,
                edgecolor: str = 'k') -> plt.Axes:
    """Plot a 3D mesh using Matplotlib.
    
    Args:
        vertices: Nx3 array of vertex positions
        faces: List of face indices (triples of vertex indices)
        ax: Optional 3D axis to plot on
        color: Face color of the mesh
        alpha: Transparency of the mesh
        edgecolor: Color of the mesh edges
        
    Returns:
        The 3D axis used for plotting
    """
    if ax is None:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
    
    # Create the poly collection
    poly3d = [[vertices[vertex] for vertex in face] for face in faces]
    mesh = Poly3DCollection(poly3d, alpha=alpha, linewidths=1, edgecolor=edgecolor)
    mesh.set_facecolor(color)
    
    ax.add_collection3d(mesh)
    
    # Auto-scale the plot
    points = np.array(poly3d).reshape(-1, 3)
    max_range = np.array([points[:, 0].max()-points[:, 0].min(), 
                         points[:, 1].max()-points[:, 1].min(), 
                         points[:, 2].max()-points[:, 2].min()]).max() / 2.0
    
    mid_x = (points[:, 0].max() + points[:, 0].min()) * 0.5
    mid_y = (points[:, 1].max() + points[:, 1].min()) * 0.5
    mid_z = (points[:, 2].max() + points[:, 2].min()) * 0.5
    
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Mesh Visualization')
    
    return ax

def plot_coordinate_frame(ax: plt.Axes, 
                        transform: Optional[Matrix3D] = None,
                        length: float = 1.0) -> None:
    """Plot a 3D coordinate frame.
    
    Args:
        ax: 3D axis to plot on
        transform: Optional transformation matrix for the frame
        length: Length of the axis arrows
    """
    # Define the origin and axis vectors
    origin = np.zeros(3)
    x_axis = np.array([length, 0, 0])
    y_axis = np.array([0, length, 0])
    z_axis = np.array([0, 0, length])
    
    # Apply transformation if provided
    if transform is not None:
        origin = transform.transform_point(origin)
        x_axis = transform.transform_point(x_axis) - origin + origin
        y_axis = transform.transform_point(y_axis) - origin + origin
        z_axis = transform.transform_point(z_axis) - origin + origin
    
    # Plot the axes
    ax.quiver(*origin, *x_axis, color='r', arrow_length_ratio=0.1, linewidth=2)
    ax.quiver(*origin, *y_axis, color='g', arrow_length_ratio=0.1, linewidth=2)
    ax.quiver(*origin, *z_axis, color='b', arrow_length_ratio=0.1, linewidth=2)
    
    # Add labels
    ax.text(*(origin + x_axis*1.1), 'X', color='r')
    ax.text(*(origin + y_axis*1.1), 'Y', color='g')
    ax.text(*(origin + z_axis*1.1), 'Z', color='b')

def create_cube(size: float = 1.0) -> Tuple[np.ndarray, List[Tuple[int, int, int]]]:
    """Create vertices and faces for a cube.
    
    Args:
        size: Size of the cube (edge length)
        
    Returns:
        Tuple of (vertices, faces)
    """
    s = size / 2.0
    vertices = np.array([
        [-s, -s, -s], [s, -s, -s], [s, s, -s], [-s, s, -s],
        [-s, -s, s], [s, -s, s], [s, s, s], [-s, s, s]
    ])
    
    faces = [
        (0, 1, 2, 3),  # bottom
        (4, 5, 6, 7),  # top
        (0, 1, 5, 4),  # front
        (2, 3, 7, 6),  # back
        (1, 2, 6, 5),  # right
        (0, 3, 7, 4),  # left
    ]
    
    # Convert quads to triangles
    tri_faces = []
    for face in faces:
        tri_faces.append((face[0], face[1], face[2]))
        tri_faces.append((face[0], face[2], face[3]))
    
    return vertices, tri_faces

def create_sphere(radius: float = 1.0, resolution: int = 8) -> Tuple[np.ndarray, List[Tuple[int, int, int]]]:
    """Create vertices and faces for a sphere.
    
    Args:
        radius: Radius of the sphere
        resolution: Number of subdivisions (lower = less detailed, but more stable)
        
    Returns:
        Tuple of (vertices, faces)
    """
    # Use a simpler approach using icosahedron subdivision
    # This is more reliable than the parametric approach
    
    # Golden ratio
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    
    # Vertices of an icosahedron
    vertices = [
        [-1.0,  phi, 0.0],
        [ 1.0,  phi, 0.0],
        [-1.0, -phi, 0.0],
        [ 1.0, -phi, 0.0],
        
        [0.0, -1.0,  phi],
        [0.0,  1.0,  phi],
        [0.0, -1.0, -phi],
        [0.0,  1.0, -phi],
        
        [ phi, 0.0, -1.0],
        [ phi, 0.0,  1.0],
        [-phi, 0.0, -1.0],
        [-phi, 0.0,  1.0],
    ]
    
    # Faces of an icosahedron (20 triangles)
    faces = [
        # 5 faces around point 0
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        # 5 adjacent faces
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        # 5 faces around point 3
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        # 5 adjacent faces
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1],
    ]
    
    # Convert to numpy array and normalize vertices to unit sphere
    vertices = np.array(vertices, dtype=np.float32)
    vertices = vertices / np.linalg.norm(vertices, axis=1, keepdims=True)
    
    # Scale by radius
    vertices = vertices * radius
    
    # Convert faces to tuples of integers
    faces = [tuple(face) for face in faces]
    
    return vertices, faces
