#
# This file is part of cphVB and copyright (c) 2012 the cphVB team:
# http://cphvb.bitbucket.org
#
# cphVB is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 
# of the License, or (at your option) any later version.
# 
# cphVB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the 
# GNU Lesser General Public License along with cphVB. 
#
# If not, see <http://www.gnu.org/licenses/>.
#

#
# Modify the lines below to reflect the local environment. 
#
MACHINE="unknown"
BUILD_ROOT="~/buildbot"
BENCH_SRC="$ROOT/benchpress"
CPHVB_SRC="$ROOT/cphvb"
CPHVB_LIB="$ROOT/cphvb.lib"

#
# STOP: Do not modify anything below unless you want to change the functionality of the build-n-test script.
#
cd $BUILD_ROOT

OLDPP=$PYTHONPATH
OLDLD=$LD_LIBRARY_PATH
PYTHONVER=`python -c 'import sys; (major,minor, _,_,_) = sys.version_info; print "%d.%d" % (major, minor)'`

#
#   GRAB THE LATEST AND GREATEST
#
if [ "$1" == "FULL" ]       # Remove previous source-code and libraries.
then                        # and then clone the most recent.
    echo "Cleaning repo: $1"
    cd $BUILD_ROOT
    rm -rf $CPHVB_LIB
    rm -rf $CPHVB_SRC
    rm -rf $BENCH_SRC
    git clone git@bitbucket.org:cphvb/cphvb.git $CPHVB_SRC
    git clone git@bitbucket.org:cphvb/benchpress.git $BENCH_SRC
    mkdir $CPHVB_LIB
    cd $CPHVB_SRC
    git submodule init
fi

echo "** Pulling benchmark-updates"
cd $BENCH_SRC
git pull

echo "** Pulling cphvb-updates"
cd $CPHVB_SRC
git pull
git submodule update

REV=`git log -pretty-format:%H -n 1`

#
#   BUILD AND INSTALL
#
echo "** Rebuilding cphVB"
python build.py rebuild

echo "** Installing cphVB"
python build.py install --prefix="$CPHVB_LIB"

echo "** Testing cphVB installation."

export PYTHONPATH="$PYTHONPATH:$CPHVB_LIB/lib/python$PYTHONVER/site-packages"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$CPHVB_LIB"
python $CPHVB_SRC/test/numpy/numpytest.py

#
#   BENCHMARK-SUITE
#
echo "** Running benchmarks"
mkdir -p $BENCH_SRC/results/$MACHINE/$REV
python press.py $CPHVB_SRC --output $BENCH_SRC/results/$MACHINE/$REV > $BENCH_SRC/$MACHINE.log
cd $BENCH_SRC/results/$MACHINE/$REV
BENCHFILE=`ls -t1 benchmark-* | head -n1`

#
#   GRAPHS
#
echo "** Generating diagrams from $BENCH_SRC/results/$MACHINE/$REV/$BENCHFILE"
export PYTHONPATH=$OLDPP
export LD_LIBRARY_PATH=$OLDLD

mkdir -p $BENCH_SRC/graphs/$MACHINE/$REV
python "$BENCH_SRC/gen.diagrams.py" "$BENCH_SRC/results/$MACHINE/$REV/$BENCHFILE" --output "$BENCH_SRC/graphs/$MACHINE/$REV"

#
#   Commit & Push
#
cd $BENCH_SRC
git add $MACHINE.log
git add results/$MACHINE/$REV/$BENCHFILE
git add graphs/$MACHINE/$REV/*
git commit -m "Daily update from $MACHINE."
git push -u origin master
