#pragma once
class Person
{
private: 

public:
   int age = 0;

   int  get_age();
   Person();
   ~Person();
};


class Student(Person)
{
private: 

public:
   string id = "";

   float  get_gpa();
   Student();
   ~Student();
};


class Professor(Person)
{
private: 

public:
   string title = "";

   void  teach();
   Professor();
   ~Professor();
};


