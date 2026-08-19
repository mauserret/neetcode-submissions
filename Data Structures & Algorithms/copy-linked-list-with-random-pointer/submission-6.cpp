/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> table;
        Node* curr = head;
        while(curr){
            table[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        while(curr){
            Node* copy = table[curr];
            copy->next = table[curr->next];
            copy->random = table[curr->random];
            curr = curr->next;
        }
        return table[head];

    }
};

