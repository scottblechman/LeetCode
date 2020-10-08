def roman_to_integer(s: str) -> int:
    total = 0
    skip_next = False
    for i in range(0, len(s)):
        if skip_next:
            skip_next = False
        else:
            c = s[i]
            c_next = ''
            if i + 1 < len(s):
                c_next = s[i + 1]
            if c == 'M':
                total += 1000
            elif c == 'D':
                total += 500
            elif c == 'C':
                if c_next not in ['D', 'M']:
                    total += 100
                elif c_next == 'D':
                    total += 400
                    skip_next = True
                elif c_next == 'M':
                    total += 900
                    skip_next = True
            elif c == 'L':
                total += 50
            elif c == 'X':
                if c_next not in ['L', 'C']:
                    total += 10
                elif c_next == 'L':
                    total += 40
                    skip_next = True
                elif c_next == 'C':
                    total += 90
                    skip_next = True
            elif c == 'V':
                total += 5
            elif c == 'I':
                if c_next not in ['V', 'X']:
                    total += 1
                elif c_next == 'V':
                    total += 4
                    skip_next = True
                elif c_next == 'X':
                    total += 9
                    skip_next = True
    return total
