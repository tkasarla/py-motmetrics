"""
modified
Tejaswi Kasarla, 2018
"""
"""py-motmetrics - metrics for multiple object tracker (MOT) benchmarking.
Christoph Heindl, 2017
https://github.com/cheind/py-motmetrics
"""

import numpy as np

def delH(objs,hyps):
    """ Computes the difference of height between the object and hypothesis points

    Params
    ------
    objs: NxM array
        Object points of dim M in rows
    hyps: KxM array
        Hypothesis points of dim M in rows
    Kwargs
    ------
    None

    Returns
    ------
    H: NxK array
        Natrix containing difference of heights
    """
    objs = np.atleast_2d(objs).astype(float)
    hyps = np.atleast_2d(hyps).astype(float)

    if objs.size == 0 or hyps.size == 0:
        return np.empty((0,0))

    assert objs.shape[1] == 1
    assert hyps.shape[1] == 1

    H = np.empty((objs.shape[0], hyps.shape[0]))

    for o in range(objs.shape[0]):
        for h in range(hyps.shape[0]):
            print(objs[o])
            diff = objs[o] - hyps[h]
            H[o,h] = diff
    return H

def delW(objs,hyps):
    """ Computes the difference of height between the object and hypothesis points

    Params
    ------
    objs: NxM array
        Object points of dim M in rows
    hyps: KxM array
        Hypothesis points of dim M in rows
    Kwargs
    ------
    None

    Returns
    ------
    H: NxK array
        Natrix containing difference of heights
    """
    objs = np.atleast_2d(objs).astype(float)
    hyps = np.atleast_2d(hyps).astype(float)

    if objs.size == 0 or hyps.size == 0:
        return np.empty((0,0))

    assert objs.shape[1] == 1
    assert hyps.shape[1] == 1

    W = np.empty((objs.shape[0], hyps.shape[0]))

    for o in range(objs.shape[0]):
        for h in range(hyps.shape[0]):
            diff = objs[o] - hyps[h]
            W[o,h] = diff
    return W
