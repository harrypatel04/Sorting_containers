cmake_minimum_required(VERSION 3.5)
project(cpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    CLinkedList.cpp
    DLinkedList.cpp
    LinkedList.h
    Queue.h
    SLinkedList.cpp
    Stack.h main.cpp)

add_executable(cpp ${SOURCE_FILES})
