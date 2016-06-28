#include <iostream>
#include "LinkedList.h"
#include "Stack.h"
#include "Queue.h"

using namespace std;

int main()
{
    cout << "============" << endl << "DLinkedList" << endl << "============" << endl;
    DLinkedList dl = DLinkedList();
    dl.insert(1);
    dl.insert(2);
    dl.insert(3);
    dl.insert(4);
    dl.insert(5);

    dl.print();

    cout << dl.contains(2) << endl;
    cout << dl.contains(6) << endl;

    dl.remove(6);
    dl.print();
    dl.remove(3);
    dl.print();
    dl.remove(1);
    dl.print();

    return 0;
}
