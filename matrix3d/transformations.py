"""
3D Transformation Utilities.

This module provides utility functions for common 3D transformations
and spatial operations using the Matrix3D class.
"""
import numpy as np
from typing import Tuple, List, Optional
from .matrix3d import Matrix3D

def look_at(eye: np.ndarray, target: np.ndarray, up: np.ndarray = np.array([0, 1, 0])) -> Matrix3D:
    """Create a view matrix that looks from 'eye' to 'target'.
    
    Args:
        eye: 3D position of the camera
        target: 3D position to look at
        up: Up vector (default: [0, 1, 0])
        
    Returns:
        A Matrix3D representing the view transformation
    """
    forward = (target - eye)
    forward = forward / np.linalg.norm(forward)
    
    right = np.cross(forward, up)
    right = right / np.linalg.norm(right)
    
    up = np.cross(right, forward)
    up = up / np.linalg.norm(up)
    
    # Create rotation matrix
    rot = np.eye(4)
    rot[:3, 0] = right
    rot[:3, 1] = up
    rot[:3, 2] = -forward
    rot[3, 3] = 1.0
    
    # Create translation matrix
    trans = Matrix3D.translation(-eye[0], -eye[1], -eye[2])
    
    return Matrix3D(rot) @ trans

def perspective(fov: float, aspect: float, near: float, far: float) -> Matrix3D:
    """Create a perspective projection matrix.
    
    Args:
        fov: Field of view in degrees
        aspect: Aspect ratio (width / height)
        near: Near clipping plane distance
        far: Far clipping plane distance
        
    Returns:
        A Matrix3D representing the perspective projection
    """
    f = 1.0 / np.tan(np.radians(fov) / 2.0)
    depth = near - far
    
    proj = np.zeros((4, 4))
    proj[0, 0] = f / aspect
    proj[1, 1] = f
    proj[2, 2] = (far + near) / depth
    proj[2, 3] = 2 * far * near / depth
    proj[3, 2] = -1.0
    
    return Matrix3D(proj)

def orthographic(left: float, right: float, 
                bottom: float, top: float, 
                near: float, far: float) -> Matrix3D:
    """Create an orthographic projection matrix.
    
    Args:
        left, right: Left and right clipping planes
        bottom, top: Bottom and top clipping planes
        near, far: Near and far clipping planes
        
    Returns:
        A Matrix3D representing the orthographic projection
    """
    dx = right - left
    dy = top - bottom
    dz = far - near
    
    proj = np.eye(4)
    proj[0, 0] = 2.0 / dx
    proj[1, 1] = 2.0 / dy
    proj[2, 2] = -2.0 / dz
    
    proj[0, 3] = -(right + left) / dx
    proj[1, 3] = -(top + bottom) / dy
    proj[2, 3] = -(far + near) / dz
    
    return Matrix3D(proj)

def euler_angles_to_matrix(angles: np.ndarray, order: str = 'xyz') -> Matrix3D:
    """Convert Euler angles to rotation matrix.
    
    Args:
        angles: Array of 3 angles in degrees
        order: Rotation order, e.g., 'xyz', 'zyx', etc.
        
    Returns:
        A Matrix3D representing the combined rotation
    """
    if len(angles) != 3 or len(order) != 3:
        raise ValueError("Angles must have 3 elements and order must be 3 characters")
    
    result = Matrix3D.identity()
    
    for axis, angle in zip(order.lower(), angles):
        if axis == 'x':
            rot = Matrix3D.rotation_x(angle)
        elif axis == 'y':
            rot = Matrix3D.rotation_y(angle)
        elif axis == 'z':
            rot = Matrix3D.rotation_z(angle)
        else:
            raise ValueError(f"Invalid rotation axis: {axis}")
        
        result = rot @ result
    
    return result

def matrix_to_euler_angles(matrix: Matrix3D) -> np.ndarray:
    """Convert rotation matrix to Euler angles (XYZ order).
    
    Args:
        matrix: Rotation matrix to convert
        
    Returns:
        Array of 3 Euler angles in degrees
    """
    m = matrix.matrix
    
    # Extract rotation angles (XYZ order)
    sy = np.sqrt(m[0, 0] * m[0, 0] + m[1, 0] * m[1, 0])
    
    singular = sy < 1e-6
    
    if not singular:
        x = np.arctan2(m[2, 1], m[2, 2])
        y = np.arctan2(-m[2, 0], sy)
        z = np.arctan2(m[1, 0], m[0, 0])
    else:
        x = np.arctan2(-m[1, 2], m[1, 1])
        y = np.arctan2(-m[2, 0], sy)
        z = 0
    
    return np.degrees([x, y, z])
