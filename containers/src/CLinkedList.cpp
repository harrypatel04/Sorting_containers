#include "LinkedList.h"

CLinkedList::CLinkedList ()
{
    tailptr = nullptr;
}

CLinkedList::~CLinkedList ()
{
    node *temp = tailptr;
    do
    {
        temp = temp -> next;
        delete temp;
    } while ( temp != tailptr );
}

bool CLinkedList::insert ( int n )
{
    node *temp;
    node *prev;
    node *curr;

    temp = new (nothrow) node;
    if ( temp == nullptr )
        return false;
    temp -> item = n;
    temp -> next = nullptr;

    //Empty
    if ( tailptr == nullptr )
    {
        tailptr = temp;
        temp -> next = temp;
        return true;
    }

    //Beginning
    if ( temp -> item <= tailptr -> next -> item )
    {
        temp -> next = tailptr -> next;
        tailptr -> next = temp;
        return true;
    }

    //Middle
    prev = tailptr -> next;
    curr = tailptr -> next;

    while ( curr != tailptr && curr -> item <= temp -> item )
    {
        prev = curr;
        curr = curr -> next;
    }

    //End
    if ( temp -> item > curr -> item )
    {
        temp -> next = curr -> next;
        curr -> next = temp;
        tailptr = temp;
        return true;
    }

    //Middle
    prev -> next = temp;
    temp -> next = curr;
    return true;
}

bool CLinkedList::remove ( int n )
{
    node *temp;
    node *prev = tailptr -> next;
    node *curr = tailptr -> next;
    //Empty
    if ( tailptr == nullptr )
        return false;

    //Beginning
    if ( tailptr -> next -> item == n )
    {
        //Last remaining node
        if ( tailptr == tailptr -> next )
        {
            delete tailptr;
            tailptr = nullptr;
            return true;
        }
        //Beginning
        temp = tailptr -> next;
        tailptr -> next = temp -> next;
        delete temp;
        return true;
    }

    //Middle
    while ( curr != tailptr && curr -> item != n )
    {
        prev = curr;
        curr = curr -> next;
    }
    //Not Found
    if ( curr -> item != n )
        return false;
    //End
    if ( curr == tailptr )
    {
        prev -> next = curr -> next;
        tailptr = prev;
        delete curr;
        return true;
    }
    //Middle
    prev -> next = curr -> next;
    delete curr;
    return true;
}

bool CLinkedList::contains ( int n )
{
    node *temp = tailptr;
    do
    {
        temp = temp -> next;
        if ( temp -> item == n )
            return true;
    } while ( temp != tailptr );

    return false;
}

bool CLinkedList::is_empty ()
{
    return tailptr == nullptr;
}

int CLinkedList::size ()
{
    node *temp = tailptr;
    int i = 0;
    do
    {
        temp = temp -> next;
        i++;
    } while ( temp != tailptr );

    return i;
}

void CLinkedList::print ( ostream &out )
{
    node *temp = tailptr;

    if ( is_empty() )
        return;

    out << "=========================================================" << endl;
    do
    {
        temp = temp -> next;
        out << temp -> item << endl;
    } while ( temp != tailptr );
    out << "=========================================================" << endl;
    out << endl;
}
