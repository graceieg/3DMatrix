"""
3D Matrix Module for Spatial Transformations

This module provides a Matrix3D class for handling 3D transformations,
including translations, rotations, and scaling operations.
"""
import numpy as np
from typing import Union, List, Tuple, Optional

class Matrix3D:
    def __init__(self, matrix: Optional[np.ndarray] = None):
        """Initialize a 3D transformation matrix.
        
        Args:
            matrix: Optional 4x4 numpy array representing the transformation matrix.
                   If None, creates an identity matrix.
        """
        if matrix is not None:
            if matrix.shape != (4, 4):
                raise ValueError("Matrix must be 4x4 for 3D transformations")
            self.matrix = matrix.astype(float)
        else:
            self.matrix = np.identity(4)
    
    @classmethod
    def identity(cls) -> 'Matrix3D':
        """Return an identity matrix."""
        return cls()
    
    @classmethod
    def translation(cls, x: float, y: float, z: float) -> 'Matrix3D':
        """Create a translation matrix."""
        mat = cls()
        mat.matrix[0, 3] = x
        mat.matrix[1, 3] = y
        mat.matrix[2, 3] = z
        return mat
    
    @classmethod
    def scale(cls, x: float, y: float, z: float) -> 'Matrix3D':
        """Create a scaling matrix."""
        mat = cls()
        mat.matrix[0, 0] = x
        mat.matrix[1, 1] = y
        mat.matrix[2, 2] = z
        return mat
    
    @classmethod
    def rotation_x(cls, angle_degrees: float) -> 'Matrix3D':
        """Create a rotation matrix around the X-axis."""
        rad = np.radians(angle_degrees)
        c, s = np.cos(rad), np.sin(rad)
        mat = cls()
        mat.matrix[1:3, 1:3] = [[c, -s], [s, c]]
        return mat
    
    @classmethod
    def rotation_y(cls, angle_degrees: float) -> 'Matrix3D':
        """Create a rotation matrix around the Y-axis."""
        rad = np.radians(angle_degrees)
        c, s = np.cos(rad), np.sin(rad)
        mat = cls()
        mat.matrix[0, 0] = c
        mat.matrix[0, 2] = s
        mat.matrix[2, 0] = -s
        mat.matrix[2, 2] = c
        return mat
    
    @classmethod
    def rotation_z(cls, angle_degrees: float) -> 'Matrix3D':
        """Create a rotation matrix around the Z-axis."""
        rad = np.radians(angle_degrees)
        c, s = np.cos(rad), np.sin(rad)
        mat = cls()
        mat.matrix[0:2, 0:2] = [[c, -s], [s, c]]
        return mat
    
    def __matmul__(self, other: 'Matrix3D') -> 'Matrix3D':
        """Matrix multiplication with another Matrix3D."""
        return Matrix3D(self.matrix @ other.matrix)
    
    def transform_point(self, point: np.ndarray) -> np.ndarray:
        """Transform a 3D point using this matrix."""
        if point.shape != (3,):
            raise ValueError("Point must be a 3D vector")
        
        # Convert to homogeneous coordinates
        homog = np.append(point, 1.0)
        transformed = self.matrix @ homog
        # Convert back to 3D
        return transformed[:3] / transformed[3] if transformed[3] != 1 else transformed[:3]
    
    def transform_points(self, points: np.ndarray) -> np.ndarray:
        """Transform multiple 3D points."""
        if points.shape[1] != 3:
            raise ValueError("Points must be an Nx3 array")
        
        # Convert to homogeneous coordinates
        homog = np.column_stack((points, np.ones(len(points))))
        transformed = (self.matrix @ homog.T).T
        # Convert back to 3D
        return transformed[:, :3] / transformed[:, 3:4]
    
    def inverse(self) -> 'Matrix3D':
        """Return the inverse of this matrix."""
        return Matrix3D(np.linalg.inv(self.matrix))
    
    def __repr__(self) -> str:
        return f"Matrix3D(\n{np.array_str(self.matrix, precision=4, suppress_small=True)}\n)"
