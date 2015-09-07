class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0 or denominator == 0:
            return '0'
            
        negFlag = (numerator < 0) != (denominator < 0)
        num = abs(numerator)
        den = abs(denominator)
        
        intpart = num // den
        remainder = num % den
        
        fracFlag = False
        if remainder > 0:
            fracFlag = True
            
        numList = list()
        seenNum = dict()
        pos = 0
        repeatPos = -1
        
        while remainder > 0:
            if remainder in seenNum:
                repeatPos = seenNum[remainder]
                break
            else:
                seenNum[remainder] = pos
                
            r = remainder // den
            remainder = remainder % den
            
            remainder *= 10
            numList.append(str(r))
            pos += 1

        if negFlag:
            ans = '-' + str(intpart)
        else:
            ans = str(intpart)
        if fracFlag:
            ans += '.'
            if repeatPos >= 0:
                ans += ''.join(numList[1:repeatPos]) + '(' + ''.join(numList[repeatPos:]) + ')'
            else:
                ans += ''.join(numList[1:])
        return ans
                