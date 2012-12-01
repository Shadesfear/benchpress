from default import scripts, engines
import pprint

pp = pprint.PrettyPrinter()

engines = [
    ('numpy',   None,       None),
    ('naive',   'naive',    None),
    ('score',   'score',    None),
    ('simple',  'simple',   None),
    ('tile',    'tile',     None),
    ('mcore',   'mcore',    None),
    ('jitbatchcacheon',  'jit',      {"CPHVB_JIT_DIRECTEXECUTE":"False","CPHVB_JIT_CACHE_ENABLED":"True"}),
    ('jitbatchcacheoff', 'jit',      {"CPHVB_JIT_DIRECTEXECUTE":"False","CPHVB_JIT_CACHE_ENABLED":"False"}),
    ('jitexprcacheon',   'jit',      {"CPHVB_JIT_DIRECTEXECUTE":"True","CPHVB_JIT_CACHE_ENABLED":"True"}),
    ('jitexprcacheoff',  'jit',      {"CPHVB_JIT_DIRECTEXECUTE":"True","CPHVB_JIT_CACHE_ENABLED":"False"}),    
    ('gpu',     'gpu',      None),
]


x=4000
y=4000
jacobi_iterative_script = []
for i in xrange(1,10):
    jacobi_iterative_script.append( ('Jacobi Iterative - Reduce {0}'.format(i),   'jacobi.iterative.reduc.py','--size={0}*{1}*{2}'.format(x,y,i) ))
for i in xrange(1,11):
    jacobi_iterative_script.append( ('Jacobi Iterative - Reduce {0}'.format(i*10),   'jacobi.iterative.reduc.py','--size={0}*{1}*{2}'.format(x,y,i*10) ))
jacobi_iterative_script.append( ('Jacobi Iterative - Reduce {0}'.format(200),   'jacobi.iterative.reduc.py','--size={0}*{1}*{2}'.format(x,y,200) ))

jacobi_iterative_script_naive = []
for i in xrange(1,10):
    jacobi_iterative_script_naive.append( ('Jacobi Iterative - Reduce Naive {0}'.format(i),   'jacobi.iterative.reduce.oneline.py','--size={0}*{1}*{2}'.format(x,y,i) ))
for i in xrange(1,11):
    jacobi_iterative_script_naive.append( ('Jacobi Iterative - Reduce Naive {0}'.format(i*10),   'jacobi.iterative.reduce.oneline.py','--size={0}*{1}*{2}'.format(x,y,i*10) ))
jacobi_iterative_script_naive.append( ('Jacobi Iterative - Reduce Naive {0}'.format(200),   'jacobi.iterative.reduce.oneline.py','--size={0}*{1}*{2}'.format(x,y,200) ))

jacobi_fixed = []
jacobi_fixed.append( ('Jacobi Iterative - {0}'.format(1),   'jacobi.iterative.py','--size={0}*{1}*{2}'.format(x,y,1) ))
for i in xrange(1,11):
    jacobi_fixed.append( ('Jacobi Iterative - {0}'.format(i*10),   'jacobi.iterative.py','--size={0}*{1}*{2}'.format(x,y,i*10) ))


temp_remove_effect = []
#~ temp_remove_effect.append( ('Jacobi Iterative optimized- {0}'.format(10),   'jacobi.iterative.py','--size={0}*{1}*{2}'.format(x,y,10) ))
for i in xrange(1,11):
    temp_remove_effect.append( ('Jacobi Iterative optimized- {0}'.format(i*10),   'jacobi.iterative.py','--size={0}*{1}*{2}'.format(x,y,i*10) ))
#~ temp_remove_effect.append( ('Jacobi Iterative regular - {0}'.format(10),   'jacobi.iterative.oneline.py','--size={0}*{1}*{2}'.format(x,y,10) ))
for i in xrange(1,11):
    temp_remove_effect.append( ('Jacobi Iterative regular - {0}'.format(i*10),   'jacobi.iterative.oneline.py','--size={0}*{1}*{2}'.format(x,y,i*10) ))



#shallow water tests
sw_data_range = []
for i in xrange(1,6):
    sw_data_range.append( ('Shallow water.flush - {0}'.format(i*10),   'swater.flushing.py','--size={0}*{1}'.format(2000,i*10) ))

sw_iterate
for i in xrange(1,6):

# Scripts and their arguments
# (alias, script, parameters)
scripts   = [
    #('Cache Synth',     'cache.py',     '--size=10500000*10*1'),
    #('Lattice Boltzmann 2D', 'lbm.2d.py', '--size=15*200000*2'),
    #('Lattice Boltzmann 3D', 'lbm.3d.py', '--size=100*100*100*2'),
    # This one seems to be broken
    #('LU Factorization', 'lu.py', '--size=5000*10'),


    #~ # tests
    #~ ('Black Scholes',   'bscholes.py',  '--size=2000000*4'),
    #~ ('Jacobi Iterative',            'jacobi.iterative.py',          '--size=7000*7000*4'),
    #~ ('Jacobi Iterative - PS',       'jacobi.iterative.ps.py',       '--size=7000*7000*4'),     
    #~ ('Jacobi Iterative - Reduce',   'jacobi.iterative.reduc.py',    '--size=7000*7000*4'),
    #~ ('Jacobi Iterative - Reduce Naive',   'jacobi.iterative.reduce.oneline.py',    '--size=7000*7000*4'),
    #~ ('kNN',             'knn.py',       '--size=10000*120'),    
    #~ ('kNN - Naive',     'knn.naive.py', '--size=10000*120*10'),
    #~ ('Monte Carlo PI - RIL',    'mc.py',        '--size=10*1000000*10'),
    #~ ('Monte Carlo PI - 2xN',    'mc.2byN.py',   '--size=10*1000000*10'),
    #~ ('Monte Carlo PI - Nx2',    'mc.Nby2.py',   '--size=10*1000000*10'),
    #~ ('N-Body',  'nbody.py', '--size=2500*10'),
    #~ ('Stencil - 1D 4way',       'stencil.simplest.py',  '--size=100000000*1'),
    #~ ('Stencil - 2D',            'stencil.2d.py',        '--size=10000*1000*10'),
    #~ ('Shallow Water',           'swater.py',            '--size=2200*1'),
    #~ 
    #~ #fun
    #~ ('Monte Carlo PI - RIL',    'mc.py',        '--size=10*1000000*10'),
    #~ ('kNN',             'knn.py',       '--size=10000*120'),    
    #~ ('N-Body',  'nbody.py', '--size=2500*10'),
    #~ ('Shallow Water',           'swater.py',            '--size=2200*1'),
    #~ ('Black Scholes',   'bscholes.py',  '--size=2000000*4'),
    #~ ('Jacobi Iterative - Reduce',   'jacobi.iterative.reduc.py',    '--size=7000*7000*4'),
    #~ ('Jacobi Iterative - Reduce Naive',   'jacobi.iterative.reduce.oneline.py',    '--size=7000*7000*4'),

    #test
    #~ ('Black Scholes',   'bscholes.py',  '--size=100*4'),
    #~ ('Jacobi Iterative',            'jacobi.iterative.py',          '--size=100*100*4'),
    #~ ('Jacobi Iterative - PS',       'jacobi.iterative.ps.py',       '--size=100*100*4'),     
    #~ ('Jacobi Iterative - Reduce',   'jacobi.iterative.reduc.py',    '--size=100*100*4'),
    #~ ('Jacobi Iterative - Reduce Naive',   'jacobi.iterative.reduce.oneline.py',    '--size=100*100*4'),
    #~ ('kNN',             'knn.py',       '--size=100*120'),    
    #~ ('kNN - Naive',     'knn.naive.py', '--size=100*120*10'),
    #~ ('Monte Carlo PI - RIL',    'mc.py',        '--size=10*100*10'),
    #~ ('Monte Carlo PI - 2xN',    'mc.2byN.py',   '--size=10*100*10'),
    #~ ('Monte Carlo PI - Nx2',    'mc.Nby2.py',   '--size=10*100*10'),
    #~ ('N-Body',  'nbody.py', '--size=2500*10'),
    #~ ('Stencil - 1D 4way',       'stencil.simplest.py',  '--size=100*1'),
    #~ ('Stencil - 2D',            'stencil.2d.py',        '--size=100*100*10'),
    #~ ('Shallow Water',           'swater.py',            '--size=100*1'),
    #~ ('Shallow Water with flush',           'swater.flushing.py',            '--size=100*1'),

]

suite = {

    # SW data test
    

    # temp removal testing
    #'scripts':  temp_remove_effect,
    #'engines':  [engines[1]] + [engines[8]]
    
    # big speedup test
    'scripts':  jacobi_iterative_script + jacobi_iterative_script_naive,
    'engines':  engines[0:4] + [engines[6]] + [engines[8]]

}

pp.pprint(suite)
