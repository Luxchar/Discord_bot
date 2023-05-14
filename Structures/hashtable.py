class Hashtable:
    def __init__(self, elements): # elements is a list of tuples (key, value)
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None

# capitals = [
#   ('France', 'Paris'),
#   ('United States', 'Washington D.C.'),
#   ('Italy', 'Rome'),
#   ('Canada', 'Ottawa')
# ]
# hashtable = Hashtable(capitals)

# print(f"The capital of Italy is {hashtable.get_value('Italy')}")