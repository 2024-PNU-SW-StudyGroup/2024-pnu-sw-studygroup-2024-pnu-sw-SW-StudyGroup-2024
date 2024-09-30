while True:
    N = str(input())
    if N == '0':
        break
    
    N_lst = list(N)
        
    if N_lst == N_lst[::-1]:
        print('yes')
    else:
        print('no')