# Edu-Connect API

## Descrição

A Edu-Connect API é um projeto MVP que oferece funcionalidades para gerenciar cursos e alunos. Esta API foi desenvolvida em Flask e utiliza o SQLAlchemy como ORM (Object-Relational Mapping) para interagir com um banco de dados SQLite.

## Pré-requisitos

Certifique-se de que você tenha o Python e o pip instalados em sua máquina.

## Instalação

1. Clone este repositório:

```bash
git clone git@github.com:marmota-alpina/Edu-Connect-API.git
```
Ou 

```bash
git clone https://github.com/marmota-alpina/Edu-Connect-API.git
```

2. Navegue até o diretório do projeto:

```bash
cd Edu-Connect-API
```

3. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

4. Ative o ambiente virtual (Linux/macOS):

```bash
source venv/bin/activate
```

Ative o ambiente virtual (Windows):

```bash
venv\Scripts\activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

Após a instalação, você pode iniciar a aplicação Flask com o seguinte comando:

```bash
flask run
```

A aplicação será executada localmente em `http://127.0.0.1:5000/`.

## Endpoints da API

### Courses (Cursos)

- `POST /courses/`: Crie um novo curso.
  - Este endpoint permite que você crie um novo curso com os dados fornecidos.
  - Request Body:
    - name (string): Nome do curso.
    - description (string): Descrição do curso.
    - course_load (int): Carga horária do curso.
  - Respostas:
    - 201 Created: Curso criado com sucesso.
    - 409 Conflict: Se o nome do curso já estiver em uso.

- `GET /courses/`: Obtenha uma lista de cursos.
  - Este endpoint retorna uma lista de todos os cursos disponíveis.
  - Respostas:
    - 200 OK: Lista de cursos.

- `PUT /courses/{id}`: Atualize os detalhes de um curso específico.
  - Este endpoint permite que você atualize os detalhes de um curso identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do curso.
  - Request Body:
    - name (string): Nome atualizado do curso.
  - Respostas:
    - 200 OK: Detalhes do curso atualizados.
    - 404 Not Found: Se o curso com o ID fornecido não existir.

- `GET /courses/{id}`: Obtenha detalhes de um curso específico.
  - Este endpoint retorna os detalhes de um curso específico identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do curso.
  - Respostas:
    - 200 OK: Detalhes do curso.
    - 404 Not Found: Se o curso com o ID fornecido não existir.

- `DELETE /courses/{id}`: Exclua um curso específico.
  - Este endpoint permite que você exclua um curso específico identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do curso.
  - Respostas:
    - 204 No Content: Curso excluído com sucesso.
    - 404 Not Found: Se o curso com o ID fornecido não existir.
    - 409 Conflict: Se o nome do curso já estiver em uso.

### Students (Alunos)

- `GET /students/`: Obtenha uma lista de alunos.
  - Este endpoint retorna uma lista de todos os alunos disponíveis.
  - Respostas:
    - 200 OK: Lista de alunos.

- `PUT /students/{id}`: Atualize os detalhes de um aluno específico.
  - Este endpoint permite que você atualize os detalhes de um aluno identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do aluno.
  - Request Body:
    - name (string): Nome atualizado do aluno.
    - course_id (int): ID do curso atualizado ao qual o aluno pertence.
  - Respostas:
    - 200 OK: Detalhes do aluno atualizados.
    - 400 Bad Request: Se o ID do curso não existir.
    - 404 Not Found: Se o aluno com o ID fornecido não existir.

- `GET /students/{id}`: Obtenha detalhes de um aluno específico.
  - Este endpoint retorna os detalhes de um aluno específico identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do aluno.
  - Respostas:
    - 200 OK: Detalhes do aluno.
    - 404 Not Found: Se o aluno com o ID fornecido não existir.

- `DELETE /students/{id}`: Exclua um aluno específico.
  - Este endpoint permite que você exclua um aluno específico identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do aluno.
  - Respostas:
    - 204 No Content: Aluno excluído com sucesso.
    - 404 Not Found: Se o aluno com o ID fornecido não existir.

- `POST /courses/{id}/enroll`: Matricule um aluno em um curso.
  - Este endpoint permite que você matricule um aluno em um curso específico identificado pelo seu ID.
  - Parâmetros:
    - id (int): ID exclusivo do curso.
  - Request Body:
    - name (string): Nome do aluno.
    - email (string): E-mail do aluno.
  - Respostas:
    - 201 Created: Aluno matriculado com sucesso.
    - 404 Not Found: Se o curso com o ID fornecido não existir.
    - 409 Conflict: Se o aluno já estiver matriculado no curso.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para o desenvolvimento deste projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para a sua contribuição:

```bash
git checkout -b feature/sua-feature
```

3. Faça suas alterações e commit:

```bash
git commit -m "Adicionando nova funcionalidade"
```

4. Faça um push para o seu fork:

```bash
git push origin feature/sua-feature
```

5. Crie um pull request para este repositório.

## Licença

Este projeto é distribuído sob a licença MIT. Para mais informações, leia o arquivo [LICENSE](LICENSE.txt).

