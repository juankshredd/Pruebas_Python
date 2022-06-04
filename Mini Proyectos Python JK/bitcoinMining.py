from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'* prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Listo parce!!! BitCoins minados por valor nonce de: {nonce}")

    raise BaseException(f"No se mino nada en {MAX_NONCE} intentos")

if __name__ == '__main__':
    transactions = '''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    # entre mas dificultad mayor tiempo toma mminar
    difficulty = 4
    import time
    start = time.time()
    print("empezar a minar")
    new_hash = mine(5, transactions, '', difficulty)
    total_time = str((time.time() - start))
    print(f"Terminando de minar, tiempo de minado: {total_time} segundos")
    print(new_hash)