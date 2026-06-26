#include "../Lists/List.cpp"

#include<cstdlib>
#include<stdexcept>
#include<iostream>
#include<cmath>
using namespace std;

template <typename Type>
class ExternalChainHashTable {
private:
    List<Type>* table;

    int size;

    // not sure if this hash is any good
    int hash(Type x){
        int h = 5381;
        char* s = (char*)&x;
        for(int i=0; i<sizeof(Type)/sizeof(char); i++)
            h = h*33 + s[i];
        return h;
    }

    int hashCode(Type x){
        return hash(x) % size;
    }

public:
    ExternalChainHashTable(int size) {
        this->table = (List<Type>*)malloc(sizeof(List<Type>)*size);
        for(int i=0; i<size; i++)
            this->table[i] = List<Type>();
        
        this->size = size;
    }
    ExternalChainHashTable(int amountOfElements, int loadFactor) 
        : ExternalChainHashTable(ceil((float)amountOfElements/(float)loadFactor)) {}
    ~ExternalChainHashTable(){
        free(table);
    }


    void insert(Type x){
        int index = hashCode(x);
        table[index].insert(x);
    }


    List<Type>::Node* search(Type x){
        int index = hashCode(x);
        List<Type> list = table[index];

        for(int i=0; i<list.getSize(); i++)
            if(x == list.get(i))
                return list.getNode(i);
        return nullptr;
    }


    void remove(Type x){
        int index = hashCode(x);
        table[index].remove(x);
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
};


int main(){
    int n = 50;

    ExternalChainHashTable<int> table(n, 3);

    printf("Inserting...\n");
    for(int i=0; i<n; i++){
        int val = -i*4 + i*i;
        table.insert(val);
        printf("%d,\t", val);
    }
    printf("\n");
    table.print();

    printf("Removing...");
    for(int i=0; i<ceil(n/2); i++){
        int val = -i*4 + i*i;
        table.remove(val);
        printf("%d,\t", val);
    }
    printf("\n");
    table.print();
}