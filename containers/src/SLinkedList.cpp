#include "LinkedList.h"

SLinkedList::SLinkedList ()
{
    headptr = nullptr;
}

SLinkedList::~SLinkedList()
{
    node *temp;

    while ( headptr != nullptr )
    {
        temp = headptr;
        headptr = headptr -> next;
        delete temp;
    }
}

bool SLinkedList::insert ( int n )
{
    node *temp = nullptr;
    node *curr = headptr;
    node *prev = headptr;

    temp = new (nothrow) node;
    if ( temp == nullptr )
        return false;
    temp -> item = n;
    temp -> next = nullptr;

    //Empty
    if ( headptr == nullptr )
    {
        headptr = temp;
        return true;
    }

    //Beginning
    if ( temp -> item <= headptr -> item )
    {
        temp -> next = headptr;
        headptr = temp;
        return true;
    }

    //Middle
    while ( curr != nullptr && curr -> item <= temp -> item )
    {
        prev = curr;
        curr = curr -> next;
    }

    prev -> next = temp;
    temp -> next = curr;
    return true;

}

bool SLinkedList::remove ( int n )
{
    node *temp = headptr;
    node *prev= headptr;
    node *curr = headptr;

    //empty
    if ( headptr == nullptr )
        return false;

    //beginning
    if ( headptr -> item == n )
    {
        headptr = headptr -> next;
        delete temp;
        return true;
    }

    //middle and end
    while ( curr != nullptr && curr -> item != n )
    {
        prev = curr;
        curr = curr -> next;
    }
    if ( curr == nullptr )
        return false;

    prev -> next = curr -> next;
    delete curr;
    return true;
}


bool SLinkedList::is_empty ()
{
    return headptr == nullptr;
}

int SLinkedList::size ()
{
    int size = 0;
    node *temp = headptr;

    while ( temp != nullptr )
    {
        size++;
        temp = temp -> next;
    }

    return size;
}


void SLinkedList::print ( ostream &out )
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


bool SLinkedList::contains ( int n )
{
    node *temp = headptr;

    while ( temp != nullptr )
    {
        if ( temp -> item == n )
            return true;

        temp = temp -> next;
    }

    return false;
}
