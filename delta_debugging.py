import re

with open('htmlPage.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
def test_string(input_string):
    pattern = r'.*<SELECT.*>'
    match = re.search(pattern, input_string)  
    if match:
        return True
    else:
        return False


def split(string, n):
    part_size = len(string) // n
    parts = [string[i:i+part_size] for i in range(0, len(string), part_size)]
    if len(parts) > n:
        parts[n-1] += parts[n]
        parts = parts[:n]
    
    deltas = parts
    
    nambas = []
    for i in range(n):
        namba = ''.join(parts[:i] + parts[i+1:])
        nambas.append(namba)
    return deltas, nambas
    

def delta_debugging(n, delta):
    if len(delta) == 1:
        return delta
    deltas, nambas = split(delta, n)
    for d in deltas:
        if test_string(d):
            return delta_debugging(2, d)
    for namba in nambas:
        if test_string(namba):
            return delta_debugging(n-1, namba)
    if n*2 <= len(delta):
        return delta_debugging(n*2, delta)
    return delta




