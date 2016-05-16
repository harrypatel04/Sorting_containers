#include "LinkedList.h"

DLinkedList::DLinkedList ()
{
    headptr = nullptr;
    tailptr = nullptr;
}

DLinkedList::~DLinkedList ()
{
    node *temp;

    while ( headptr != nullptr )
    {
        temp = headptr;
        headptr = headptr -> next;
        delete temp;
    }
}

bool DLinkedList::insert ( int n )
{
    node *temp;
    node *prev;
    node *curr;

    temp = new (nothrow) node;
    if ( temp == nullptr )
        return false;
    temp -> item = n;
    temp -> next = nullptr;
    temp -> last = nullptr;

    //Insert into empty list
    if ( headptr == nullptr )
    {
        headptr = temp;
        tailptr = temp;
        return true;
    }

    //Insert into first location. Is a sorted list.
    if ( temp -> item <= headptr -> item )
    {
        temp -> next = headptr;
        headptr -> last = temp;
        headptr = temp;
        return true;
    }

    prev = headptr;
    curr = headptr;

    while ( curr != nullptr && curr -> item <= temp -> item )
    {
        prev = curr;
        curr = curr -> next;
    }

    //Insert at end of list
    if ( curr == nullptr )
    {
        prev -> next = temp;
        temp -> last = prev;
        tailptr = temp;
        return true;
    }

    //Insert in middle of list
    prev -> next = temp;
    temp -> next = curr;
    curr -> last = temp;
    temp -> last = prev;
    return true;
}

bool DLinkedList::remove ( int n )
{
    node *temp = headptr;
    node *prev = headptr;
    node *curr = headptr;

    //Empty
    if ( headptr == nullptr )
        return false;

    //Front
    if ( headptr -> item == n )
    {
        //Last remaining node
        if ( headptr -> next = nullptr )
        {
            delete headptr;
            headptr = nullptr;
            tailptr = nullptr;
            return true;
        }

        headptr = headptr -> next;
        headptr -> last = nullptr;
        delete temp;
        return true;
    }

    //Middle
    while ( curr != nullptr && curr -> item < n )
    {
        prev = curr;
        curr = curr -> next;
    }

    if ( curr == nullptr || curr -> item != n )
        return false;

    //End
    if ( curr == nullptr )
    {
        prev -> next = nullptr;
        tailptr = prev;
        delete curr;
        return true;
    }
    //Middle
    prev -> next = curr -> next;
    curr -> next -> last = prev;
    delete curr;
    return true;
}

bool DLinkedList::contains ( int n, bool forward )
{
    node *temp = ( forward ? headptr : tailptr );

    while ( temp != nullptr )
    {
        if ( temp -> item == n )
            return true;
        temp = ( forward ? temp -> next : temp -> last );
    }
    return false;
}

void DLinkedList::print ( ostream &out)
{
    node *temp = headptr;

    out << "=========================================================" << endl;
    while ( temp != nullptr )
    {
        out << temp -> item << endl;
        temp = temp -> next;
    }
    out << "=========================================================" << endl;
    out << endl;
}

bool DLinkedList::is_empty ()
{
    return ( tailptr == nullptr && headptr == nullptr );
}


int DLinkedList::size ()
{
    node *temp = headptr;
    int i = 0;

    while ( temp != nullptr )
    {
        i++;
        temp = temp -> next;
    }

    return i;
}
