import numpy as np

from distort_points import distort_points


def project_points(points_3d: np.ndarray,
                   K: np.ndarray,
                   D: np.ndarray) -> np.ndarray:
    """
    Projects 3d points to the image plane, given the camera matrix,
    and distortion coefficients.

    Args:
        points_3d: 3d points (3xN)
        K: camera matrix (3x3)
        D: distortion coefficients (4x1)

    Returns:
        projected_points: 2d points (2xN)
    """

    # [TODO] get image coordinates
    if points_3d.shape[1] != 3:
        raise ValueError("points_3d should have shape (Nx3)")

    # Extract intrinsic camera matrix parameters
    fx, fy = K[0, 0], K[1, 1]  # Focal lengths
    cx, cy = K[0, 2], K[1, 2]  # Principal point coordinates

    # Normalize 3D points to camera coordinates
    x = points_3d[:, 0] / points_3d[:, 2]
    y = points_3d[:, 1] / points_3d[:, 2]

    # Distort normalized coordinates
    normalized_points = np.stack([x, y], axis=1)  # Shape: (Nx2)
    distorted_points = distort_points(normalized_points, D, K)

    # Apply intrinsic camera parameters to get image coordinates
    u = fx * distorted_points[:, 0] + cx
    v = fy * distorted_points[:, 1] + cy

    # Stack into (Nx2) array
    projected_points = np.stack([u, v], axis=1)

    # [TODO] apply distortion


    return projected_points
