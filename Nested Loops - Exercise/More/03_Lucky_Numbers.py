N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if (i + j) == (k + l) and N % (i + j) == 0 and (int(str(f'{i}{j}{k}{l}'))) < N * 1000:
                    print(f'{i}{j}{k}{l}', end=' ')