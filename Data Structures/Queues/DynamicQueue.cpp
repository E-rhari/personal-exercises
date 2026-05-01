#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class DynamicQueue {
private:
    class Node{
    public:
        Type value;
        Node* next;
    };

    Node* head;
    int size;

public:
    DynamicQueue(){
        head = nullptr;
        size = 0;
    }
    ~DynamicQueue(){
        while(!isEmpty())
            dequeue();
        free(head);
    }


    void enqueue(Type value){
        Node* element = (Node*)malloc(sizeof(Node));
        if(element == nullptr)
            throw runtime_error("Out of Memory!");

        element->value = value;
        element->next = head;
        head = element;
        size++;
    }

    Type dequeue(){
        if(isEmpty())
            return 0x0;

        Node* previous = nullptr;
        Node* current  = head;

        while(current->next != nullptr){
            previous = current;
            current  = current->next;
        }
        
        free(current);
        size--;

        if(previous == nullptr){
            head = nullptr;
            return 0x0;
        }
        previous->next = nullptr;
        return previous->value;

    }


    Type getHeadValue(){
        if(isEmpty())
            return 0x0;
        return head->value;
    }

    Type getTailValue(){
        if(isEmpty())
            return 0x0;
        
        Node* current = head;
        while(current->next != nullptr)
            current = current->next;
        return current->value;
    }
    

    void print(){
        Node* current = head;

        printf("Queue: [");
        while(current != nullptr){
            cout << current->value;
            if(current->next != nullptr)
                printf(", ");
            current = current->next;
        }
        cout << "] (size: " << getSize() << ")\n";
    }

    bool isEmpty(){
        return head == nullptr;
    }
    int getSize(){
        return size;
    }
};


int main(){
    DynamicQueue<int> queue;

    for(int i=1; i<=20; i++){
        queue.enqueue(i + 2 * i*i);
        printf("--- After %d enqueues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Top Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    for(int i=1; i<=25; i++){
        queue.dequeue();
        printf("--- After %d dequeues ---\n", i);
        queue.print();
        printf("Size of array:     %d\n", queue.getSize());
        printf("Top Element:       %d\n", queue.getHeadValue());
        printf("Tail Element:      %d\n\n", queue.getTailValue());
    }

    return 0;
}