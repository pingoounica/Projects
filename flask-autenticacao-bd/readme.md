🔐 Sistema de Login com Flask 🚀 Sobre o projeto

Este projeto é um sistema de autenticação de usuários desenvolvido com Flask, com o objetivo de praticar conceitos de backend web, sessões, requisições HTTP e segurança básica com hash de senha.

A aplicação simula um ambiente real de login, permitindo validação de usuário, controle de sessão e acesso a uma área restrita.

⚙️ Funcionalidades

✔️ Login de usuário ✔️ Validação de credenciais com hash SHA-512 ✔️ Controle de sessão com Flask (session) ✔️ Redirecionamento para área logada ✔️ Proteção de rota (acesso apenas autenticado) ✔️ Logout do sistema ✔️ Verificação de existência de usuário via JSON (/existe)

🛠️ Tecnologias utilizadas

🐍 Python 🌐 Flask 🔐 Hashlib (SHA-512) 📦 JSON 🎨 HTML + CSS ⚡ JavaScript (Fetch API)

▶️ Como executar

Clone o repositório

git clone https://github.com/seu-usuario/seu-repo.git

Acesse a pasta

cd seu-repo

Instale as dependências

pip install flask

Execute o projeto

python app.py

Acesse no navegador

http://localhost:5000/login

📂 Estrutura do projeto 📦 projeto ┣ 📄 app.py ┣ 📂 models ┃ ┗ 📄 banco_de_dados.py ┣ 📂 templates ┃ ┣ 📄 index.html ┃ ┣ 📄 login.html ┃ ┗ 📄 area_logada.html ┣ 📂 static ┃ ┣ 📄 estilos.css ┃ ┗ 📄 verifica_usuario_fetch.js ┗ 📄 README.md

🔄 Funcionamento O usuário acessa a tela de login Insere usuário e senha A senha é convertida em hash usando SHA-512 O sistema verifica os dados no banco Se válido → cria sessão e redireciona Se inválido → exibe mensagem de erro 🧠 Aprendizados

Este projeto foi importante para reforçar:

Criação de rotas com Flask Uso de sessões (session) Integração entre frontend e backend Requisições HTTP (GET e POST) Manipulação de JSON Segurança básica com hash de senha Organização de projeto web

👩‍💻 Autora

Feito por Vanessa Pires de Almeida 🔗 https://github.com/pingoounica

⭐ Observação

Este projeto faz parte da minha evolução na área de tecnologia, com foco em desenvolvimento web backend. Novas melhorias serão adicionadas conforme avanço nos estudos.
