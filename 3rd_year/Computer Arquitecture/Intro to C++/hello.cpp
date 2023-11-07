#include<iostream>

int main(){
    //Programa de Hola Mundo
    std::cout << "Hello C++\n";
}

/*
Después ejecuté el comando "g++ hello.cpp -E -o hello.ii" en terminal
-E flag -> Solo precompila
-o flag -> Guarda el resultado en un archivo 

Después ejecuté el comando "g++ hello.cpp -S -o hello.s" en terminal
-S flag -> Genera código ensamblador

Después ejecuté el comando "g++ hello.cpp -c -o hello.o" en terminal
-c flag -> Genera archivo objeto, que puede enlazarse a otros archivos objeto

Después ejecuté el comando "g++ hello.cpp -o hello.o" en terminal
(solo) -o flag -> Genera archivo ejecutable

Herramientas no cubiertas en el curso:
    -nm
    -readelf
    -objdump
    -c++filt
*/