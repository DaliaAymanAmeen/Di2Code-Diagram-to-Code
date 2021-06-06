#pragma once
#include <string>
using namespace std;

class Person
{
private: 
  //write your private attributes here
public:
   int age = 0;

   int  get_age();
   Person();
   ~Person();
};


class Student : public Person
{
private: 
 //write your private attributes here
public:
   string id = "";

   float  get_gpa();
   Student();
   ~Student();
};


class Professor : public Person
{
private: 
 //write your private attributes here
public:
   string title = "";

   void  teach();
   Professor();
   ~Professor();
};


