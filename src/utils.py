import time


def get_snippet(text, length=200):
    
    Returns the first `length` characters of a document.
    
    return text[:length].replace("\n", " ").strip()


def timer(func):
    
    Decorator to measure execution time of functions.

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper
