shakesP = ''
with open('t8.shakespeare.txt', 'r') as f_var:
    shakesP = shakesP + f_var.read()

    lines = shakesP.split('\n')
    line_count = len(lines)
print(f'Line Count: {line_count}')