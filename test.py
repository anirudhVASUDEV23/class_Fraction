from fraction import Fraction

if __name__ == "__main__":
    # Instantiate two Fraction objects
    x = Fraction(5, 6)
    y = Fraction(1, 2)
    z = Fraction(3, 4)
    w = Fraction(2, 3)
    
    print("--- Arithmetic Operations ---")
    print(f"Fraction x: {x}")
    print(f"Fraction y: {y}")
    print(f"Fraction z: {z}")
    print(f"Fraction w: {w}")

    # Addition
    print(f"\n{x} + {y} = {x + y}")
    
    # Subtraction
    print(f"{x} - {y} = {x - y}")
    
    # Multiplication
    print(f"{x} * {y} = {x * y}")
    
    # True Division
    print(f"{x} / {y} = {x / y}")
    
    # Floor Division
    # This will return an integer
    print(f"{x} // {w} = {x // w}")
    
    # Modulo
    print(f"{x} % {w} = {x % w}")

    # Power (assuming integer exponent)
    print(f"{w} ** 2 = {w ** 2}")
    
    print("\n--- Comparison Operations ---")
    # Equality
    print(f"{x} == {Fraction(10, 12)} is {x == Fraction(10, 12)}") # Demonstrates equality of simplified and non-simplified
    print(f"{x} != {y} is {x != y}")

    # Less than and Greater than
    print(f"{x} < {y} is {x < y}")
    print(f"{x} > {y} is {x > y}")

    # Less than or equal to and Greater than or equal to
    print(f"{x} <= {y} is {x <= y}")
    print(f"{x} >= {y} is {x >= y}")
    print(f"{x} >= {Fraction(10, 12)} is {x >= Fraction(10, 12)}")