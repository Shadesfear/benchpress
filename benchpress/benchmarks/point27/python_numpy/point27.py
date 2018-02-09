from __future__ import print_function
from benchpress import util
import numpy as np
from bohrium.stdviews import no_border, D3P27

def point27_init(size):
    """TODO: Describe the data generated by this function."""

    data = np.zeros((size,size,size))
    mid = size//2
    data[mid-8:mid+8, mid-8:mid+8] = 100.0

    return data

def point27(data, iterations):
    """TODO: Describe the benchmark."""

    active  = no_border(data, 1)
    stencil = D3P27(data)
    for _ in range(iterations):
        active[:] = sum(stencil)/27.0
        util.Benchmark().flush()

    return active

def main():
    """
    Example parameter: --size=400*10.
    This will execute on a 400x400x400 dataset for 10 iterations.
    """
    B = util.Benchmark()        # Benchmark setup
    (N, I) = B.size
    data = point27_init(N)

    B.start()                   # Benchmark run, timing, pprint
    R = point27(data, I)
    B.stop()
    B.pprint()

    if B.outputfn:
        B.tofile(B.outputfn, {'res': R})

if __name__ == "__main__":
    main()
