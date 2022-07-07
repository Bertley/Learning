'''
Given a string of length n consisting of digits [0-9], count the number of ways the given string can be split
into prime numbers. The digits must remain in the order given and the entire string must be used. Each
number must be in the range 2 to 10^6 inclusive, and may not contain leading zeros. Since the answer can
be large, return the answer modulo (10^9 + 7).

Note: The initial string does not contain leading zeros.

Example
s = "11375"
This string can be split into primes 3 different ways: [11, 37, 5], [11,3, 7, 5], [113, 7, 5]

Function Description
Complete the function countPrimeStrings in the editor below.

countPrimeStrings has the following parameter(s):
- string s: a string of digits
Return
- int: the number of ways the string can be split into primes, modulo 1000000007, (10^9 +7)

Constraints
- 1 ≤ length of s ≤ 10^5
'''


# https://math.stackexchange.com/questions/3031327/all-possible-ways-to-split-a-number

class Solution:

    def countPrimeStrings(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """

        def isPrime(number) -> bool: 
            """A really simplistic way of identifying a prime number"""
            if number < 2: 
                return False
            
            for i in range(2, number):
                if (number % i == 0): 
                    return False

            return True

        def splitNum(number) -> list:
            '''
            ---- Binomial theorem --- 

            When you have a sequence of 𝑛 numbers, you can 𝑛−1 slots to make cuts. So we need to know all the ways we can choose 0 cuts out if it, then 1 cut, 2 cuts, etc
            Split a string into all possible combinations using binary numbers
            Look at the cuts as a binary number where each digit i of the number indicates if we cut between digit i and i+1 in the real number.
            for example:
                12345 would be 0000.
                12,345 would be 0100.
                
            Now,for a number of size n our binary number would be of size n-1, how many unique values can a n-1 digits binary number represent? 2^(n-1)
            
            def getSplits(myciphers):
                comb=[]    
                for split in [p for p in itertools.product([0,1], repeat=4)]:            
                    tsplit=[]
                    tsplit.append(myciphers[0])
                    for c,s in zip(myciphers[1:],split):      
                        if s == 1:
                            tsplit.append("-")
                        tsplit.append(c)

                    comb.append("".join(tsplit))
                return comb
            '''
            output = []
            i = 0
    
            while i < 2 ** (len(number) - 1):
                # Get the binary representation of i as a string without the 0b prefix
                b = str(bin(i))[2:]
                # Add 0s to the front of the binary representation 
                # to make it the same length as the given number
                b = "0" * (len(s) - len(b) - 1) + b + "0"
                # Initiale p to loop through the given number
                p = 0 
                # Initialize r to an empty string to help build the possible combinations
                r = ""

                # Loop through the given number
                # If the binary representation of i has a 1 at position p, add a digit to the string 
                # where the digit is the digit at position p of the given number
                while p < len(number): 
                    r += number[p]

                    if b[p] == "1":
                        r += ","

                    p += 1

                # Split the string into a list of numbers
                nums = [int(x) for x in r.split(",")]
                output.append(nums)
                i += 1
                
            return output

        def isAllPrimes(nums) -> bool:
            '''
            Return True if all numbers in the set are Prime numbers
            '''

            for num in nums: 
                if not isPrime(num): 
                    return False 

            return True
        
        # initialize the count to track of the number of ways the string can be split into primes
        count = 0
        # split the string into all possible combinations
        splits = splitNum(s)

        # iterate through each combination and check if it is a prime number
        for num in splits: 
            if isAllPrimes(num): 
                count += 1

        return count % (10**9 + 7)

def main(): 
    s = "137117"
    solutioon = Solution()
    print(solutioon.countPrimeStrings(s))

if __name__ == "__main__":
    main() 