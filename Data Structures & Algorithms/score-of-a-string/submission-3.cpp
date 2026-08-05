class Solution {
public:
    int scoreOfString(string s) {
        int diff = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i != s.length() - 1) {
                diff += std::abs((int) s[i] - (int) s[i + 1]);
            } 
        }

        return diff;
    }
};