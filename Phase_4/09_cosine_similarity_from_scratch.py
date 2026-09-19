import math

def dot_product(a, b):
    return sum(x*y for x, y in zip(a, b))

def magnitude(v):
    return math.sqrt(sum(x*x for x in v))

def cosine_similarity(a, b):
    # Hinglish: Direction similarity compare kar rahe hain.
    denominator = magnitude(a) * magnitude(b)
    return 0 if denominator == 0 else dot_product(a, b) / denominator

print(cosine_similarity([1,2,3], [2,4,6]))
