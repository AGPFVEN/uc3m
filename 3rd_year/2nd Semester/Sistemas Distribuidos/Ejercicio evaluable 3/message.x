typedef double t_vector<>;

struct get_res
{
    char value1[256];
    t_vector V_value2;
    int status;
};

program EJERCICIO3
{
    version EJERCICIO3_VERSION
    { 
        int d_init           ()                                           = 1;
        int d_set_value      (int key, string value1, t_vector V_value2)  = 2;
        get_res d_get_value  (int key)                                    = 3;
        int d_modify_value   (int key, string value1, t_vector V_value2)  = 4;
        int d_delete_key     (int key)                                    = 5;
        int d_exist          (int key)                                    = 6;
    } = 1; 
} = 10000;