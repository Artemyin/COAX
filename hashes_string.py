"""There is string s = "Python Bootcamp". Write the code that hashes string."""
import hashlib
s = "Python Bootcamp"

def hash_string(string, hash_function=None):
    """Hashes input string.
    string -- string you want to hash
    hash_function -- hash function from hashlib (default None),
    if not specified uses str().__hash__() method.
    Guaranteed algorithms: 'sha3_512', 'sha3_384', 'sha384', 'sha224',
    'blake2b', 'sha3_224', 'sha256', 'md5', 'blake2s',
    'sha1', 'sha512', 'sha3_256' according to hashlib
    Not implemented algorithms: 'shake_128', 'shake_256'
    """
    
    if not isinstance(string, str):
        raise TypeError("takes string only")
        
    if hash_function is None:
        return string.__hash__()
        
    if hash_function not in hashlib.algorithms_guaranteed:
        raise ValueError("This algorithm is not guaranteed")
        
        
    if hash_function in ('shake_128', 'shake_256'):
        raise NotImplementedError("This algorithms have not supports, yet")
      
    hash = getattr(hashlib, hash_function)() 
    hash.update(string.encode())
    return hash.hexdigest()

#print(hash_string(s, "shake_256"))
#print(hash_string(s, "md5"))
