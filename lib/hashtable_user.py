import json
import sys
sys.path.append("..") # Adds higher directory to python modules path.
class Hashtable_user: 
  def __init__(self, bucket_size):
    self.bucket_size = bucket_size
    self.buckets = []
    for i in range(bucket_size):
      self.buckets.append([])
    self.load()

  def append(self,key,value): # append("coucou",3)
    hash_key = hash(key)
    print(len(self.buckets))
    indice_bucket = hash_key % len(self.buckets)
    self.buckets[indice_bucket].append((key,value))
    self.save()

  def get(self, key):
    hash_key = hash(key)
    print(len(self.buckets))
    indice_bucket = hash_key % len(self.buckets)
    for k,v in self.buckets[indice_bucket]:
      if k == key:
        return v
    return None
  
  def clear(self):
    self.buckets = []
    for i in range(len(self.buckets)):
      self.buckets.append([])
    self.save()
  
  def save(self):
        with open('storage/hashtable.json', 'w') as f:
            json.dump(self.buckets, f)

  def load(self):
      try:
          with open('storage/hashtable.json', 'r') as f:
              self.buckets = json.load(f)
      except FileNotFoundError:
          pass