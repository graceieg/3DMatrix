# 3D Matrix Manipulation

A full-stack application for 3D matrix transformations with a React frontend and Python FastAPI backend. This application allows you to perform various 3D transformations (translation, rotation, scaling) on 3D objects with real-time visualization.

## Features

### Backend (Python/FastAPI)
- RESTful API for matrix operations
- Support for 3D transformations (translate, rotate, scale)
- Interactive API documentation with Swagger UI

### Frontend (React/TypeScript)
- Interactive 3D viewport
- Real-time matrix manipulation
- Intuitive controls for transformations
- Responsive design

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## Getting Started

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/3d-matrix-manipulation.git
   cd 3d-matrix-manipulation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend server:
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd "3D Matrix Manipulation Frontend"
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000`

## Project Structure

```
3DMatrix/
├── 3D Matrix Manipulation Frontend/  # Frontend React application
│   ├── public/                       # Static files
│   ├── src/                          # Source files
│   │   ├── api/                      # API client
│   │   ├── components/               # React components
│   │   └── ...
│   └── package.json                  # Frontend dependencies
├── matrix3d/                         # Core matrix manipulation library
├── examples/                         # Example scripts
├── app.py                            # FastAPI application
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## API Documentation

Once the backend is running, you can access the interactive API.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Features

### Backend (Python)
- **Matrix3D Class**: A comprehensive class for 3D transformations including:
  - Translation, rotation, and scaling
  - Matrix multiplication and inversion
  - Point and point cloud transformations

- **Transformations Module**: Utility functions for common 3D operations:
  - Look-at matrix generation
  - Perspective and orthographic projections
  - Euler angle conversions

- **RESTful API**:
  - FastAPI backend with CORS support
  - Endpoints for all matrix operations
  - Error handling and validation

### Frontend (React)
- Interactive 3D visualization
- Real-time matrix manipulation
- Intuitive UI controls for transformations
  - Interactive 3D visualization

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/3d-matrix.git
   cd 3d-matrix
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies for the frontend:
   ```bash
   cd "3D Matrix Manipulation Frontend"
   npm install
   ```

## Running the Application

### Start the Backend Server
From the project root directory:
```bash
uvicorn app:app --reload
```

### Start the Frontend
In a new terminal, navigate to the frontend directory and start the development server:
```bash
cd "3D Matrix Manipulation Frontend"
npm start
```

## API Endpoints

- `POST /create_identity` - Create a 4x4 identity matrix
- `POST /translate` - Apply translation to a matrix
- `POST /rotate_x` - Rotate around X axis
- `POST /rotate_y` - Rotate around Y axis
- `POST /rotate_z` - Rotate around Z axis
- `POST /scale` - Apply scaling to a matrix

## Development

### Backend
- The backend is built with FastAPI and Python 3.8+

### Frontend
- Built with React and TypeScript
- Uses Three.js for 3D rendering
- State management with React Context API

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Example

```python
from matrix3d.matrix3d import Matrix3D
from matrix3d.visualization import plot_3d_points
import matplotlib.pyplot as plt

# Create a 3D point
point = np.array([1, 0, 0])

# Create transformation matrices
rotation = Matrix3D.rotation_y(45)  # 45 degrees around Y-axis
translation = Matrix3D.translation(2, 1, 0)

# Combine transformations (translate then rotate)
transform = rotation @ translation

# Apply transformation
transformed_point = transform.transform_point(point)

# Plot the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_3d_points(np.array([point, transformed_point]), ax=ax)
plt.show()
```

### Running the Examples

The `examples/` directory contains demonstration scripts:

```bash
# Run the transformations demo
python examples/transformations_demo.py
```

## Documentation

### Matrix3D Class

- `Matrix3D(matrix=None)`: Initialize with a 4x4 numpy array or create an identity matrix.
- `identity()`: Return an identity matrix.
- `translation(x, y, z)`: Create a translation matrix.
- `scale(x, y, z)`: Create a scaling matrix.
- `rotation_x/y/z(angle_degrees)`: Create rotation matrices around each axis.
- `transform_point(point)`: Transform a single 3D point.
- `transform_points(points)`: Transform multiple 3D points.
- `inverse()`: Return the inverse of the matrix.

### Transformations Module

- `look_at(eye, target, up)`: Create a view matrix looking from eye to target.
- `perspective(fov, aspect, near, far)`: Create a perspective projection matrix.
- `orthographic(left, right, bottom, top, near, far)`: Create an orthographic projection matrix.
- `euler_angles_to_matrix(angles, order)`: Convert Euler angles to a rotation matrix.
- `matrix_to_euler_angles(matrix)`: Convert a rotation matrix to Euler angles.

### Visualization Module

- `plot_3d_points(points, ax, color, marker, label)`: Plot 3D points.
- `plot_3d_mesh(vertices, faces, ax, color, alpha, edgecolor)`: Plot a 3D mesh.
- `plot_coordinate_frame(ax, transform, length)`: Plot a 3D coordinate frame.
- `create_cube(size)`: Generate vertices and faces for a cube.
- `create_sphere(radius, resolution)`: Generate vertices and faces for a sphere.

## Examples

See the `examples/` directory for more comprehensive examples:

1. `transformations_demo.py`: Demonstrates various 3D transformations and visualizations.

## Dependencies

- Python 3.7+
- NumPy
- Matplotlib
- SciPy (for some advanced operations)
- PyOpenGL (for future 3D rendering features)
- PyQt5 (for future GUI applications)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



