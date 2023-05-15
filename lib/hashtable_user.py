class Hashtable_user:
    def __init__(self, bucket_size):
        self.buckets = []
        for i in range(bucket_size):
            self.buckets.append([])

    def append(self, key, value):  # append("coucou",3)
        hash_key = hash(key)
        indice_bucket = hash_key % len(self.buckets)
        self.buckets[indice_bucket].append((key, value))

    def get(self, key):
        hash_key = hash(key)
        indice_bucket = hash_key % len(self.buckets)
        for k, v in self.buckets[indice_bucket]:
            if k == key:
                return v
        return None
