#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class BinaryMinArrayHeap {
private:
    class Node{
    public:
        Type value;
        int priority;
    };

    Node* values;
    int size;
    int amount;


    void goUp(int index){
        if index == 0
            return;
        int parent = ((index)-1)/2;
        if (values[parent].priority > values[index].priority){
            Node tmp = values[index];
            values[index] = values[parent];
            values[parent] = tmp;
            goUp(parent);
        }
    }
    
    void goDown(int index){ // likely incorrect
        int left = (2*index)+1

        if(left >= amount)
            return;

        int smallestChild = values[left];
        int right = left+1;

        if(right >= amount)
            return;

        if(values[right]<values[left])
            smallestChild = values[right];

        if(values[index].priority > values[smallestChild.priority])
            Node tmp = values[index];
            values[index] = values[smallestChild];
            values[smallestChild] = tmp;
            goDown(smallestChild); 
    }

public:
    BinaryMinArrayHeap(int size){
        amount = 0;
        this.size = size;
        values = (Type*)malloc(sizeof(Type)*size);
    }

    // O(nlog(n))
    BinaryMinArrayHeap(Type[] array){ // bad and stinky
        amount = 0;
        this.size = 0;
        for(int i=0; i<sizeof(array); i++)
            insert(array[i]);
    }
    
    // O(n)
    BinaryMinArrayHeap(Type[] array, int size){
        if(size<0)
            return;
        for(int i = (index-1)/2; i>0; i--)
            goDown(i);
    }


    void insert(Node x){
        if(amount == size)
            return; // overflow
        if(amount < size){
            values[amount] = x;
            goUp(amount);
            amount++;
        }
    }


    void getMin(){
        return values[0];
    }


    void removeMin(){
        if(amount = 0)
            return; // underflow
        amount--;
        values[0] = values[amount];
        goDown();
    }

    // O(nlog(n))
    Type* heapSort(){
        while(amount>0){    //O(n)
            amount--;
            Type min = values[0];
            values[0] = values[amount];
            values[amount] = min;
            goDown(0);  //O(log(n))
        }
    }
};