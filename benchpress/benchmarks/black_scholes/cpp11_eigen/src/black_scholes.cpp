/*
This file is part of Bohrium and Copyright (c) 2012 the Bohrium team:
http://bohrium.bitbucket.org

Bohrium is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 
of the License, or (at your option) any later version.

Bohrium is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the 
GNU Lesser General Public License along with bohrium. 

If not, see <http://www.gnu.org/licenses/>.
*/
#include <iostream>
#include <Eigen/Dense>
#include <bp_util.h>

using namespace std;
using namespace Eigen;

template <typename T>
Array<T, Dynamic, 1>& cnd(const Array<T, Dynamic, 1>& x)
{
    size_t samples = x.size();
    Array<T, Dynamic, 1> l(samples), k(samples), w(samples);
    Array<T, Dynamic, 1> mask(samples);
    Array<bool, Dynamic, 1> mask_bool(samples);

    T a1 = 0.31938153,
      a2 =-0.356563782,
      a3 = 1.781477937,
      a4 =-1.821255978,
      a5 = 1.330274429,
      pp = 2.5066282746310002; // sqrt(2.0*PI)

    l = abs(x);
    //k = (T)1.0 / ((T)1.0 + (T)0.2316419 * l);
    //k = (T)0.5 / l / (T)0.5;
    k = l / (T)0.5;
    w = (T)1.0 - (T)1.0 / (T)pp * exp((T)-(T)1.0*l*l/(T)2.0) * \
        ((T)a1*k + \
         (T)a2*(pow(k,(T)2)) + \
         (T)a3*(pow(k,(T)3)) + \
         (T)a4*(pow(k,(T)4)) + \
         (T)a5*(pow(k,(T)5)));

    mask_bool= (x < (T)0.0);
    mask = mask_bool.cast<T>();
    return w * (mask) + ((T)1.0-w);
    //return w * (mask) + ((T)1.0-w)* mask;
    //return w * (!mask) + (1.0-w)* mask;
}

template <typename T>
T* pricing(size_t samples, size_t iterations, char flag, T x, T d_t, T r, T v)
{
    T* p    = (T*)malloc(sizeof(T)*samples);    // Intermediate results
    T t     = d_t;                              // Initial delta

    Array<T, Dynamic, 1> d1(samples), d2(samples), res(samples);
    Array<T, Dynamic, 1> s = Array<T, Dynamic, 1>::Random(samples)*4.0 +58.0;      // Model between 58-62

    for(size_t i=0; i<iterations; i++) {
        d1 = (log(s/x) + (r+v*v/2.0)*t) / (v*sqrt(t));
        d2 = d1-v*sqrt(t);

        if (flag == 'c') {

            size_t samples = x.size();
            Array<T, Dynamic, 1> l(samples), k(samples), w(samples);
            Array<T, Dynamic, 1> mask(samples);
            Array<bool, Dynamic, 1> mask_bool(samples);

            T a1 = 0.31938153,
              a2 =-0.356563782,
              a3 = 1.781477937,
              a4 =-1.821255978,
              a5 = 1.330274429,
              pp = 2.5066282746310002; // sqrt(2.0*PI)

            l = abs(x);
            //k = (T)1.0 / ((T)1.0 + (T)0.2316419 * l);
            //k = (T)0.5 / l / (T)0.5;
            k = l / (T)0.5;
            w = (T)1.0 - (T)1.0 / (T)pp * exp((T)-(T)1.0*l*l/(T)2.0) * \
                ((T)a1*k + \
                 (T)a2*(pow(k,(T)2)) + \
                 (T)a3*(pow(k,(T)3)) + \
                 (T)a4*(pow(k,(T)4)) + \
                 (T)a5*(pow(k,(T)5)));

            mask_bool= (x < (T)0.0);
            mask = mask_bool.cast<T>();
            res =  w * (!mask) + (1.0-w)* mask;

            //cnd<T>(d1);
            //res = s * cnd<T>(d1) -x * exp(-r*t) * cnd<T>(d2);
        } else {
/*
            Array<T, Dynamic, 1> tmp1(samples), tmp2(samples);
            tmp1 = -1.0*d2;
            tmp2 = -1.0*d1;
            res = x * exp(-r*t) * cnd<T>(tmp1) - s*cnd<T>(tmp2);
    */
        }

        t += d_t;                               // Increment delta
        p[i] = res.sum() / (T)samples;           // Result from timestep
    }

    return p;
}

int main(int argc, char* argv[])
{
    bp_util_type bp = bp_util_create(argc, argv, 2);    // Grab arguments
    if (bp.args.has_error) {
        return 1;
    }
    const size_t samples    = bp.args.sizes[0];
    const size_t iterations = bp.args.sizes[1];

    bp.timer_start();                                   // Start timer
    double* prices = pricing(                           // Run...
        samples, iterations,
        'c', 65.0, 1.0 / 365.0,
        0.08, 0.3
    );
    bp.timer_stop();                                    // Stop timer
    
    bp.print("black_scholes(cpp11_bxx)");               // Print restults..
    if (bp.args.verbose) {                              // ..verbosely.
        cout << ", \"output\": [";
        for(size_t i=0; i<iterations; i++) {
            cout << prices[i];
            if (iterations-1!=i) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    free(prices);                                       // Cleanup

    return 0;
}

