"""
3D Transformations Demo

This script demonstrates various 3D transformations using the Matrix3D class.
It creates a 3D scene with multiple objects and applies different transformations.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Add parent directory to path to import our modules
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matrix3d.matrix3d import Matrix3D
from matrix3d.transformations import look_at, perspective, euler_angles_to_matrix
from matrix3d.visualization import plot_3d_points, plot_3d_mesh, create_cube, create_sphere, plot_coordinate_frame

def main():
    # Create a simpler layout with just one plot at a time
    def show_plot(title):
        plt.figure(figsize=(10, 8))
        ax = plt.axes(projection='3d')
        ax.set_title(title)
        return ax
    
    # Generate some random 3D points
    np.random.seed(42)
    points = np.random.rand(50, 3) * 10 - 5  # Points in [-5, 5] range
    
    # Plot 1: Basic 3D Points
    ax1 = show_plot('1. Random 3D Points')
    plot_3d_points(points, ax=ax1, color='b', marker='o', label='Points')
    plot_coordinate_frame(ax1, length=2.0)
    plt.tight_layout()
    plt.show()
    
    # Plot 2: Transformed Points
    ax2 = show_plot('2. Transformed Points')
    rotation = Matrix3D.rotation_x(30) @ Matrix3D.rotation_y(45)
    translation = Matrix3D.translation(2, 1, 0)
    transform = translation @ rotation
    transformed_points = transform.transform_points(points)
    plot_3d_points(points, ax=ax2, color='b', marker='o', label='Original')
    plot_3d_points(transformed_points, ax=ax2, color='r', marker='^', label='Transformed')
    plot_coordinate_frame(ax2, Matrix3D.identity(), length=2.0)
    plot_coordinate_frame(ax2, transform, length=2.0)
    ax2.legend()
    plt.tight_layout()
    plt.show()
    
    # Plot 3: 3D Cube
    ax3 = show_plot('3. Transformed Cube')
    cube_vertices, cube_faces = create_cube(2.0)
    cube_transform = (
        Matrix3D.translation(-3, 0, 0) @
        Matrix3D.rotation_x(20) @
        Matrix3D.rotation_y(30) @
        Matrix3D.scale(1, 1.5, 0.8)
    )
    transformed_cube = cube_transform.transform_points(cube_vertices)
    plot_3d_mesh(transformed_cube, cube_faces, ax=ax3, color='lightgreen', alpha=0.8)
    plot_coordinate_frame(ax3, cube_transform, length=1.5)
    plt.tight_layout()
    plt.show()
    
    # Plot 4: Complex Scene
    ax4 = show_plot('4. Complex 3D Scene')
    
    # Add a ground plane
    ground_size = 10
    ground_vertices, ground_faces = create_cube(ground_size * 2)
    ground_vertices = ground_vertices * np.array([1, 0.1, 1])  # Flatten in Y
    ground_vertices[:, 1] = -1  # Move to bottom
    plot_3d_mesh(ground_vertices, ground_faces, ax=ax4, color='#f0f0f0', alpha=0.5)
    
    # Add some objects
    objects = [
        ([-3, 0, 0], 'lightcoral', Matrix3D.rotation_y(45) @ Matrix3D.scale(1.5, 1, 1)),
        ([3, 1, 2], 'lightblue', Matrix3D.rotation_x(30) @ Matrix3D.scale(1, 1.5, 1)),
        ([0, 0.5, -3], 'lightgreen', Matrix3D.rotation_y(30) @ Matrix3D.scale(1, 1, 1.5))
    ]
    
    for pos, color, transform in objects:
        vertices, faces = create_cube(1.5)
        transform = Matrix3D.translation(*pos) @ transform
        vertices = transform.transform_points(vertices)
        plot_3d_mesh(vertices, faces, ax=ax4, color=color, alpha=0.8)
        plot_coordinate_frame(ax4, transform, length=1.0)
    
    plt.tight_layout()
    plt.show()
    
    return  # Early return to avoid running the rest of the original code
    
    # ===== Subplot 1: Basic 3D Points =====
    ax1 = fig.add_subplot(221, projection='3d')
    
    # Generate some random 3D points
    np.random.seed(42)
    points = np.random.rand(50, 3) * 10 - 5  # Points in [-5, 5] range
    
    # Plot the points
    plot_3d_points(points, ax=ax1, color='b', marker='o', label='Points')
    plot_coordinate_frame(ax1, length=2.0)
    ax1.set_title('1. Random 3D Points')
    
    # ===== Subplot 2: Transformed Points =====
    ax2 = fig.add_subplot(222, projection='3d')
    
    # Create a transformation matrix (rotation + translation)
    rotation = Matrix3D.rotation_x(30) @ Matrix3D.rotation_y(45)
    translation = Matrix3D.translation(2, 1, 0)
    transform = translation @ rotation
    
    # Apply transformation to points
    transformed_points = transform.transform_points(points)
    
    # Plot original and transformed points
    plot_3d_points(points, ax=ax2, color='b', marker='o', label='Original')
    plot_3d_points(transformed_points, ax=ax2, color='r', marker='^', label='Transformed')
    plot_coordinate_frame(ax2, Matrix3D.identity(), length=2.0)
    plot_coordinate_frame(ax2, transform, length=2.0)
    ax2.legend()
    ax2.set_title('2. Transformed Points')
    
    # ===== Subplot 3: 3D Cube with Transformations =====
    ax3 = fig.add_subplot(223, projection='3d')
    
    # Create a cube
    cube_vertices, cube_faces = create_cube(2.0)
    
    # Create transformation for the cube
    cube_transform = (
        Matrix3D.translation(-3, 0, 0) @
        Matrix3D.rotation_x(20) @
        Matrix3D.rotation_y(30) @
        Matrix3D.scale(1, 1.5, 0.8)
    )
    
    # Apply transformation to cube vertices
    transformed_cube = cube_transform.transform_points(cube_vertices)
    
    # Plot the cube
    plot_3d_mesh(transformed_cube, cube_faces, ax=ax3, color='lightgreen', alpha=0.8)
    plot_coordinate_frame(ax3, cube_transform, length=1.5)
    ax3.set_title('3. Transformed Cube')
    
    # ===== Subplot 4: Complex Scene with Multiple Objects =====
    ax4 = fig.add_subplot(224, projection='3d')
    
    # Create a sphere with lower resolution to prevent index issues
    sphere_vertices, sphere_faces = create_sphere(1.5, resolution=8)
    
    # Create multiple transformed spheres
    for i in range(3):
        angle = i * 120
        radius = 4.0
        x = np.cos(np.radians(angle)) * radius
        z = np.sin(np.radians(angle)) * radius
        
        # Create transformation for this sphere
        sphere_transform = (
            Matrix3D.translation(x, 0, z) @
            Matrix3D.rotation_y(angle) @
            Matrix3D.scale(1.0, 0.7 + 0.3 * (i % 2), 1.0)
        )
        
        # Apply transformation to sphere vertices
        transformed_sphere = sphere_transform.transform_points(sphere_vertices)
        
        # Plot the sphere
        color = ['lightblue', 'lightcoral', 'lightyellow'][i % 3]
        plot_3d_mesh(transformed_sphere, sphere_faces, ax=ax4, color=color, alpha=0.7)
        plot_coordinate_frame(ax4, sphere_transform, length=1.5)
    
    # Add a central object (cube)
    central_cube_transform = Matrix3D.rotation_x(15) @ Matrix3D.rotation_y(25)
    transformed_central_cube = central_cube_transform.transform_points(cube_vertices * 0.7)
    plot_3d_mesh(transformed_central_cube, cube_faces, ax=ax4, color='lavender', alpha=0.9)
    plot_coordinate_frame(ax4, central_cube_transform, length=1.0)
    
    ax4.set_title('4. Complex 3D Scene')
    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()
    
    # ===== Interactive 3D Visualization =====
    print("\nCreating interactive 3D visualization...")
    
    # Create a well-proportioned figure for interactive visualization
    fig = plt.figure(figsize=(10, 8))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
    ax = fig.add_subplot(111, projection='3d')
    
    # Create a more complex scene
    
    # 1. Add a ground plane
    ground_size = 10
    ground_vertices = np.array([
        [-ground_size, -1, -ground_size],
        [ground_size, -1, -ground_size],
        [ground_size, -1, ground_size],
        [-ground_size, -1, ground_size]
    ])
    ground_faces = [(0, 1, 2, 3)]
    
    # Create a checkerboard pattern for the ground
    for i in range(-ground_size, ground_size):
        for j in range(-ground_size, ground_size):
            if (i + j) % 2 == 0:
                color = '0.9'  # light gray
            else:
                color = '0.8'  # slightly darker gray
            
            # Create a small square for each cell
            square_vertices = np.array([
                [i, -0.99, j],
                [i+1, -0.99, j],
                [i+1, -0.99, j+1],
                [i, -0.99, j+1]
            ])
            
            # Plot the square
            square = Poly3DCollection([square_vertices], alpha=0.5, linewidths=0.5, edgecolor='0.7')
            square.set_facecolor(color)
            ax.add_collection3d(square)
    
    # 2. Add multiple objects with different transformations
    objects = []
    
    # Object 1: Rotating cube
    cube_pos = np.array([-3, 0, 0])
    cube_rot = Matrix3D.rotation_x(20) @ Matrix3D.rotation_y(45)
    cube_scale = Matrix3D.scale(1, 1.5, 1)
    cube_transform = Matrix3D.translation(*cube_pos) @ cube_rot @ cube_scale
    cube_vertices, cube_faces = create_cube(1.5)
    transformed_cube = cube_transform.transform_points(cube_vertices)
    plot_3d_mesh(transformed_cube, cube_faces, ax=ax, color='lightcoral', alpha=0.9)
    plot_coordinate_frame(ax, cube_transform, length=1.5)
    
    # Object 2: Sphere
    sphere_pos = np.array([3, 1, 2])
    sphere_scale = Matrix3D.scale(1.5, 1.0, 1.5)
    sphere_transform = Matrix3D.translation(*sphere_pos) @ sphere_scale
    sphere_vertices, sphere_faces = create_sphere(1.0, resolution=12)
    transformed_sphere = sphere_transform.transform_points(sphere_vertices)
    plot_3d_mesh(transformed_sphere, sphere_faces, ax=ax, color='lightblue', alpha=0.9)
    plot_coordinate_frame(ax, sphere_transform, length=1.5)
    
    # Object 3: Pyramid
    pyramid_vertices = np.array([
        [0, 0, 0], [2, 0, 0], [2, 0, 2], [0, 0, 2],  # base
        [1, 2, 1]  # apex
    ])
    pyramid_faces = [
        (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4),  # sides
        (0, 1, 2, 3)  # base
    ]
    
    pyramid_pos = np.array([0, 0, -3])
    pyramid_rot = Matrix3D.rotation_y(30)
    pyramid_transform = Matrix3D.translation(*pyramid_pos) @ pyramid_rot
    transformed_pyramid = pyramid_transform.transform_points(pyramid_vertices)
    
    # Plot pyramid (convert quads to triangles for plotting)
    for face in pyramid_faces:
        if len(face) == 3:
            poly = Poly3DCollection([transformed_pyramid[list(face)]], alpha=0.9, linewidths=1, edgecolor='k')
        else:  # quad face (base)
            poly = Poly3DCollection([transformed_pyramid[[face[0], face[1], face[2]], :], 
                                   transformed_pyramid[[face[0], face[2], face[3]], :]], 
                                  alpha=0.9, linewidths=1, edgecolor='k')
        poly.set_facecolor('lightgreen')
        ax.add_collection3d(poly)
    
    plot_coordinate_frame(ax, pyramid_transform, length=1.5)
    
    # Set up the view
    ax.set_xlim(-5, 5)
    ax.set_ylim(-2, 5)
    ax.set_zlim(-5, 5)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Interactive 3D Scene')
    
    # Enable interactive rotation
    print("Use your mouse to rotate and zoom the 3D view.")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
