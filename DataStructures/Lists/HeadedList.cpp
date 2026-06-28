#include<cstdlib>
#include<stdexcept>
#include<iostream>
using namespace std;

template <typename Type>
class List {
public:
    class Node{
    public:
        Type value;
        Node* next;
    };
    Node* head;
    int size;


    List(){
        size = 0;
        head = new Node();
        head->value = __INT_MAX__;
        head->next = nullptr;
    }

    bool insert(Type x, int index=-1){
        Node* el = new Node();
        if(el == nullptr)
            return false;
        el->value = x;

        if(index==-1)
            index = getSize();
        Node* prev = getNode(index-1);
        if(prev == nullptr) // out of bounds
            return false;
        el->next = prev->next;
        prev->next = el;

        size++;
        return true;
    }

    bool insertBefore(Type x, Type after){
        Node* el = new Node();
        if(el == nullptr)
            return false;
        el->value = x;

        Node** currAndPrev = search(after);
        Node* curr = currAndPrev[0];
        Node* prev = currAndPrev[1];
        free(currAndPrev);
        
        if(curr == nullptr) // element not in list
            return false;
        el->next = prev->next; //aka curr
        prev->next = el;
        size++;
        return true;
    }

    bool remove(Type x){
        Node** elAndPrev = search(x);
        Node* el   = elAndPrev[0];
        Node* prev = elAndPrev[1];
        free(elAndPrev);
        
        if(el == nullptr) // not in list
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

        Node* prev = getNode(index-1);
        if(prev == nullptr) // out of bound
            return false;
        prev->next = el->next;
        free(el);
        size--;
        return true;
    }

    Node* getNode(int index){
        if(index<-1 || index>=getSize())
            return nullptr;

        Node* current = head;
        for(int i=-1; i<index && current != nullptr; i++)
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
        Node* current = head->next;
        Node* prev = head;

        while(current != nullptr && current->value != x){
            prev = current;
            current = current->next;
        }

        Node** currAndPrev = (Node**)malloc(sizeof(Node*)*2);
        currAndPrev[0] = current;
        currAndPrev[1] = prev;
        return currAndPrev;
    }

    bool isEmpty(){
        return head->next == nullptr;
    }
    int getSize(){
        return size;
    }

    void print(){
        cout << "List: [";
        Node* current = head->next;
        while(current!=nullptr){
            cout << current->value;
            if(current->next != nullptr)
                cout << ", ";
            current = current->next;
        }
        cout << "] (size: " << getSize() << ")\n";
    } 
};


// int main(){
//     List<int> list = List<int>();
//     list.print();

//     int values[] = {1,2,3,6,9};
//     for(int value : values){
//         list.insert(value);
//         list.print();
//     }

//     int values2[] = {7, 4, 75, 89, 45};
//     int indexes[] = {2, 4, 76, -1, 0};
//     for(int i=0; i < 5; i++){
//         list.insert(values2[i], indexes[i]);
//         list.print();
//     }

//     list.insertBefore(68, 4);
//     list.print();
//     list.insertBefore(23, 45);
//     list.print();
//     list.insertBefore(3, 67);
//     list.print();

//     list.remove(9);
//     list.print();

//     list.removeIn(4);
//     list.print();
//     list.remove(6);
//     list.print();
//     list.removeIn(200);
//     list.print();
//     list.removeIn(-200);
//     list.print();
//     for(int i=0; i<7; i++){
//         list.removeIn(0);
//         list.print();
//     }
// }