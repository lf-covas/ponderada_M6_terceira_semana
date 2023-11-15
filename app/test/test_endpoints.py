import requests

def test_criar_animal():
    dados_animal = {
        'nome': 'Leão',
        'especie': 'Felino',
        'recinto': 'Savana'
    }

    response = requests.post('http://127.0.0.1:5000/criar_animal', json=dados_animal)

    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Animal Leão da espécie Felino criado com sucesso!'


def test_criar_recinto():
    nome_recinto = {'nome':'Inteli'}

    response = requests.post('http://127.0.0.1:5000/criar_recinto', json = nome_recinto)

    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Recinto Inteli criado com sucesso!'


def test_alimentar_animal():
    dados_animal = {
        'nome_recinto': 'Inteli',
        'nome_animal': 'Tony'
    }

    response = requests.post('http://127.0.0.1:5000/alimentar_animal', json = dados_animal)

    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Animal Tony do recinto Inteli alimentado com sucesso!'

def test_adicionar_visitas():
    response = requests.post('http://127.0.0.1:5000/recebe_visitas')

    assert response.status_code == 200
    assert response.json()['mensagem'] == 'Sem condições de receber visitas'