for i in range(2):
    p = False
    if i == 1:
        p = True
        i = 0
    for j in range(2):
        q = False
        if j == 1:
            q = True
            j = 0
        for k in range(2):
            r = False
            if k == 1:
                r = True
                k = 0
            print(p,q,r,(not(p and q)) or r)