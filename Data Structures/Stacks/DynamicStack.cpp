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

    Type getTopValue(){
        if(top != nullptr)
            return top->value;
        return 0;
    }

    int getSize(){
        return size;
    }

    
    void push(Type value){
        Node* newNode = (Node*)malloc(sizeof(Node));
        
        newNode->value = value;
        newNode->next = top;

        top = newNode;
        size++;
    }

    Type pop(){
        if(top == nullptr)
            return 0;

        Node* oldTop = top;
        Type value = oldTop->value;

        top = top->next;
        free(oldTop);
        size--;

        return value;
    }
};


int main(){
    DynamicStack<int> q;

    q.push(3);
    printf("%d\n", q.getTopValue());
    q.pop();
    printf("%d\n", q.getTopValue());
    q.pop();
    q.pop();

    return 0;
}