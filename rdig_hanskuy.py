def invert_bits(b):
    if len(b) >= 2 and b[1] == 'b':
        b = b[2:]
    return ''.join('1' if a == '0' else '0' for a in b)

def s1scomp_toi(b):
    if b[0] == '1':
        return int(invert_bits(b), 2) * -1
    return int(b, 2)

def s2scomp_toi(b):
    if b[0] == '1':
        return s1scomp_toi(b) - 1
    return int(b, 2)

def sm_toi(b):
    if b[0] == '1':
        return int(b[1:], 2) * -1
    return int(b, 2)

def bool_alg(a, b, op):
    a = int(a, 2)
    b = int(b, 2)
    res = 0
    op.strip().lower()
    if op == 'and':
        res = a & b
    elif op == 'or':
        res = a | b
    elif op == 'xor':
        res = a ^ b
    elif op == 'nor':
        res = ~(a | b)
    elif op == 'nand':
        res = ~(a & b)
    elif op == 'xnor':
        res = ~(a ^ b)
    return res

def bool_not(b):
    return ~int(b, 2)