managers = [('proxy', 'proxy', '{bridge}', None)]

engines = [\
           ('sleep    0ms', 'cpu',  {'BH_VEM_PROXY_SLEEP':0}),
           ('sleep   10ms', 'cpu',  {'BH_VEM_PROXY_SLEEP':10}),
           ('sleep  100ms', 'cpu',  {'BH_VEM_PROXY_SLEEP':100}),
           ('sleep  200ms', 'cpu',  {'BH_VEM_PROXY_SLEEP':200}),
           ('sleep  500ms', 'cpu',  {'BH_VEM_PROXY_SLEEP':500}),
           ('sleep 1000ms', 'cpu',  {'BH_VEM_PROXY_SLEEP':1000}),
]

python_script = [\
    		 ('N-body  5k',        'nbody',          '--size=5000*10'),
    		 ('N-body 10k',        'nbody',          '--size=10000*10'),
    		 ('N-body 15k',        'nbody',          '--size=15000*10'),
    		 ('Heat Equation  5k', 'heat_equation',  '--size=5000*5000*10'),
    		 ('Heat Equation 10k', 'heat_equation',  '--size=10000*10000*10'),
    		 ('Heat Equation 20k', 'heat_equation',  '--size=20000*20000*10'),
                 ('Shallow Water  5k', 'shallow_water',  '--size=5000*5000*10'),
                 ('Shallow Water 10k', 'shallow_water',  '--size=10000*10000*10'),
                 ('Shallow Water 20k', 'shallow_water',  '--size=20000*20000*10'),
                 ('Black Scholes  10m', 'black_scholes',  '--size=10000000*10'),
                 ('Black Scholes 100m', 'black_scholes',  '--size=100000000*10'),
]

python = {
    'bridges': [('numpy', 'python benchmark/Python/{script}.py {args} --bohrium=True', None)],
    'managers': managers,
    'engines': engines,
    'scripts': python_script
}

suites = [python]

