#pragma once
#include <iostream>

using namespace std;

template <class TY>
class Queue
{
public:
       Queue();
       Queue( Queue<TY> &q );
       ~Queue();

       bool enque( TY item );
       bool deque( TY &item );
       bool front( TY &item );
       bool is_empty();
       int size();

       void print();

   private:

       struct node
       {
           TY item;
           node *next;
       };
       node *tailptr;
       int _size;
};


template <class TY>
Queue<TY>::Queue()
{
    //create a tailptr to null
    tailptr = nullptr;
    //set size of empty Queue
    _size = 0;
}


template <class TY>
Queue<TY>::Queue( Queue<TY> &q )
{
    node *srctemp = nullptr;
    node *destemp = nullptr;
    node *headptr = nullptr;
    tailptr = nullptr;
    _size = q._size; //set new Queue to same size of old Queue

    //check if Queue is empty
    if ( q.is_empty() )
        return;

    //copy first node into empty Queue
    srctemp = q.tailptr -> next;
    destemp = new (nothrow) node;
    if ( destemp == nullptr )
        return;
    destemp -> item = srctemp -> item;

    //make a temp headptr to track front of Queue
    headptr = destemp;

    //if only one item in Queue
    if ( srctemp -> next == q.tailptr )
    {
           tailptr = destemp;
           //make the node point to itself
           tailptr -> next = tailptr;
    }

    //copy rest of Queue
    while( srctemp != q.tailptr )
    {
        srctemp = srctemp -> next;
        tailptr = new (nothrow) node;
        if ( tailptr == nullptr )
            return;
        destemp -> next = tailptr;
        tailptr -> item = srctemp -> item;
        tailptr -> next = headptr;
        destemp = destemp -> next;
    } ;
}


template <class TY>
Queue<TY>::~Queue()
{
    node *temp = tailptr;
    node *next = tailptr;

    //check if empty
    if ( is_empty ( ) )
        return;

    //delete every node
    while ( next != tailptr )
    {
        temp = next;
        next = temp -> next;
        delete temp;
    }

    delete next;
}


template <class TY>
bool Queue<TY>::enque( TY item )
{
    //create new node with passed in item value
    node *temp = nullptr;
    temp = new (nothrow) node;
    if ( temp == nullptr )
        return false;
    temp -> item = item;
    temp -> next = nullptr;

    //if empty make node tailptr
    if ( is_empty() )
    {
        tailptr = temp;
    }

    //add node to end of Queue
    temp -> next = tailptr -> next;
    tailptr -> next = temp;
    tailptr = temp;

    //increment size
    _size++;
    return true;
}


template <class TY>
bool Queue<TY>::deque( TY &item )
{
    node *temp = nullptr;

    //check if empty
    if ( is_empty() )
        return false;

    //check if only one node
    if ( tailptr == tailptr -> next )
    {
        item = tailptr->item;
        delete tailptr;
        tailptr = nullptr;
        _size--;
        return true;
    }

    //grab item and delete first node
    temp = tailptr -> next;
    tailptr -> next = temp -> next;
    item = temp->item;
    delete temp;

    //decrease size by one
    _size--;
    return true;
}


template <class TY>
bool Queue<TY>::front( TY &item )
{
    //check if empty
    if ( is_empty() )
        return false;

    //grab item of first node
    item = tailptr -> next -> item;
    return true;
}


template <class TY>
bool Queue<TY>::is_empty()
{
    //check if empty
    return tailptr == nullptr;
}


template <class TY>
int Queue<TY>::size()
{
    //return size of Queue
    return _size;
}


template <class TY>
void Queue<TY>::print()
{
    node *temp = tailptr;

    //check if empty
    if ( is_empty() )
        return;

    //print all items to the screen
    do {
        temp = temp -> next;
        cout << temp -> item << endl;
    } while( temp != tailptr );
    cout << endl;
}
