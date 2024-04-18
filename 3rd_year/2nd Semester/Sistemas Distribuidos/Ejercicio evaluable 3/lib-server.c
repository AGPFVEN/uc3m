#include <stdio.h>
#include <stdlib.h>

#include "lib.h"
#include "message.h"

bool_t d_init_1_svc (int *result, struct svc_req *rqstp)
{
    bool_t ret;
    ret = TRUE;
    *result = init();
    return ret;
}