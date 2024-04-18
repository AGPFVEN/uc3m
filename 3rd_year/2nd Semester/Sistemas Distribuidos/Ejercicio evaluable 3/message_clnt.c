/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include <memory.h> /* for memset */
#include "message.h"

/* Default timeout can be changed using clnt_control() */
static struct timeval TIMEOUT = { 25, 0 };

enum clnt_stat 
d_init_1(int *clnt_res, CLIENT *clnt)
{
	 return (clnt_call (clnt, d_init, (xdrproc_t) xdr_void, (caddr_t) NULL,
		(xdrproc_t) xdr_int, (caddr_t) clnt_res,
		TIMEOUT));

}

enum clnt_stat 
d_set_value_1(int key, char *value1, int N_value2, double V_value2, int *clnt_res,  CLIENT *clnt)
{
	d_set_value_1_argument arg;
	arg.key = key;
	arg.value1 = value1;
	arg.N_value2 = N_value2;
	arg.V_value2 = V_value2;
	return (clnt_call (clnt, d_set_value, (xdrproc_t) xdr_d_set_value_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_int, (caddr_t) clnt_res,
		TIMEOUT));
}

enum clnt_stat 
d_get_value_1(int key, char *value1, int N_value2, double V_value2, get_res *clnt_res,  CLIENT *clnt)
{
	d_get_value_1_argument arg;
	arg.key = key;
	arg.value1 = value1;
	arg.N_value2 = N_value2;
	arg.V_value2 = V_value2;
	return (clnt_call (clnt, d_get_value, (xdrproc_t) xdr_d_get_value_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_get_res, (caddr_t) clnt_res,
		TIMEOUT));
}

enum clnt_stat 
d_modify_value_1(int key, char *value1, int N_value2, double V_value2, int *clnt_res,  CLIENT *clnt)
{
	d_modify_value_1_argument arg;
	arg.key = key;
	arg.value1 = value1;
	arg.N_value2 = N_value2;
	arg.V_value2 = V_value2;
	return (clnt_call (clnt, d_modify_value, (xdrproc_t) xdr_d_modify_value_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_int, (caddr_t) clnt_res,
		TIMEOUT));
}

enum clnt_stat 
d_delete_key_1(int key, int *clnt_res,  CLIENT *clnt)
{
	return (clnt_call(clnt, d_delete_key,
		(xdrproc_t) xdr_int, (caddr_t) &key,
		(xdrproc_t) xdr_int, (caddr_t) clnt_res,
		TIMEOUT));
}

enum clnt_stat 
d_exist_1(int key, int *clnt_res,  CLIENT *clnt)
{
	return (clnt_call(clnt, d_exist,
		(xdrproc_t) xdr_int, (caddr_t) &key,
		(xdrproc_t) xdr_int, (caddr_t) clnt_res,
		TIMEOUT));
}
