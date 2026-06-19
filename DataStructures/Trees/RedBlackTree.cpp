#include<cstdlib>
#include<iostream>
#include "./BinarySearchTree.cpp"
using namespace std;


template <typename Type>
class RedBlackTree : public BinarySearchTree<Type> {
protected:
    class Node : public BinarySearchTree<Type>::Node {
    public:
        enum Color {
            RED,
            BLACK
        };

        Node* parent;
        Color color;
        int backHeight;

        Node(Type x=0x0, Color color=Color::BLACK){
            this->left = nullptr;
            this->right = nullptr;
            this->parent = nullptr;
            this->color = color;
            value = x;
        }
    };


    // turns node's right child into its parent
    void leftRotate(Node* node){
        Node* child = node->right;
        
        // node adopts child's child
        node->right = child->left;
        if(child->left != nullptr)
            child->left->parent = node;

        // takes parent
        child->parent = node->parent;

        // child takes node's parent's place
        if(node->parent == nullptr)
            root = child;
        else if(node == node->parent->left)
            node->parent->left = child;
        else //(node == node->parent->right)
            node->parent->right = child;

        // child becoming node's parent
        child->left = node;
        node->parent = child;
    }

    // turns node's left child into its parent
    void right(Node* node){
        Node* child = node->left;
        
        // node adopts child's child
        node->left = child->right;
        if(child->right != nullptr)
            child->right->parent = node;

        // take parent
        child->parent = node->parent;

        // child takes node's parent's place
        if(node->parent == nullptr)
            root = child;
        else if(node == node->parent->left)
            node->parent->left = child;
        else //(node == node->parent->right)
            node->parent->right = child;

        // child becoming node's parent
        child->right = node;
        node->parent = child;
    }


    void recolor(Node* node){ // please make it recursive
        Node* current = node;
        while(current->parent->color == Node::Color::RED){
            Node* parent = current->parent;
            Node* grandparent = parent->parent;

            if(parent == grandparent->left){
                Node* pibling = grandparent->right; // pibling, I've searched, is the gender neutral for uncle and aunt
                
                if(pibling->color == Node::Color::RED){
                    parent->color = Node::Color::BLACK;
                    pibling->color = Node::Color::BLACK;
                    grandparent->color = Node::Color::RED;
                    current = grandparent;
                }
                else { // pibling->color == Node::Color::BLACK
                    if(current == parent->right){
                        current = parent;
                        parent = current->parent;
                        grandparent = parent->parent;
                        leftRotate(current);
                    }
                    parent->color = Node::Color::BLACK;
                    grandparent->color = Node::Color::RED;
                    rightRotate(grandparent);
                }
            }
            else { // parent == grandparent->right
                // same but with left and right switched, i don't feel like doing it right now
            }
        }
    }



public:
    // as a red-black tree is just a way to balance a binary search tree,
    // the search method is unaltered 

    bool insert(Type x){
        Node* node = (Node*)malloc(sizeof(Node));
        if(node == nullptr)
            return false;

        Node** temp = (Node**)search(x);
        Node* parent = temp[1];
        free(temp);

        node->parent = parent;

        if(parent == nullptr)
            root = node;
        else if(node->value < parent->value)
            parent->left = node;
        else //(node->value >= parent->value)
            parent->right = node;
        
        recolor(node);
        return true;
    }

    bool remove(Type x){
        // to-do
        return false;
    }

};


int main(){
    return 0;
}