import re

def load_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def test_string(input_string):
    return bool(re.search(r'<SELECT.*>', input_string))

def split(string, n):
    part_size = len(string) // n
    parts = [string[i:i+part_size] for i in range(0, len(string), part_size)]
    nambas = [''.join(parts[:i] + parts[i+1:]) for i in range(n)]
    return parts, nambas
    

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


def main():
    filepath = 'htmlPage.txt'  
    file = load_file(filepath)
    result = delta_debugging(2, file)
    print(result)

if __name__ == "__main__":
    main()


