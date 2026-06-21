#include<cstdlib>
#include<iostream>
#include <string> 
using namespace std;


template <typename Type>
class BinarySearchTree {
protected:

    class Node {
    public:
        Type value;
        Node* left;
        Node* right;

        Node(Type x=0x0){
            left = nullptr;
            right = nullptr;
            value = x;
        }

        virtual string toString(){
            return to_string(value);
        }
    };


    int size;


    void printPreOrder(Node* node){
        if(node == nullptr)
            return;

        cout << node->toString() << ", ";
        printPreOrder(node->left);
        printPreOrder(node->right);
    }

    void printSymmetricOrder(Node* node){
        if(node == nullptr)
            return;
            
        printSymmetricOrder(node->left);
        cout << node->toString() << ", ";
        printSymmetricOrder(node->right);
    }

    void printPostOrder(Node* node){
        if(node == nullptr)
            return;

        printPostOrder(node->left);
        printPostOrder(node->right);
        cout << node->toString() << ", ";
    }

    
public:
    BinarySearchTree(){
        root = nullptr;
        size=0;
    }

    Node* root;

    Node** search(Type x){
        Node* node = root;
        Node* parent = nullptr;

        while(node != nullptr && node->value != x){
            parent = node;
            if(node->value > x)
                node = node->left;
            else if(node->value < x)
                node = node->right;
        }

        Node** packet = (Node**)malloc(sizeof(Node*)*2);
        packet[0] = node;
        packet[1] = parent;
        return packet;
    }
    // Node** recursiveSearch(Type x, Node* node=root){ // does not return the parent because i don't want to do it
    //     if(node == nullptr || node->value = x)
    //         return node;

    //     if(node->value < x)
    //         return recursiveSearch(x, node->left);
    //     if(node->value > x)
    //         return recursiveSearch(x, node->right);
    // }

    bool insert(Type x){
        Node* element = (Node*)malloc(sizeof(Node));
        if(element == nullptr) // out of memory
            return false;
        *element = Node(x);

        if(isEmpty()){
            root = element;
            size++;
            return true;
        }

        Node** temp = search(x);
        Node* child  = temp[0];
        Node* parent = temp[1];
        free(temp);

        if(child != nullptr) // already on tree
            return false;
        if(parent->value > x)
            parent->left = element;
        else //parent->value < x
            parent->right = element;

        size++;
        return true;
    }

    bool remove(Type x){
        Node** temp = search(x);
        Node* node = temp[0];
        Node* parent = temp[1];

        if(node == nullptr) // not in tree
            return false;
        
        Node* child = nullptr;
        int amountOfChildren = 0;

        if(node->left != nullptr){
            amountOfChildren++;
            child = node->left;
        }
        if(node->right != nullptr){
            amountOfChildren++;
            child = node->right;
        }

        if(amountOfChildren <= 1){          // we are going to simply skip node 
            if(node == root)                // could be achieved through <parent == nullptr> in architectures withour a pointer to root
                root = child;               // as node has no other child and root is node, root has no other child, so me skip node
            else if(parent->left == node)
                parent->left = child;
            else if(parent->right == node)
                parent->right = child;
            free(node);
            size--;
            return true;
        }             

        // Because node has more than a single child, we need a switcheroo.
        // As deleting a node with 2 subtrees is rather troublesome, we are not doing it.
        // We will find a node with no more than one subtree and a convinient value be deleted in its place.
        // We will overwrite the value of x with the value from the node we are actually deleting.
        // This way, it'll be as a if we had deleted the node that had x as it's value
        Node* currentParent = node;
        Node* currentNode   = child;

        while(currentNode->left != nullptr){
            currentParent = currentNode;
            currentNode = currentNode->left;
        }

        if(currentNode == child)                        // current node didn't move
            node->right = child->right;                 // all of child's childeren are smaller than node. as child has no children to the left, we can just skip it.
        else
            currentParent->left = currentNode->right;   // all of currentNode's children as smaller than currentParent, so we can stick them on its left. as currentNode has no children to the left, we can jump through it.
        node->value = currentNode->value;               // we put node's value as not to lose it. we made sure that it isn't in a disruptive place
        free(currentNode);
        size--;
        return true;
    }

    bool isEmpty(){
        return root == nullptr;
    }
    int getSize(){
        return size;
    }


    typedef enum {
        PREORDER,
        SYMMETRIC,
        POSTORDER
    } Order;


    void print(Order order=Order::PREORDER){
        cout << "Tree: [";
        if(!isEmpty()){
            switch(order){
                case Order::PREORDER: printPreOrder(root);
                            break;
                case Order::SYMMETRIC: printSymmetricOrder(root);
                            break;
                case Order::POSTORDER: printPostOrder(root);
                            break;
            }
        }
        cout << "] (size: " << getSize() << ")\n";
    }
};


// int main(){
//     BinarySearchTree<int> tree;

//     tree.print(BinarySearchTree<int>::Order::POSTORDER);
//     tree.insert(3);
//     tree.insert(2);
//     tree.insert(5);
//     tree.insert(4);
//     tree.insert(6);
//     tree.insert(3);
//     tree.insert(1);
//     tree.insert(0);
//     tree.insert(0);
//     tree.print(BinarySearchTree<int>::Order::PREORDER);
//     tree.remove(0);
//     tree.print(BinarySearchTree<int>::Order::POSTORDER);
//     tree.remove(0);
//     tree.print(BinarySearchTree<int>::Order::POSTORDER);
//     tree.remove(6);
//     tree.print(BinarySearchTree<int>::Order::POSTORDER);
//     tree.remove(4);
//     tree.print(BinarySearchTree<int>::Order::POSTORDER);
//     tree.remove(5);
//     tree.print(BinarySearchTree<int>::Order::POSTORDER);
// }