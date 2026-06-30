from calcular import calcular_preco_final

def test_desconto_10_porcento():
    assert calcular_preco_final(100, 10) == 90

def test_sem_desconto():
    assert calcular_preco_final(200, 0) == 200

def test_desconto_50_porcento():
    assert calcular_preco_final(300, 50) == 150