
/*
 *  Copyright 2020-2024 Felix Garcia Carballeira, Alejandro Calderon Mateos,
 *
 *  This file is part of nanodt proyect.
 *
 *  nanodt is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU Lesser General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  nanodt is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public License
 *  along with nanodt.  If not, see <http://www.gnu.org/licenses/>.
 *
 */


#include <stdio.h>
#include <stdlib.h>
#include "lib-client.h"


int   N = 10 ;
char *A = "nombre" ;


int main ( int argc, char *argv[] )
{
    int ret ;

    // init
    ret = d_init() ;
    if (ret < 0) {
        printf("d_init: error code %d\n", ret) ;
        exit(-1) ;
    }

    //set_value
    double *t;
    int size = 3;
    t = (double *) malloc(sizeof(double) * size);
    for (int i = 1; i < size; i++){
        t[i] = i * 5;
    }

    char *op = "ijijijijijo";
    ret = d_set_value(5, op, size, t);
    if (ret < 0) {
        printf("d_set_value: error code %d\n", ret) ;
        exit(-1) ;
    }

    char *pp;
    double *p;
    pp = (char *) malloc(sizeof(char) * 12);
    p = (double *) malloc(sizeof(double) * 3);

    ret = d_get_value(5, pp, 3, p);
    printf("%s\n", pp);
    printf("%f\n", p[1]);

    //set_value
    char *up = "cambiando";
    double *ki;
    size = 5;
    ki = (double *) malloc(sizeof(double) * size);
    for (int i = 1; i < size; i++){
        ki[i] = i * 9;
    }
    ret = d_modify_value(5, up, size, ki);
    ret = d_exist(5);
    ret = d_delete_key(5);
    ret = d_exist(5);
    ret = d_delete_key(5);

    /*int val ;
    for (int i=0; i<N; i++)
    {
	    // set
	    ret = d_set (A, 100+i, i) ;
	    if (ret < 0) {
		printf("d_set: error code %d\n", ret) ;
		exit(-1) ;
	    }
	    printf("set(\"%s\", %d, 0x%x)\n", A, 100+i, i) ;
    }
    
    for (int i=0; i<N; i++)
    {
	    // get
	    ret = d_get (A, 100+i, &val) ;
	    if (ret < 0) {
		printf("d_get: error code %d\n", ret) ;
		exit(-1) ;
	    }
	    printf("get(\"%s\", %d) -> 0x%x\n", A, 100+i, val) ;
    }*/

    return 0 ;
}

