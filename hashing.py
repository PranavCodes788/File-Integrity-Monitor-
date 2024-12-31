import hashlib
import os

def compute_file_hash(file_path, algorithm='sha256'):

   #computes the hasing of a file with a specified algorithm.

    hasher = hashlib.new(algorithm)

    # Reads the file into chunks to avoid loading all the memory
    # at once.

    with open(file_path, 'rb') as f:
        chunk = f.read(8192)
        while chunk:
            hasher.update(chunk)
            chunk = f.read(8192)
    return hasher.hexdigest()

def compare_file_hashes(old_hash, new_hash):

    # Compares two hashstrings. Returns true if they are the same, and false otherwise.

    return old_hash == new_hash
