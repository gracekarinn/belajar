class Solution(object):
    def plusOne(self, digits):
        number_string = ""
        for digit in digits:
            number_string  += str(digit)
        number = int(number_string)
        result = number + 1
        result = list(map(int, str(result)))
        
        return result