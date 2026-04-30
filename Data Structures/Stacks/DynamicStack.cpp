#include<cstdlib>
#include<iostream>
using namespace std;


template <typename Type>
class DynamicStack {

private:
    class Node{
    public:
        Type value;
        Node* next;
    };

    int size;
    Node* top;

public:
    DynamicStack(){
        top = nullptr;
        size = 0;
    }
    ~DynamicStack(){
        while (top!=nullptr)
            pop();
    }

    
    void push(Type value){
        Node* newNode = (Node*)malloc(sizeof(Node));
        
        newNode->value = value;
        newNode->next = top;

        top = newNode;
        size++;
    }

    Type pop(){
        if(isEmpty())
            return 0;

        Node* oldTop = top;
        Type value = oldTop->value;

        top = top->next;
        free(oldTop);
        size--;

        return value;
    }

    
    void print(){
        printf("Stack: [");

        Node* node = top;
        while(node != nullptr){
            cout << node->value;
            if(node->next != nullptr)
                printf(", ");
            node = node->next;
        }
        cout << "] (amount:" << getSize() << ")\n";
    }

    Type getTopValue(){
        if(top != nullptr)
            return top->value;
        return 0;
    }
    int getSize(){
        return size;
    }
    bool isEmpty(){
        return top == nullptr;
    }
};


int main(){
    DynamicStack<int> stack;

    for(int i=1; i<=20; i++){
        stack.push(i + 2 * i*i);
        printf("--- After %d pushes ---\n", i);
        stack.print();
        printf("Size of array:     %d\n", stack.getSize());
        printf("Top Element:       %d\n\n", stack.getTopValue());
    }

    for(int i=1; i<=25; i++){
        stack.pop();
        printf("--- After %d pops ---\n", i);
        stack.print();
        printf("Size of array:     %d\n", stack.getSize());
        printf("Top Element:       %d\n\n", stack.getTopValue());
    }

    return 0;
}