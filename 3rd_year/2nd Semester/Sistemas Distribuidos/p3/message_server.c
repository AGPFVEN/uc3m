/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */
#include<stdlib.h>

#include "message.h"
#include "lib.h"

bool_t
d_init_1_svc(int *result, struct svc_req *rqstp)
{
	*result = init();

	return 1;
}

bool_t
d_set_value_1_svc(int key, char *value1, int N_value2, t_vector V_value2, int *result,  struct svc_req *rqstp)
{
	double *V_value2_array = (double *)	malloc(V_value2.t_vector_len * sizeof(double));

	for (int i = 0; i < N_value2; i++){
		V_value2_array[i] = V_value2.t_vector_val[i];
	}

	printf("%f\n", V_value2_array[1]);

	set_value(key, value1, N_value2, V_value2_array);

	return 1;
}

bool_t
d_get_value_1_svc(int key, char *value1, int N_value2, t_vector V_value2, get_res *result,  struct svc_req *rqstp)
{
	int *n2;
	double *v2;
	n2 = (int *) malloc(sizeof(int));
	v2 = (double *) malloc (32 * sizeof(double));

	get_value(key, result->value1, n2, v2);


	result->N_value2 = V_value2.t_vector_len = *n2;
	result->V_value2.t_vector_val = (double *) malloc(*n2 * sizeof(double));
	for (int i = 0; i < N_value2; i++){
		result->V_value2.t_vector_val[i] = v2[i];
	}

	return 1;
}

bool_t
d_modify_value_1_svc(int key, char *value1, int N_value2, t_vector V_value2, int *result,  struct svc_req *rqstp)
{
	bool_t retval;

	/*
	 * insert server code here
	 */

	return retval;
}

bool_t
d_delete_key_1_svc(int key, int *result,  struct svc_req *rqstp)
{
	bool_t retval;

	/*
	 * insert server code here
	 */

	return retval;
}

bool_t
d_exist_1_svc(int key, int *result,  struct svc_req *rqstp)
{
	bool_t retval;

	/*
	 * insert server code here
	 */

	return retval;
}

int
ejercicio3_1_freeresult (SVCXPRT *transp, xdrproc_t xdr_result, caddr_t result)
{
	xdr_free (xdr_result, result);

	/*
	 * Insert additional freeing code here, if needed
	 */

	return 1;
}
