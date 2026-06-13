#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class SequentialStack {

private:
    Type* data;
    int top;
    int size;

public:
    SequentialStack(int initialSize=1){
        data = (Type*)malloc(sizeof(Type)*initialSize);
        top = -1;
        size = initialSize;
    }
    ~SequentialStack(){
        free(data);
    }
    

    void push(Type value){
        if(top+1 >= size){
            Type* newData = (Type*)malloc(sizeof(Type)*size*2);
            if(newData == nullptr)
                throw runtime_error("Out of memory"); 

            for(int i=0; i<size; i++)
                newData[i] = data[i];

            free(data);
            data = newData;
            size *= 2;
        }
        top++;
        data[top] = value;
    }

    void pop(){
        if(isEmpty())
            return;
        top--;
    }


    void print(){
        printf("Stack %X: [", data);
        for(int i=top; i>0; i--)
            cout << data[i] << ", ";
        if(!isEmpty())
            cout << data[0];
        cout << "] (amount:" << getNumElem() << ")\n";
    }


    Type getTopValue(){
        if(isEmpty())
            return 0x0;
        return data[top];
    }

    int getNumElem(){
        return top+1;
    }

    int getSize(){
        return size;
    }

    bool isEmpty(){
        return top == -1;
    }
};



int main(){
    SequentialStack<int> stack = SequentialStack<int>();
    
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
}