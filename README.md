# wsBackend-Fabrica25.2

# Buscador de Músicas Django 🎵

Este projeto é um buscador de músicas que permite aos usuários pesquisar músicas, avaliar cada música com estrelas e opiniões, e salvar músicas como favoritas. Cada avaliação e música favorita é armazenada em seu próprio modelo no banco de dados.

O projeto utiliza a API do Deezer para buscar informações detalhadas sobre as músicas.

---

## Tecnologias Utilizadas

- Python 3.x  
- Django 5.x  
- Requests (para consumir a API do Deezer)  
- HTML, CSS (para templates básicos)  

---

## Funcionalidades

1. **Página inicial (Home)**  
   - Formulário de busca de músicas.
   - Direciona para a página de resultados da pesquisa.

2. **Buscar músicas**  
   - Integração com a API do Deezer para buscar músicas pelo nome.
   - Exibe lista de músicas com informações básicas.

3. **Perfil da música**  
   - Exibe detalhes da música selecionada (nome, artista, álbum, duração, etc.).
   - Permite adicionar avaliação (estrelas + opinião).
   - Permite favoritar a música.

4. **Gerenciamento de Avaliações**  
   - Listar todas as avaliações realizadas.
   - Atualizar ou deletar avaliações existentes.
   - Cada avaliação está associada ao nome da música, número de estrelas e opinião do usuário.

5. **Gerenciamento de Favoritas**  
   - Listar todas as músicas favorited.
   - Remover músicas da lista de favoritas.
   - Cada música favorita é salva com o nome da música e do artista.

---

## Estrutura dos Modelos

### Avaliacao
- `nomemusica` → Nome da música avaliada (`CharField`, max_length=100)  
- `estrelas` → Nota em estrelas (`IntegerField`)  
- `descricao` → Opinião do usuário (`TextField`, max_length=100)  

**Observação:** As avaliações são independentes, ou seja, cada música pode ter múltiplas avaliações separadas.

### Favoritas
- `musica` → Nome da música (`CharField`, max_length=100)  
- `artista` → Nome do artista (`CharField`, max_length=80)  

**Observação:** Cada usuário (ou sessão) pode salvar suas músicas favoritas, que ficam armazenadas separadamente.

---

## Estrutura dos Formulários

### PesquisaForm
- Campo único: `pesquisa` (CharField, max_length=100)  
- Usado para capturar o termo de pesquisa do usuário na página inicial.

### AtualizarForm
- Formulário baseado no modelo `Avaliacao`.  
- Campos:
  - `nomemusica`
  - `estrelas`
  - `descricao`  
- Usado para atualizar avaliações já salvas.

---

## Estrutura das Views

- `home(request)` → Exibe o formulário de pesquisa.  
- `buscar(request)` → Busca músicas na API do Deezer com base no termo pesquisado.  
- `perfilmusica(request, pk)` → Exibe detalhes de uma música e permite avaliar.  
- `favoritar(request, pk)` → Salva ou remove uma música como favorita.  
- `listar(ListView)` → Lista todas as avaliações.  
- `listarfavoritas(ListView)` → Lista todas as músicas favoritas.  
- `deletar(DeleteView)` → Deleta uma avaliação específica.  
- `deletarfavoritas(DeleteView)` → Deleta uma música da lista de favoritas.  
- `update(UpdateView)` → Atualiza uma avaliação existente.

---

## URLs do Projeto

| URL | View | Descrição |
| --- | --- | --- |
| `/` | `home` | Página inicial com formulário de busca |
| `/busca/` | `buscar` | Página de resultados da pesquisa |
| `/music/<int:pk>` | `perfilmusica` | Página do perfil da música |
| `/favoritar/<int:pk>` | `favoritar` | Adiciona ou remove música dos favoritos |
| `/listar/` | `listar` | Lista todas as avaliações |
| `/deletar/<int:pk>` | `deletar` | Remove uma avaliação |
| `/atualizar/<int:pk>` | `update` | Atualiza uma avaliação |
| `/favorita/` | `listarfavoritas` | Lista todas as músicas favoritas |
| `/removerfav/<int:pk>` | `deletarfavoritas` | Remove música dos favoritos |

---

## Instalação

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git

2. Entre na pasta do projeto:  
cd seu-repositorio

3. Crie e ative o ambiente virtual:  
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

4. Instale as dependências:  
pip install -r requirements.txt

5. Rode as migrações do banco de dados:  
python manage.py migrate

6. Inicie o servidor:  
python manage.py runserver

7. Acesse no navegador:  
http://127.0.0.1:8000/

## Observações

- A API utilizada é a Deezer API (https://developers.deezer.com/api) para busca de músicas e informações detalhadas.
- Avaliações e músicas favoritas são armazenadas separadamente.
- Cada avaliação inclui: nome da música, estrelas e opinião do usuário.
- Cada música favorita inclui: nome da música e nome do artista.

## Futuras melhorias

- Implementar autenticação de usuários para salvar avaliações e favoritas individualmente.  
- Adicionar paginação para listas de músicas e avaliações.  
- Melhorar o layout com CSS ou frameworks como Bootstrap/Tailwind.  
- Permitir filtrar avaliações por música ou artista.  
- Adicionar suporte a imagens de capa das músicas nos templates.

## Autor

Gabriel Américo


