scripts   = [
    ('Jacobi Stencil',        'jacobi_stencil',        '--size=300*300*10'),
    ('Shallow Water',         'shallow_water',         '--size=200*200*10'),
    #    ('Heat Equation',         'heat_equation',         '--size=3000*3000*100'),
    #    ('N-Body',                'nbody',                 '--size=1000*100'),
    #    ('Wire World',            'wireworld',             '--size=100*100'),
    #    ('Monte Carlo Pi',        'mc',                    '--size=10000000*100'),
    #    ('Black Scholes',         'black_scholes',         '--size=1000000*100'),
    #    ('Lattice Boltzmann D2Q9','lattice_boltzmann_D2Q9','--size=1000*1000*10'),
    #    ('Gauss Elimination',     'gauss',                 '--size=1000'),
    #    ('Convolution 3D',        'convolve_3d',           '--size=100'),
    #    ('Matrix Multiplication', 'mxmul',                 '--size=1000'),
    #    ('LU Factorization',      'lu',                    '--size=1000'),
]

bohrium = {
    'bridges': [('Bohrium', 'python benchmark/python/{script}.py {args} --bohrium=True', None)],
    'engines': [\
                ('CPU_OMP1',  'cpu', {'OMP_NUM_THREADS': 1}),
                ('CPU_OMP32', 'cpu', {'OMP_NUM_THREADS': 32}),
                ('GPU', 'gpu', None)
               ],
    'scripts': scripts
}

numpy = {
    'bridges': [('NumPy', 'python benchmark/python/{script}.py {args} --bohrium=False', None)],
    'engines': [('CPU',   'cpu', None)],
    'scripts': scripts
}

suites = [numpy, bohrium]
