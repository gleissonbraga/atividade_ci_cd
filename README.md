# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Gleisson Braga
- Natalia Morandi
- Jonatas Davi

---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | atividade_ci_cd |
| Link do repositório | https://github.com/gleissonbraga/atividade_ci_cd |

### Estrutura de Diretórios

```text
atividade_ci_cd/
├── tests/
│   ├── test_calculo.py
├── .github/
│   └── workflows/
│       └── validacao.yml
├── calcular.py
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Calcula o desconto em porcentagem |
| Objetivo da funcionalidade | Calcular automaticamente a porcentagem de desconto no produto |
| Link da Issue | https://github.com/gleissonbraga/atividade_ci_cd/issues/2 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Valida o calculo da porcentagem |
| Link para o arquivo do teste | https://github.com/gleissonbraga/atividade_ci_cd/blob/tree/main/tests/test_calculo.py |

```python
from calcular import calcular_preco_final

def test_desconto_10_porcento():
    assert calcular_preco_final(100, 10) == 90

def test_sem_desconto():
    assert calcular_preco_final(200, 0) == 200

def test_desconto_50_porcento():
    assert calcular_preco_final(300, 50) == 150
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Checar Qualidade |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/gleissonbraga/atividade_ci_cd/blob/main/.github/workflows/validacao.yml |
| Link da execução | https://github.com/gleissonbraga/atividade_ci_cd/actions |

```yaml
name: Checar Qualidade

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install pytest

      - run: pytest
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 2 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 1 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro no cálculo pois a função esta sem a divisão por 100 |
| Severidade | Alta |
| Link da Issue | https://github.com/gleissonbraga/atividade_ci_cd/issues/3 |

Simulei o defeito exeutando um novo teste sem a / 100 que seria para calcular a porcentagem

```
from calcular import calcular_preco_final

def calcular_preco_final(valor, desconto):
    return valor - (valor * desconto)
```
