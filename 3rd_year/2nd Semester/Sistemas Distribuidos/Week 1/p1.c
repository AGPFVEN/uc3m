#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main (int argc, char **argv)
{
	printf("Programa P1 \n");

    //Crear array dinámico
    long analizing_arg;
    char *end;
    int array_length = 0;
    long *dynamic_array = (long*)malloc(sizeof(long) * argc - 1);

    //Verificar que memoria se asignó correctamente
    if (dynamic_array == NULL){

        perror("Error allocating memory. args to dynamic array");
        return -1;

    } else {

        printf("Memory allocated successfully\n");

        //Análisis de argumentos
        for(int i=1; i<argc; i++){

            //Convertir de char a long int
            analizing_arg = strtol(argv[i], &end, 10);
            printf("Argumento %d: ", i + 1); 

            if(*end != '\0'){
                //Casos inútiles
                printf("Error de conversión\n");
            } else {
                //Casos útiles
                printf("%ld\n", analizing_arg);

                //Añadir número a array dinámico
                dynamic_array[i - 1] = analizing_arg;
                array_length++;
            }
        }

        //Comprobar que argumentos entraron bien
        printf("The elements of the array are: "); 
        for (int k = 0; k < array_length; ++k) { 
            printf("%ld, ", dynamic_array[k]); 
        }
    }

    return 0;
}

//Si un argumento tiene un * es una referencia por valor (se copia y se usa la copia) si se pasa un ** se pasa por referencia y se modifica el original
//realloc es para reusar un array dinamico pero quitar espacio
void obtenerMinMax(int max, int *darray, int min_num, int max_num){

}

    //Primer bucle para contar
/*
    long analizing_arg;
    long min;
    long max;
    bool check = false;
    char *end;
    for(int i=1; i<argc; i++){

        analizing_arg = strtol(argv[i], &end, 10);
        printf("Argumento %d: ", i + 1);

        if(*end != '\0'){
            printf("Error de conversión\n");
        } else {
            printf("%ld\n", analizing_arg);
            
            if (check == false){
                min = analizing_arg;
                max = analizing_arg;
                check = true;
            } else {
                if (analizing_arg < min){
                    min = analizing_arg;
                }
                if (analizing_arg > max){
                    max = analizing_arg;
                }
            }
        }
    }

	return 0;
}
*/