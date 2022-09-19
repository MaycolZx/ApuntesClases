Analogia:
Comparar 8 escarabajos a 1M de hormigas, es como comparar 8 nucleos a 1M de threads.
Depende de mucho en que usemos los nucleos y los threads.
Secuencia
Paralela en GPU
Paralelo


## Sep-19-2022:
"stl" significa Standard Library

threads en cpu no en gpu

El tiempo computacional es medir el numero de movientos para ejecutar una accion

```cpp
#include <vector>
#include <iostream>
using namespace std;


int main(){
    vector<int> v(4);
    v.push_back(3);
    v[2]=9;
    cout<<v[0]<<endl;
    //push_back  k + expancion
    //push_front n + k + expancion
    //pop_back   k
    //pop_front  n
    //[ ]        K sobrecarga de operadores
    return 0;
}
```
El vector es super rapido en el acceso "[ ]"(sobrecarga de operadores), pero no en lo demas
Veremos  que es una lista:
son bloques enlazados unos con otros

Son bloques dispersos , no hay fora de locarzar algo como con los arrays , la unica manera de moverse

seria con los enlaces


```cpp
#include <iostream>
#include <list>
using namespace std;

int main(){
    list<int> v(4);
    v.push_back(3);
    v.push_front(6);
    // v[2]= 9;
    //push_back     k
    //push_front    k (constate) 
    //pop_back      k
    //pop_front     k (constante)
    //[ ]           n               //
    return 0;
}

```
//La lista es optima en todo expepto en los parentesis "[ ]"(sobrecarga de operadores)
//Si queremos insertar y mover muchos elementos es usar "list"

//Conclusion lo ideal seria usar insersion en "k"(tiempo constante) y acceso en tambien en "k"(tiempo constate)

//Implementar una lista y un vector que funciones con esas cuatra cosas:
//push_back,push_front,pop_back,pop_front.

```cpp

#include <iostream>
using namespace std;

class cvector{
    int *v;
    int n, ne;
    int f(int i){
        return v[i];
    }

    int & operator[](int i){
        return v[1];
    }
};

int main(){
    int a;
    cvector x;
    a = x.f(3);
    x.f(3)=4;
    return 0;
}
```