// API Configuration
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

if (!API_BASE_URL) {
  console.warn('VITE_API_BASE_URL is not set. Using default URL:', API_BASE_URL);
}

// Types
export interface Matrix4x4 {
  matrix: number[][];
}

interface TransformRequest {
  matrix: number[][];
  x?: number;
  y?: number;
  z?: number;
  angle?: number;
}

// Helper function to handle API requests
async function apiRequest<T>(endpoint: string, method: string = 'GET', data?: any): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method,
    headers: {
      'Content-Type': 'application/json',
    },
    body: data ? JSON.stringify(data) : undefined,
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'An error occurred');
  }

  return response.json();
}

// Matrix Operations
export async function createIdentityMatrix(): Promise<Matrix4x4> {
  return apiRequest<Matrix4x4>('/create_identity', 'POST');
}

export async function translateMatrix(matrix: number[][], x: number, y: number, z: number): Promise<Matrix4x4> {
  return apiRequest<Matrix4x4>('/translate', 'POST', { matrix, x, y, z });
}

export async function rotateX(matrix: number[][], angle: number): Promise<Matrix4x4> {
  return apiRequest<Matrix4x4>('/rotate_x', 'POST', { matrix, angle });
}

export async function rotateY(matrix: number[][], angle: number): Promise<Matrix4x4> {
  return apiRequest<Matrix4x4>('/rotate_y', 'POST', { matrix, angle });
}

export async function rotateZ(matrix: number[][], angle: number): Promise<Matrix4x4> {
  return apiRequest<Matrix4x4>('/rotate_z', 'POST', { matrix, angle });
}

export async function scaleMatrix(matrix: number[][], x: number, y: number, z: number): Promise<Matrix4x4> {
  return apiRequest<Matrix4x4>('/scale', 'POST', { matrix, x, y, z });
}
