def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # inicializa o array de resposta com 1s
    
    # --- Passo 1: calcular prefixo (produto da esquerda) ---
    prefix = 1
    for i in range(n):
        answer[i] = prefix      # produto de todos elementos à esquerda de i
        prefix *= nums[i]        # atualiza prefixo acumulado
    
    # --- Passo 2: multiplicar pelo sufixo (produto da direita) ---
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix     # multiplica pelo produto da direita
        suffix *= nums[i]       # atualiza sufixo acumulado
    
    return answer
