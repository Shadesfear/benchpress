#!/usr/bin/env python
#
#
# (source, token, regex, converter)
#
# The result-file has three sources: "output", "time", and "perf".
# They contain the plain-text output from the standard output
# when running the benchmark, the output from /usr/bin/time and
# the output of the perf-tool with as many counters as possible.
#
# Tokens include elapsed, utime, stime, wtime, etc.
#
# The regex in the expression that will search through the source.
#
# Converter is any function x -> x. Useful for converting to
# floats etc.
#
import pprint
import json
import sys
import os
import re

tokens = [
    ('stdout',  'elapsed', 'elapsed-time: ([\d.]+)', float),
    ('stdout',  'bytes_missed', "bytes_missed:.?'(\d+)'", int),
    ('stdout',  'bytes_reused', "bytes_reused:.?'(\d+)'", int),
    ('time',    'utime', "User\stime\s\(seconds\):\s([\d.]+)", float),
    ('time',    'stime', "System\stime\s\(seconds\):\s([\d.]+)", float),
    ('time',    'resident_kb', "Maximum\sresident\sset\ssize\s\(kbytes\):\s(\d+)", int),
]

def avg(elapsed):
    return sum(elapsed)/float(len(elapsed))

def variance(elapsed):
    count = len(elapsed)
    if (count<2):
        return 0.0

    acc     = sum(elapsed)
    acc_2   = acc*acc
    acc_2d  = acc_2/count
    acc_s   = sum([x*x for x in elapsed])
    diff    = (acc_s - acc_2d)/(count-1)

    return diff

def from_str(results, wc=False):
    results = json.loads(results)['runs']
    res = []
    for run in results:
        data = {}                   # Grab the tokens
        for source, token, regex, conv in tokens:
            if source not in run:   # Source is not available
                continue
            if token not in data:   # First entry for this token
                data[token] = []

            topic = ''.join(run[source])
            matches = re.finditer(regex, topic)
            for m in matches:       # Remaining entries
                data[token].append(conv(m.group(1)))

                                    # Legacy mode...
        if 'elapsed' not in data and 'elapsed' in run:
            data['elapsed'] = run['elapsed']

        data['sizes'] = []          # Parse the --size parameter
        sizes = [cmd for cmd in run['cmd'] if '--size=' in cmd]
        if sizes:
            data['sizes'] =[int(size) for size in sizes[0][len('--size='):].split('*')]

        res.append((
            run['script_alias'],
            run['bridge_alias'],
            run['manager_alias'],
            run['engine_alias'],
            data
        ))
    return sorted(res)


def from_file(results_fn):
    """Parses a result-file into something slightly more useful."""

    return from_str(open(results_fn).read())
