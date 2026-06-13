#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class BinaryMinHeap {
private:
    class Node{
    public:
        Type value;
        int priority;
        Node* next;
    };
    Node* head;
    int size;
    
public:
    void insert(Type x);

    void findMin();

    void removeMin();
};