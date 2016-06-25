#pragma once
#include <iostream>

using namespace std;


template <class TY>
class Stack
{
public:
    Stack();
    Stack( Stack<TY> &s );
    ~Stack();

    bool push( TY item );
    bool pop( TY &item );
    bool top( TY &item );
    bool is_empty();
    int size();

    void print();

private:
    struct node
    {
        TY item;
        node *next;
    };

    node *headptr;
    int _size;
};


template <class TY>
Stack<TY>::Stack()
{
    //create an empty list
    headptr = nullptr;
    _size = 0;
}


template <class TY>
Stack<TY>::Stack( Stack<TY> &s )
{
    node *srctemp = nullptr;
    node *destemp = nullptr;
    headptr = nullptr;
    _size = 0;

    //If src is an empty list, headptr and _size are null and zero, just return.
    if ( s.is_empty() )
        return;

    //set up a temporary pointer to walk through the src list.
    srctemp = s.headptr;

    //allocated the first node.
    headptr = new (nothrow) node;
    if ( headptr == nullptr )
        return;

    //populate the first node, set next to nullptr.
    headptr -> item = srctemp -> item;
    headptr -> next = nullptr;
    _size++;

    //move src temp pointer down
    srctemp = srctemp -> next;

    //set up dest temp pointer to walk through the destination list.
    destemp = headptr;

    //while the src temp pointer isn't null, walk through
    while ( srctemp != nullptr )
    {
        //allocate a new node
        destemp -> next = new (nothrow) node;
        if ( destemp -> next == nullptr )
            return;
        //move destination pointer to new node.
        destemp = destemp -> next;

        //populate new node and increment size.
        destemp -> item = srctemp -> item;
        destemp -> next = nullptr;
        _size++;

        //move source pointer down.
        srctemp = srctemp -> next;
    }
}


template <class TY>
Stack<TY>::~Stack()
{
    //set up temp pointer to walk through list with.
    node *temp = nullptr;
    while ( headptr != nullptr )
    {
        //start at the beginning of the list, and move headptr down while
        //deleting the first node.
        temp = headptr;
        headptr = headptr -> next;
        delete temp;
    }
}


template <class TY>
bool Stack<TY>::push( TY item )
{
    //create a new node
    node * temp;
    temp = new (nothrow) node;
    if ( temp == nullptr )
        return false;

    //populate the new node, and change addresses appropriately.
    temp -> item = item;
    temp -> next = headptr;
    headptr = temp;
    _size++;
    return true;
}


template <class TY>
bool Stack<TY>::pop( TY &item )
{
    //set up temporary node to delete.
    node * temp = headptr;
    if (is_empty())
        return false;
    else
    {
        //if list isn't empty, change item, then move headptr down then delete it.
        item = headptr -> item;
        headptr = headptr -> next;
        delete temp;
        _size--;
        return true;
    }
}


template <class TY>
bool Stack<TY>::top( TY &item )
{
    if ( is_empty() )
        return false;
    else
    {
        //if list isn't empty, peek at the top item in the Stack.
        item = headptr -> item;
        return true;
    }
}


template <class TY>
bool Stack<TY>::is_empty()
{
    //empty lists are defined as headptr being nullptr.
    return headptr == nullptr;
}


template <class TY>
int Stack<TY>::size()
{
    //return the size of the list
    return _size;
}


template <class TY>
void Stack<TY>::print()
{
    //set up temp pointer to walk through list with.
    node *temp = headptr;

    //walk through list and print each item to the screen
    while ( temp != nullptr )
    {
        cout << temp -> item << endl;
        temp = temp -> next;
    }
    cout << endl;
}
