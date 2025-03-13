#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};
    
class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num >= capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        Node* temp = head;
        int poppedValue = temp->data;
        head = head->next;
        delete temp;
        num--;
        return poppedValue;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return num <=0;
    }
    void printStack() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return;
        }
    
        cout << "[ ";
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data;
            if (temp->next != nullptr) {
                cout << ", ";
            }
            temp = temp->next;
        }
        cout << " ]" << endl;
        return;
    }
    

    void increaseCapacity() {
        capacity *= 2;
        cout << "Stack capacity increased to: " << capacity << endl;
    }

    bool deleteElement(int val) {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return false;
        }
        Node* temp = head;
        Node* prev = nullptr;

        while (temp != nullptr) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    head = temp->next;
                } else {
                    prev->next = temp->next;
                }
                delete temp;
                num--;
                return true;
            }
            prev = temp;
            temp = temp->next;
        }
        cout << "Element not found in stack!" << endl;
        return false;
    }
};

int main() {
    Stack s(3);
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(12);
    s.push(121);
    s.push(17);
    
    cout << "Top element: " << s.peek() << endl;
    s.push(40); // This will trigger capacity increase
    cout << "Top element after pushing: " << s.peek() << endl;
    s.pop();
    cout << "Top element after pop: " << s.peek() << endl;
    s.deleteElement(12);
    cout << "Top element after deleting: " << s.peek() << endl;
    cout<<"All Current Stack Elements: \n ";
    s.printStack();
    return 0;
}