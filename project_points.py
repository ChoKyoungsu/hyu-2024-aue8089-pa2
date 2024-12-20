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


    fx, fy = K[0, 0], K[1, 1]  # Focal lengths
    cx, cy = K[0, 2], K[1, 2]  # Principal point coordinates


    x = points_3d[:, 0] / points_3d[:, 2]
    y = points_3d[:, 1] / points_3d[:, 2]


    normalized_points = np.stack([x, y], axis=1)  # Shape: (Nx2)

    u = fx * normalized_points[:, 0] + cx
    v = fy * normalized_points[:, 1] + cy

    projected_points = np.stack([u, v], axis=1)

    # [TODO] apply distortion

    projected_points = distort_points(projected_points, D, K)

    return projected_points
