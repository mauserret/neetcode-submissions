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
        Node* curr = head;
        unordered_map<Node*, Node*> table;
        while(curr) {
            table[curr] = new Node(curr->val);
            curr = curr->next;
        }
        curr = head;

        while (curr) {
            if (curr->next) {
                table[curr]->next = table[curr->next];
            } else {
                table[curr]->next = nullptr;
            }
            if (curr->random) {
                table[curr]->random = table[curr->random];
            } else {
                table[curr]->random = nullptr;
            }
            curr = curr->next;
        }
        return table[head];
    }
};
