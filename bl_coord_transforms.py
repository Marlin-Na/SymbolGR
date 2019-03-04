import numpy as np


def CartesianToBL_pos(pos_vec, a):
    pass


def CartesianToBL_vel(pos_vec, vel_vec, a):
    pass


def BLToCartesian_pos(pos_vec, a):
    """
    Function to convert Boyer-Lindquist coordinates to Cartesian coordinates

    Parameters
    ----------
    pos_vec : ~numpy.array
        3-length numpy array having r, theta, phi coordinates in SI units(m, rad, rad)
    a : float
        Any constant

    Returns
    -------
    ~numpy.array
        3-length numpy array with x, y, z in m.

    """
    r_vec = np.zeros(shape=(3,), dtype=float)
    tmp = np.sqrt(pos_vec[0] ** 2 + a ** 2) * np.sin(pos_vec[1])
    r_vec[0] = tmp * np.cos(pos_vec[2])
    r_vec[1] = tmp * np.sin(pos_vec[2])
    r_vec[2] = pos_vec[0] * np.cos(pos_vec[1])
    return r_vec


def BLToCartesian_vel(pos_vec, vel_vec, a):
    """
    Function to convert velocities in Boyer-Lindquist coordinates to velocities in Cartesian coordinates

    Parameters
    ----------
    pos_vec : ~numpy.array
        3-length numpy array having r, theta, phi coordinates in SI units(m, rad, rad)
    vel_vec : ~numpy.array
        3-length numpy array with V_r, V_theta, V_phi (m/s, rad/s, rad/s)
    a : float
        Any constant

    Returns
    -------
    ~numpy.array
        3-length numpy array having vx, vy, vz in SI units(m/s)

    """
    v_vec = np.zeros(shape=(3,), dtype=float)
    tmp = np.sqrt(pos_vec[0] ** 2 + a ** 2)
    v_vec[0] = (
        (pos_vec[0] * vel_vec[0] * np.sin(pos_vec[1]) * np.cos(pos_vec[2]) / tmp)
        + (tmp * np.cos(pos_vec[1]) * np.cos(pos_vec[2]) * vel_vec[1])
        - (tmp * np.sin(pos_vec[1]) * np.sin(pos_vec[2]) * vel_vec[2])
    )
    v_vec[1] = (
        (pos_vec[0] * vel_vec[0] * np.sin(pos_vec[1]) * np.sin(pos_vec[2]) / tmp)
        + (tmp * np.cos(pos_vec[1]) * np.sin(pos_vec[2]) * vel_vec[1])
        + (tmp * np.sin(pos_vec[1]) * np.cos(pos_vec[2]) * vel_vec[2])
    )
    v_vec[2] = (vel_vec[0] * np.cos(pos_vec[1])) - (
        pos_vec[0] * np.sin(pos_vec[1]) * vel_vec[1]
    )
    return v_vec
