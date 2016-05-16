#include <iostream>

using namespace std;

#ifndef __LINKLIST_H
#define __LINKLIST_H

//Singularly linked list
class SLinkedList
{
public:
    SLinkedList();
    ~SLinkedList();

    bool insert ( int n );
    bool remove ( int n );
    bool is_empty ();
    bool contains ( int n );
    void print ( ostream &out=cout );
    int size ();


private:
    struct node
    {
        int item;
        node *next;
    };

    node *headptr;
};

//Doubly linked list
class DLinkedList
{
public:
    DLinkedList();
    ~DLinkedList();

    bool insert ( int n );
    bool remove ( int n );
    bool is_empty ();
    bool contains ( int n, bool forward=true );
    int size ();
    void print ( ostream &out=cout);

private:
    struct node
    {
        int item;
        node *next;
        node *last;
    };

    node *headptr;
    node *tailptr;
};

//Circularly linked list
class CLinkedList
{
public:
    CLinkedList();
    ~CLinkedList();

    bool insert ( int n );
    bool remove ( int n );
    bool contains ( int n );
    bool is_empty ();
    int size ();
    void print ( ostream &out=cout );

private:
    struct node
    {
        int item;
        node *next;
    };

    node *tailptr;
};

#endif // __LINKLIST_H
