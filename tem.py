class Solution(object):
    def isPalindrome(self, s):
        new = {}
        new2 = ''
        
        for i in range(65,122) :
            new[chr(i)] = []
        for j in range(len(s)):
            if s[j] in new :
                # new2 =''.join(s[j]).lower()  both true
                new2 += s[j].lower()

        sorted_s = ''.join(sorted(s))   # sorts the characters in 's'
        print(new2)
        print(sorted_s,'this is')
        print(new2 == new2[::-1])


        # print(new)
s = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s)