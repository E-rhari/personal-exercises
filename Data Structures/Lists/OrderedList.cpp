#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class OrderedList {
private:
    class Node{
    public:
        Type value;
        Node* next;
    };
    Node* head;
    int size;

public:
    OrderedList(){
        size = 0;
        head = nullptr;
    }

    bool insert(Type x){
        Node* el = (Node*)malloc(sizeof(Node));
        if(el == nullptr)
            return false;
        el->value = x;
        
        if(isEmpty()){
            head = el;
            el->next = nullptr;
        }
        else{
            Node** nextAndPrev = search(x);
            Node* next = nextAndPrev[0];
            Node* prev = nextAndPrev[1];
            free(nextAndPrev);
            if(next == nullptr){ // end of list
                prev->next = el;
                el->next = nullptr;
            }
            else if(prev == nullptr){ // start of list
                el->next = head;
                head = el;
            }
            else{
                el->next = next;
                prev->next = el;
            }
        }

        size++;
        return true;
    }

    bool remove(Type x){
        Node** elAndPrev = search(x);
        Node* el   = elAndPrev[0];
        Node* prev = elAndPrev[1];
        free(elAndPrev);
        
        if(el == nullptr)
            return false;

        prev->next = el->next;
        free(el);

        size--;
        return true;
    }
    bool removeIn(int index){
        Node* el = getNode(index);
        if(el == nullptr)
            return false;

        if(index == 0)
            head = head->next;
        else{
            Node* prev = getNode(index-1);
            if(prev == nullptr)
                head = nullptr;
            else
                prev->next = el->next;
            free(el);
        }
        size--;
        return true;
    }

    Node* getNode(int index){
        if(index<0 || index>=getSize())
            return nullptr;

        Node* current = head;
        for(int i=0; i<index && current != nullptr; i++)
            current = current->next;
        return current;
    }
    Type get(int index){
        Node* node = getNode(index);
        if(node == nullptr)
            return 0x0;
        return node->value;
    }

    Node** search(Type x){
        Node* current = head;
        Node* prev = nullptr;
        
        while(current != nullptr && current->value < x){
            prev = current;
            current = current->next;
        }

        Node** currAndPrev = (Node**)malloc(sizeof(Node*)*2);
        currAndPrev[0] = current;
        currAndPrev[1] = prev;
        return currAndPrev;
    }

    bool isEmpty(){
        return head == nullptr;
    }
    int getSize(){
        return size;
    }

    void print(){
        cout << "List: [";
        Node* current = head;
        while(current!=nullptr){
            cout << current->value;
            if(current->next != nullptr)
                cout << ", ";
            current = current->next;
        }
        cout << "] (size: " << getSize() << ")\n";
    } 
};


int main(){
    OrderedList<int> list = OrderedList<int>();
    list.print();

    int values[] = {1,2,7,3,6,9};
    for(int value : values){
        list.insert(value);
        list.print();
    }

    list.remove(9);
    list.print();

    list.removeIn(3);
    list.print();
    list.remove(6);
    list.print();
    list.removeIn(200);
    list.print();
    list.removeIn(-200);
    list.print();
    for(int i=0; i<7; i++){
        list.removeIn(0);
        list.print();
    }
}