#ifndef LIB_MSG_H
#define LIB_MSG_H

   #define MAX 256

   //  message = op + q_name + (nombre, N) + (nombre, i, valor) + (nombre, i)
   struct message 
   {
      // peticion 
      int      op, name, i;
      char     *value1 ,q_name[MAX];
      double   *value2;
      // respuesta
    //int    value;
      char   status;
   } ;

#endif