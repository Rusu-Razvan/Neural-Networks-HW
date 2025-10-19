import pathlib

def read_system(path: pathlib.Path)-> tuple[list[list[float]], list[float]]:
     A = []
     B = []

     with open(path,'r') as file:
        lines = file.readlines()

        for line in lines:
          coefficients = [0,0,0]
          coefficient_index = 0
          tokens = line.split()

          free_term = tokens[-1]
          if tokens[-2] == '-':
              B.append(-float(free_term))
          else:   
              B.append(float(free_term))
          
          i = 0
          while i < len(tokens) - 1:
                if tokens[i] == '-':
                    i += 1 
                    if i < len(tokens) - 1 and (tokens[i].endswith('x') or tokens[i].endswith('y') or tokens[i].endswith('z')):
                        if tokens[i][:-1] == '':
                            coefficients[coefficient_index] = -1.0
                        else:
                            coefficients[coefficient_index] = -float(tokens[i][:-1])
                        coefficient_index += 1
                    
                    i += 1
                    continue
                        
                elif tokens[i] == '+':
                    i += 1
                    continue
                    
                elif tokens[i].endswith('x') or tokens[i].endswith('y') or tokens[i].endswith('z'):
                    if tokens[i][:-1] == '':
                        coefficients[coefficient_index] = 1.0
                    else:
                        coefficients[coefficient_index] = float(tokens[i][:-1])
                    coefficient_index += 1
                    
                i += 1

          A.append(coefficients)

     return A, B


if __name__ == "__main__":
    A, B = read_system(pathlib.Path('system.txt'))

    print(A)
    print(B)