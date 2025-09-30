from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from matrix3d.transformations import *

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # React default port
    "http://127.0.0.1:3000",  # React default port (alternative)
    "http://localhost:5173",  # Vite default port
    "http://127.0.0.1:5173",  # Vite default port (alternative)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatrixRequest(BaseModel):
    matrix: list

class TransformRequest(MatrixRequest):
    x: float = 0
    y: float = 0
    z: float = 0
    angle: float = 0  # in degrees

@app.get("/")
async def root():
    return {"message": "3D Matrix Manipulation API is running"}

@app.post("/create_identity")
async def create_identity():
    """Create a 4x4 identity matrix"""
    matrix = np.eye(4).tolist()
    return {"matrix": matrix}

@app.post("/translate")
async def translate(request: TransformRequest):
    """Apply translation to a matrix"""
    try:
        matrix = np.array(request.matrix)
        translation = translation_matrix([request.x, request.y, request.z])
        result = np.dot(translation, matrix)
        return {"matrix": result.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rotate_x")
async def rotate_x(request: TransformRequest):
    """Rotate around X axis"""
    try:
        matrix = np.array(request.matrix)
        rotation = rotation_matrix(np.radians(request.angle), [1, 0, 0])
        result = np.dot(rotation, matrix)
        return {"matrix": result.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rotate_y")
async def rotate_y(request: TransformRequest):
    """Rotate around Y axis"""
    try:
        matrix = np.array(request.matrix)
        rotation = rotation_matrix(np.radians(request.angle), [0, 1, 0])
        result = np.dot(rotation, matrix)
        return {"matrix": result.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rotate_z")
async def rotate_z(request: TransformRequest):
    """Rotate around Z axis"""
    try:
        matrix = np.array(request.matrix)
        rotation = rotation_matrix(np.radians(request.angle), [0, 0, 1])
        result = np.dot(rotation, matrix)
        return {"matrix": result.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/scale")
async def scale(request: TransformRequest):
    """Apply scaling to a matrix"""
    try:
        matrix = np.array(request.matrix)
        scale_mat = scaling_matrix([request.x, request.y, request.z])
        result = np.dot(scale_mat, matrix)
        return {"matrix": result.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
