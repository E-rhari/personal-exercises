#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class SequentialQueue {
private:
    int head;
    int tail;
    int size;
    Type* data;
    bool full;

    int nextIndex(int index){
        return (index+1)%size;
    }

    int previousIndex(int index){
        if(index-1 < 0)
            index += size;
        return (index-1)%size;
    }


public:
    SequentialQueue(int size){
        head = 0;
        tail = 0;
        full = false;
        this->size = size;
        data = (Type*)malloc(sizeof(Type)*size);
    }
    ~SequentialQueue(){
        while(!isEmpty())
            dequeue();
        free(data);
    }


    void enqueue(Type x){
        if(isFull())
            return;

        data[head] = x;
        head = nextIndex(head);

        if(head == tail)
            full = true;
    }

    Type dequeue(){
        if(isEmpty())
            return 0x0;

        Type value = data[tail];
        tail = nextIndex(tail);

        if(tail != head)
            full = false;
        return value;
    }


    void print(){
        printf("Queue %X: [", data);

        if(!isEmpty()){
            int current = previousIndex(head);
            while(current != tail){
                cout << data[current];
                cout << ", ";
                current = previousIndex(current);
            }
            cout << data[current];
        }

        printf("] (amount: %d)\n", getAmountOfElements());
    }

    bool isEmpty(){
        return tail == head && !full;
    }
    bool isFull(){
        return tail == head && full;
    }

    int getAmountOfElements(){
        if(full)
            return size;

        int amount = head - tail;
        if(amount < 0)
            amount = size + amount;

        return amount;
    }
    int getSize(){
        return size;
    }

    bool resize(int newSize){
        while(getAmountOfElements()>newSize)
            printf("%d\n",dequeue());

        Type* newData = (Type*)malloc(sizeof(Type)*newSize);
        if(newData == nullptr)
            return false;

        for(int i=0; i<getAmountOfElements(); i++)
            newData[i] = data[(tail+i)%size];
            

        free(data);
        data = newData;
        head = getAmountOfElements()%newSize;
        tail = 0;
        size = newSize;

        
        if(tail == head)
            full = true;    
        
        return true;
    }


    Type getHeadValue(){
        if(isEmpty())
            return 0x0;
        return data[previousIndex(head)];
    }
    Type getTailValue(){
        if(isEmpty())
            return 0x0;
        return data[tail];
    }
};


int main(){
    SequentialQueue<int> queue(20);

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
