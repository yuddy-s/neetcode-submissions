class Solution {
public:
    int scoreOfString(string s) {
        int diff = 0;
        int holder = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i != s.length() - 1) {
                holder = std::abs((int) s[i] - (int) s[i + 1]);
                diff += holder;
            } 
        }

        return diff;
    }
};