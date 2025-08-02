import math

class Fraction:
    def __init__(self,n,d):
        if d==0:
            raise ZeroDivisionError
        self.num=n
        self.den=d
    
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        new_num=self.num*other.den+self.den*other.num
        new_den=self.den*other.den
        common_divisor = math.gcd(new_num, new_den)
        simplified_num = new_num // common_divisor
        simplified_den = new_den // common_divisor
        return Fraction(simplified_num, simplified_den)
    
    def __sub__(self,other):
        new_num=self.num*other.den-self.den*other.num
        new_den=self.den*other.den
        common_divisor = math.gcd(new_num, new_den)
        simplified_num = new_num // common_divisor
        simplified_den = new_den // common_divisor
        return Fraction(simplified_num, simplified_den)
    
    def __mul__(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den
        common_divisor = math.gcd(new_num, new_den)
        simplified_num = new_num // common_divisor
        simplified_den = new_den // common_divisor
        return Fraction(simplified_num, simplified_den)
    
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        common_divisor = math.gcd(new_num, new_den)
        simplified_num = new_num // common_divisor
        simplified_den = new_den // common_divisor
        return Fraction(simplified_num, simplified_den)

    # Magic method for floor division (//)
    def __floordiv__(self, other):
        # Calculate the result of true division
        true_division_result = self.__truediv__(other)
        # Return the floor of the result, which is an integer
        return true_division_result.num // true_division_result.den

    # Magic method for modulo (%)
    def __mod__(self, other):
        # The remainder of a/b % c/d is (a/b - (a/b // c/d) * c/d)
        floor_division = self.__floordiv__(other)
        product = other.__mul__(Fraction(floor_division, 1))
        return self.__sub__(product)

    # Magic method for power (**)
    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError("Power must be an integer")
        
        new_num = self.num ** other
        new_den = self.den ** other
        
        # Simplify the result
        common_divisor = math.gcd(new_num, new_den)
        simplified_num = new_num // common_divisor
        simplified_den = new_den // common_divisor
        
        return Fraction(simplified_num, simplified_den)
    
    def __eq__(self, other):
        # a/b == c/d  is  a*d == c*b
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        # a/b != c/d  is  a*d != c*b
        return self.num * other.den != other.num * self.den
    
    def __lt__(self, other):
        # a/b < c/d is a*d < c*b
        return self.num * other.den < other.num * self.den
        
    def __gt__(self, other):
        # a/b > c/d is a*d > c*b
        return self.num * other.den > other.num * self.den
        
    def __le__(self, other):
        # a/b <= c/d is a*d <= c*b
        return self.num * other.den <= other.num * self.den
        
    def __ge__(self, other):
        # a/b >= c/d is a*d >= c*b
        return self.num * other.den >= other.num * self.den

