
# Descripcion sin sentido

import numpy as np
import time 

def main():
    
    a = np.random.rand(1000000)
    b = np.random.rand(1000000)
    tic = time.time()
    x = np.dot(a,b)

    toc = time.time()
    
    print(toc-tic)
    
    # Comentario sin sentido

if __name__ == "__main__":
    main()