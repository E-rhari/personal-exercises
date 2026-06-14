// This tree is optmial if you know how often you access each node.
// It's kind of useless.
// Not sure if this should be a class, a namespace or just a function
#include<cstdlib>
#include<iostream>
#include "./BinarySearchTree.cpp"
#include "../Lists/List.cpp"
using namespace std;



namespace OptimalBinarySearchTree {

    class Cell {
    public:
        int index;
        int cost;       // C
        int probSum;    // S

        Cell(int index, int cost, int probSum){
            this->index = index;
            this->cost = cost;
            this->probSum = probSum;
        }
    };


    int* f;
    int* f0;
    Cell** matrix;
    List<int> indexOrder;


    // S(i,j) = S(i, j-1) + f[j] +f'[j]
    int S(int i, int j){
        if(matrix[i][j].probSum != -1)
            return matrix[i][j].probSum;
        return S(i, j-1) + f[j] + f0[j]; 
    }


    // C(i,j) = min(C(i, k-1) + C(k, j), i+1, j) + S(i,j)
    int C(int i, int j){
        if(matrix[i][j].cost != -1)
            return matrix[i][j].cost;

        int cost = __INT_MAX__;
        int index = 0;
        for(int k=i+1; k<=j; k++){
            int costk = C(i, k-1) + C(k, j);
            if(costk<cost){
                cost = costk;
                index = k;
            }
        }
        matrix[i][j].index = index;
        return cost + S(i,j);
    }


    void setInsertOrder(int i, int j){
        if(matrix[i][j].index == 0)
            return;
        int index = matrix[i][j].index;
        indexOrder.insert(index);
        setInsertOrder(i, index-1);
        setInsertOrder(index, j);
    }


    template <typename Type>
    static BinarySearchTree<Type> init(int n, Type c[], int frequency[], int nullFrequency[]){
        f  = frequency;
        f0 = nullFrequency;

        matrix = (Cell**)malloc(sizeof(Cell*)*n);
        for(int i=0; i < n; i++)
            matrix[i] = (Cell*)malloc(sizeof(Cell)*n);
        
        indexOrder = List<int>();
        
        for(int a=0; a<n; a++)
            for(int b=0; b<n-a; b++){   // this nested loops fill the matrix diagonally
                int i=b;
                int j=b+a;
                
                Cell* cell = &matrix[i][j];
                *cell = Cell(-1, -1, -1);

                if(i==j){   // diagonal
                    cell->cost = 0;
                    cell->index = 0;
                    cell->probSum = f0[i];
                    continue;
                }

                cell->probSum = S(i,j);
                cell->cost = C(i,j); // this also determines the index

                if(a==1)   // directly above the diagonal
                    cell->index = j;
            }

        BinarySearchTree<Type> tree = BinarySearchTree<Type>();
        setInsertOrder(0,n-1);
        while(!indexOrder.isEmpty()){
            tree.insert(c[indexOrder.get(0)]);
            indexOrder.removeIn(0);
        }
        printf("%d", C(0,n-1));

        free(f);
        free(f0);
        for(int i=0; i < n; i++)
            free(matrix[i]);
        free(matrix);

        return tree;
    }
};


int main(){
    int n;
    scanf("%d", &n);
    n++;

    int* c  = (int*)malloc(sizeof(int)*n);
    int* f  = (int*)malloc(sizeof(int)*n);
    int* f0 = (int*)malloc(sizeof(int)*n);

    scanf("%d", f0);
    
    for(int i=0; i<n-1; i++)
        scanf("%d %d %d", c+i+1, f+i+1, f0+i+1);
    
    printf("\n");

    BinarySearchTree tree = OptimalBinarySearchTree::init<int>(n, c, f, f0);
    printf("\n");
    tree.print();

    return 0;
}