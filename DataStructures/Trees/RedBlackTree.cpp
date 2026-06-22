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

        RedBlackNode(Type x=0x0, Color color=Color::RED, RedBlackNode* parent=nullptr){
            this->left = nullptr;
            this->right = nullptr;
            this->parent = parent;
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

        string toString() override {
            char charColor;
            if(color == Color::RED)
                charColor = 'R';
            else // Color:BLACK
                charColor = 'N';
            return BinarySearchTree<Type>::Node::toString() + charColor;
        }
    };



    RedBlackNode* minimun(RedBlackNode* start){
        RedBlackNode* currentParent = nullptr;
        RedBlackNode* currentNode   = start;

        while(currentNode->left != nullptr){
            currentParent = currentNode;
            currentNode = currentNode->getLeftChild();
        }
        return currentNode;
    }


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

    void rotate(RedBlackNode* node, bool left){
        if(left)
            leftRotate(node);
        else
            rightRotate(node);
    }


    void transplant(RedBlackNode* u, RedBlackNode* v){
        if(u->parent == nullptr)
            this->root = v;
        else if(u == u->parent->getLeftChild())
            u->parent->left = v;
        else // (u == u->parent->getRightNode())
            u->parent->right = v;

        if(v != nullptr)
            v->parent = u->parent;
    }


    void insertFixUp(RedBlackNode* node){ // please make it recursive
        RedBlackNode* current = node;

        RedBlackNode* parent = current->parent;
        if(current->parent == nullptr){
            current->color = RedBlackNode::Color::BLACK;
            return;
        }
        RedBlackNode* grandparent = parent->parent;
        if(grandparent == nullptr)
            return;

        if(parent->color == RedBlackNode::Color::RED){

            bool parentIsLeftChild = false;
            RedBlackNode* pibling = nullptr; // pibling, I've searched, is the gender neutral for uncle and aunt
            RedBlackNode* compareChild = nullptr;
            if(parent == grandparent->getLeftChild()){
                parentIsLeftChild = true;
                pibling = grandparent->getRightChild(); 
                compareChild = parent->getRightChild();
            }
            else {// (parent == grandparent->getRightChild())
                parentIsLeftChild = false;
                pibling = grandparent->getLeftChild(); 
                compareChild = parent->getLeftChild();
            }
                
            if(pibling!=nullptr && pibling->color == RedBlackNode::Color::RED){
                // no need for rotations, recoliring is enough
                parent->color = RedBlackNode::Color::BLACK;
                pibling->color = RedBlackNode::Color::BLACK;
                grandparent->color = RedBlackNode::Color::RED;
                insertFixUp(grandparent);
            }
            else { // pibling->color == RedBlackNode::Color::BLACK
                if(current == compareChild){
                    // Switch current and parent so the black child is to the same side as the pibling 
                    current = parent;
                    rotate(current, parentIsLeftChild);
                    parent = current->parent;
                    grandparent = parent->parent;
                }
                // rotate
                parent->color = RedBlackNode::Color::BLACK;
                grandparent->color = RedBlackNode::Color::RED;
                rotate(grandparent, !parentIsLeftChild);
                insertFixUp(current);
            }
        }
    }


    void removeFixUp(RedBlackNode* node){
        RedBlackNode* current = node;

        if(current == this->root || current->color != RedBlackNode::Color::BLACK){        
            node->color = RedBlackNode::Color::BLACK;
            return;
        }

        bool isLeftChild = false;
        RedBlackNode* sibling = nullptr;
        RedBlackNode* cousin = nullptr;

        if(current == current->parent->getLeftChild()){
            isLeftChild = true;
            RedBlackNode* sibling = current->parent->getRightChild();
            RedBlackNode* cousin = sibling->getRightChild();
        }
        else{
            isLeftChild = false;
            RedBlackNode* sibling = current->parent->getLeftChild();
            RedBlackNode* cousin = sibling->getLeftChild();
        }

        if(sibling->color == RedBlackNode::Color::RED){
            sibling->color = RedBlackNode::Color::BLACK;
            current->parent->color = RedBlackNode::Color::RED;
            rotate(current->parent, isLeftChild);
            sibling = current->parent->getRightChild();
            cousin = sibling->getRightChild();
        }

        if(sibling->getLeftChild()->color  == RedBlackNode::Color::BLACK
        && sibling->getRightChild()->color == RedBlackNode::Color::BLACK){
            sibling->color = RedBlackNode::Color::RED;
            removeFixUp(current->parent);
        }
        else { 
            if(cousin->color == RedBlackNode::Color::BLACK){
                sibling->color = RedBlackNode::Color::RED;
                if(isLeftChild){
                    sibling->getLeftChild()->color = RedBlackNode::Color::BLACK;
                    rightRotate(sibling);
                }
                else{
                    sibling->getRightChild()->color = RedBlackNode::Color::BLACK;
                    leftRotate(sibling);
                }
            }
            sibling->color = current->parent->color;
            current->parent->color = RedBlackNode::Color::BLACK;
            cousin->color = RedBlackNode::Color::BLACK;
            rotate(current, isLeftChild);
        }
    }


public:
    RedBlackTree() : BinarySearchTree<Type>(){};

    RedBlackNode** search(Type x){
        return (RedBlackNode**)BinarySearchTree<Type>::search(x);
    }

    bool insert(Type x){
        RedBlackNode* node = new RedBlackNode();
        if(node == nullptr)
            return false;

        RedBlackNode** temp = this->search(x);
        RedBlackNode* child  = temp[0];
        RedBlackNode* parent = temp[1];
        free(temp);
        
        if(child != nullptr)
            return false;

        node->parent = parent;
        node->value = x;
        
        if(parent == nullptr)
            this->root = node;
        else if(node->value < parent->value)
            parent->left = node;
        else //(node->value >= parent->value)
            parent->right = node;

        insertFixUp(node);
        this->size++;
        return true;
    }

    bool remove(Type x){
        RedBlackNode** temp = search(x);
        RedBlackNode* node  = temp[0];
        free(temp);

        if(node == nullptr)
            return false;

        RedBlackNode* current = node;
        typename RedBlackNode::Color originalColor = current->color;
        
        RedBlackNode* child;
        if(node->getLeftChild() == nullptr){
            child = node->getRightChild();
            transplant(node, node->getRightChild());
        }
        else if(node->getRightChild() == nullptr){
            child = node->getLeftChild();
            transplant(node, child);
        }
        else { // node has 2 children
            current = minimun(node->getRightChild());
    
            originalColor = current->color;
            child = current->getRightChild();
            if(child != nullptr && current->parent == node)
                child->parent = current;
            else{
                transplant(current, child);
                current->right = node->getRightChild();
                if(current->getRightChild() != nullptr)
                    current->getRightChild()->parent = current;
            }
            transplant(node, current);
            current->left = node->left;
            current->getLeftChild()->parent = current;
            current->color = node->color;
        }
        
        if(child == nullptr){
            child = new RedBlackNode(0, RedBlackNode::Color::BLACK, current); // memory leak?
            removeFixUp(child);
            free(child);
        }
        else if(originalColor == RedBlackNode::BLACK)
            removeFixUp(child);

        this->size--;
        return true;
    }

};


int main(){
    RedBlackTree<int> tree;

    char command = ' ';
    int value = 0;

    while(scanf("%c", &command) != EOF){
        switch(command){
            case 'i':   scanf("%d", &value);
                        tree.insert(value);
                        break;
            case 'r':   scanf("%d", &value);
                        tree.remove(value);
                        break;
            case 'p':   tree.print();
                        break;
        }
    }

    // for(int i=0; i<10; i++)
    //     tree.insert(i*4 - i*i);
    // tree.print();
    

    return 0;
}