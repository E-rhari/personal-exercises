#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class AcyclicSequentialQueue {
private:
    int head;
    // tail is always equal to 0
    int size;
    Type* data;


public:
    AcyclicSequentialQueue(int initialSize=1){
        head = 0;
        this->size = initialSize;
        data = (Type*)malloc(sizeof(Type)*initialSize);
    }
    ~AcyclicSequentialQueue(){
        while(!isEmpty())
            dequeue();
        free(data);
    }


    void enqueue(Type x){
        if(isFull())
            resize(size*2);

        data[head] = x;
        head++;
    }

    Type dequeue(){
        if(isEmpty())
            return 0x0;

        Type value = data[0];
        for(int i=0; i<getAmountOfElements()-1; i++)
            data[i] = data[i+1];
        head--;

        return value;
    }


    void print(){
        printf("Queue %X: [", data);

        if(!isEmpty()){
            int current = head-1;
            while(current != 0){
                cout << data[current];
                cout << ", ";
                current -= 1;
            }
            cout << data[0];
        }

        printf("] (amount: %d)\n", getAmountOfElements());
    }

    bool isEmpty(){
        return head == 0;
    }
    bool isFull(){
        return head == size;
    }

    int getAmountOfElements(){
        return head;
    }
    int getSize(){
        return size;
    }

    bool resize(int newSize){
        while(getAmountOfElements()>newSize)
            dequeue();

        Type* newData = (Type*)malloc(sizeof(Type)*newSize);
        if(newData == nullptr)
            return false;

        for(int i=0; i<getAmountOfElements(); i++)
            newData[i] = data[i];

        free(data);
        data = newData;
        size = newSize;

        return true;
    }


    Type getHeadValue(){
        if(isEmpty())
            return 0x0;
        return data[head-1];
    }
    Type getTailValue(){
        if(isEmpty())
            return 0x0;
        return data[0];
    }
};


int main(){
    AcyclicSequentialQueue<int> queue = AcyclicSequentialQueue<int>();

    for(int i=1; i<=20; i++){
        queue.enqueue(i + 2 * i*i);
        printf("--- After %d enqueues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Head Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    for(int i=1; i<=25; i++){
        queue.dequeue();
        printf("--- After %d dequeues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Head Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    for(int i=1; i<=20; i++){
        queue.enqueue(i + 2 * i*i);
        printf("--- After %d enqueues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Head Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    printf(">> REZISE 10 <<\n\n");
    queue.resize(10);

    for(int i=1; i<=5; i++){
        queue.dequeue();
        printf("--- After %d dequeues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Head Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    printf(">> REZISE 30 <<\n\n");
    queue.resize(30);

    for(int i=1; i<=23; i++){
        queue.enqueue(i + 2 * i*i);
        printf("--- After %d enqueues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Head Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    return 0;
}
