#include<cstdlib>
#include<iostream>
#include "./BinarySearchTree.cpp"
using namespace std;


template <typename Type>
class RedBlackTree : public BinarySearchTree<Type> {
protected:
    using BinarySearchTree<Type>::BinarySearchTree;

    class RedBlackNode : public BinarySearchTree<Type>::Node {
    public:
        enum Color {
            RED,
            BLACK
        };

        RedBlackNode* parent;
        Color color;
        int backHeight;

        RedBlackNode(Type x=0x0, Color color=Color::BLACK){
            this->left = nullptr;
            this->right = nullptr;
            this->parent = nullptr;
            this->color = color;
            this->value = x;
        }

        RedBlackNode* getParent(){
            return parent;
        }

        RedBlackNode* getLeftChild(){
            return (RedBlackNode*) this->left;
        }

        RedBlackNode* getRightChild(){
            return (RedBlackNode*) this->right;
        }
    };


    // turns node's right child into its parent
    void leftRotate(RedBlackNode* node){
        RedBlackNode* child = node->getRightChild();
        
        // node adopts child's child
        node->right = child->getLeftChild();
        if(child->getLeftChild() != nullptr)
            child->getLeftChild()->parent = node;

        // takes parent
        child->parent = node->parent;

        // child takes node's parent's place
        if(node->parent == nullptr)
            this->root = child;
        else if(node == node->parent->getLeftChild())
            node->parent->left = child;
        else //(node == node->parent->rightRotate())
            node->parent->right = child;

        // child becoming node's parent
        child->left = node;
        node->parent = child;
    }

    // turns node's left child into its parent
    void rightRotate(RedBlackNode* node){
        RedBlackNode* child = node->getLeftChild();
        
        // node adopts child's child
        node->left = child->right;
        if(child->getRightChild() != nullptr)
            child->getRightChild()->parent = node;

        // take parent
        child->parent = node->parent;

        // child takes node's parent's place
        if(node->parent == nullptr)
            this->root = child;
        else if(node == node->parent->getLeftChild())
            node->parent->left = child;
        else //(node == node->parent->right)
            node->parent->right = child;

        // child becoming node's parent
        child->right = node;
        node->parent = child;
    }


    void recolor(RedBlackNode* node){ // please make it recursive
        RedBlackNode* current = node;

        if(current->parent == nullptr){
            current->color = RedBlackNode::Color::BLACK;
            return;
        }

        while(current->parent->color == RedBlackNode::Color::RED){
            printf("Tuturu~%d\n", node->value);
            RedBlackNode* parent = current->parent;
            RedBlackNode* grandparent = parent->parent;

            if(grandparent == nullptr)
                return;

            bool isLeftChild = false;
            RedBlackNode* pibling = nullptr; // pibling, I've searched, is the gender neutral for uncle and aunt
            RedBlackNode* compareChild = nullptr;
            if(parent == grandparent->getLeftChild()){
                isLeftChild = true;
                pibling = grandparent->getRightChild(); 
                compareChild = parent->getRightChild();
            }
            else {// (parent == grandparent->left)
                isLeftChild = false;
                pibling = grandparent->getLeftChild(); 
                compareChild = parent->getLeftChild();
            }
                
            if(pibling->color == RedBlackNode::Color::RED){
                parent->color = RedBlackNode::Color::BLACK;
                pibling->color = RedBlackNode::Color::BLACK;
                grandparent->color = RedBlackNode::Color::RED;
                current = grandparent;
            }
            else { // pibling->color == RedBlackNode::Color::BLACK
                if(current == compareChild){
                    current = parent;
                    parent = current->parent;
                    grandparent = parent->parent;
                    if(isLeftChild)
                        leftRotate(current);
                    else
                        rightRotate(current);
                }
                parent->color = RedBlackNode::Color::BLACK;
                grandparent->color = RedBlackNode::Color::RED;
                if(isLeftChild)
                    rightRotate(grandparent);
                else
                    leftRotate(grandparent);
            }
        }
    }


public:
    RedBlackTree() : BinarySearchTree<Type>(){};

    // as a red-black tree is just a way to balance a binary search tree,
    // the search method is unaltered 

    bool insert(Type x){
        RedBlackNode* node = new RedBlackNode();
        if(node == nullptr)
            return false;
        printf("Inserting %d!\n", x);

        RedBlackNode** temp = (RedBlackNode**)this->search(x);
        RedBlackNode* parent = temp[1];
        free(temp);
        
        node->parent = parent;
        node->value = x;
        
        if(parent == nullptr)
            this->root = node;
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
    printf("Create tree!\n");
    RedBlackTree<int> tree;
    printf("Insert!\n");
    for(int i=0; i<10; i++)
        tree.insert(i*4 - i*i);
    tree.print();
    return 0;
}