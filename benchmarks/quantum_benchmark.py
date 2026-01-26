import math

def grover_oracle_calls(keyspace_size):
    return math.ceil(math.pi/4 * math.sqrt(keyspace_size))
