#include "../Lists/List.cpp"

#include<cstdlib>
#include<stdexcept>
#include<iostream>
#include<cmath>
#include <typeinfo>
#include <type_traits>
// #include<hash>
using namespace std;

#pragma once

template <typename Type>
class ExternalChainHashTable {
private:
    List<Type>* table;

    int size;
    int amount;

    
    int hashFunc(Type x){
        // int h = 5381;
        // char* s = (char*)&x;
        // for(int i=0; i<sizeof(Type)/sizeof(char); i++)
        //     h = h*33 + s[i];
        return hash<Type>{}(x);
    }

    int hashCode(Type x){
        return abs(hashFunc(x)) % size;
    }

public:
    ExternalChainHashTable(int size) {
        this->table = new List<Type>[size];
        for(int i=0; i<size; i++)
            this->table[i] = List<Type>();
        
        this->size = size;
        this->amount = 0;
    }
    ExternalChainHashTable(int amountOfElements, int loadFactor) 
        : ExternalChainHashTable(ceil((float)amountOfElements/(float)loadFactor)) {}
    ~ExternalChainHashTable(){
        // do nothing
    }


    void insert(Type x){
        int index = hashCode(x);
        if(table[index].insert(x))
            amount++;
    }


    List<Type>::Node* search(Type x){
        int index = hashCode(x);
        List<Type> list = table[index];

        return list.search(x)[0];

    }


    void remove(Type x){
        int index = hashCode(x);
        if(table[index].remove(x))
            amount--;
    }


    void print(int hash){
        int index = hash % size;
        table[index].print();
    }
    void print(){
        for(int i=0; i<size; i++){
            printf("%d:\t", i);
            table[i].print();
        }
    }


    int getAmount(){
        return amount;
    }
};


// int main(){
//     int n = 50;

//     ExternalChainHashTable<int> table(n, 3);

//     printf("Inserting...\n");
//     for(int i=0; i<n; i++){
//         int val = -i*4 + i*i;
//         table.insert(val);
//         printf("%d,\t", val);
//     }
//     printf("\n");
//     table.print();

//     printf("Removing...");
//     for(int i=0; i<ceil(n/2); i++){
//         int val = -i*4 + i*i;
//         table.remove(val);
//         printf("%d,\t", val);
//     }
//     printf("\n");
//     table.print();
// }