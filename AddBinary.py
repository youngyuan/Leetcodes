class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = 0
        r = []
        while i < len(a) or i < len(b):
            bit = carry
            if i < len(a) and a[ -1 - i] == '1':
                bit += 1
            if i < len(b) and b[ -1 - i] == '1':
                bit += 1
            if bit < 2:
                r.append(str(bit))
                carry = 0
            else:
                r.append(str(bit % 2))
                carry = 1
            i += 1
        if carry == 1:
            r.append('1')
        return ''.join(r[::-1])

s=Solution()
print(s.addBinary('1111','1111'))