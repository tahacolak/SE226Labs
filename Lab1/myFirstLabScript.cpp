//Question1
#include <iostream>
#include <string>
#include<stdio.h>
using namespace std;

int main() {
   
    string name;
    string studentId;
    
    
    cout << "What is your name? ";
    std::getline(std::cin, name);
    
    
    cout << "Hello " << name << "." << endl;
    
   
    cout << "What is your Student ID? ";
    getline(std::cin, studentId);
    
    
    cout << "Your ID is " << studentId <<endl;


//Question2




    double var1, var2;
    
    
    cout << "Enter a value for var1: ";
    cin >> var1;
    
   
    cout << "Enter a value for var2: ";
    cin >> var2;

    double sum = var1 + var2;
    double diff = var1 - var2;
    double prod = var1 * var2;
    
    
    cout << "var1 = " << var1 << endl;
    cout << "var2 = " << var2 << endl;
    cout << "sum = " << sum << endl;
    cout << "diff = " << diff << endl;
    cout << "prod = " << prod << endl;
    
 

//Question3


    string studentName;
    double labGrade, midtermGrade, finalGrade, generalScore;
    
    cout << "Enter student name: ";
    getline(cin, studentName);
    
    cout << "Enter lab grade: ";
    cin >> labGrade;
    
    cout << "Enter midterm grade: ";
    cin >> midtermGrade;
    
    cout << "Enter final grade: ";
    cin >> finalGrade;
    
   
    generalScore= (labGrade /4) + (midtermGrade *35/100) + (finalGrade *2/5);
    
    
    cout << "Name: " << studentName << endl;
    cout << "Lab: " << labGrade << endl;
    cout << "Midterm: " << midtermGrade << endl;
    cout << "Final: " << finalGrade << endl;
    cout << "General Score: " << generalScore << endl;
    

//Question4


    cout<<("*\n**\n***\n**\n*");
    
   
    return 0;
}
