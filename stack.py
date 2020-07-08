class Solution:
    def isValid(self, s: str) -> bool:
        left_stack = list()
        right_stack = list()
        left_parrem = "([{"
        right_parrem = ")]}"
        key_parrem = {"(":")", "[":"]", "{":"}"}
        if (len(s) % 2) != 0:
            return False
        elif len(s) ==0:
            return True
        for x in list(s):
            if left_parrem.find(x) != -1:
                left_stack.insert(0, x)
            else:
                if len(left_stack) == 0:
                    print('failed')

                    return False
                if key_parrem[left_stack.pop(0)] == x:
                    continue
                else:
                    print('failed')
                    return False
        if len(left_stack) == 0:
            print(s)
            return True
        else:
            print('failed')
            return False
    
    def Vaild(self, s: str) -> bool:
        pass


new = Solution()
new.isValid("[[")


