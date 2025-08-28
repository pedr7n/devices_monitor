# ⚡ Devices_monitor - Monitoramento de Equipamentos

Aplicação Django para **monitoramento de equipamentos Meraki**, com suporte a CRUD completo e autenticação.

---

## 🚀 Funcionalidades

- 👤 **Autenticação**
  - Registro de usuários
  - Login e Logout
  - Controle de acesso às páginas

- 🏢 **Organizações**
  - Cadastro, edição, listagem e remoção
  - Campos: Nome, ID Meraki, Endereço, CNPJ, Gerente, Flags de ativação

- 📦 **Categorias**
  - Cadastro, edição, listagem e remoção
  - Campo: Nome

- 🏷️ **Marcas**
  - Cadastro, edição, listagem e remoção
  - Campo: Nome

- 🖥️ **Produtos**
  - Cadastro, edição, listagem e remoção
  - Campos: Nome, Categoria, Marca, Quantidade

- 🔌 **Devices**
  - Cadastro, edição, listagem, detalhamento e remoção
  - Campos: Produto, Organização, Categoria, Serial, MAC Address, Local, Admin, Flag de Ativação, Licença, Dias até expiração

- 🎨 **Interface**
  - Tema **dark/light** com toggle e persistência
  - Navegação intuitiva
  - Tabelas e cards responsivos

---

## 🛠️ Stack

- Python 3.13+
- Django 5.2.3
- Bootstrap 5.3
- Django Template Language (DTL)

---

## 📦 Setup

### 1. Clonar o projeto

git clone https://github.com/pedr7n/devices_monitor.git

cd devices_monitor

### 2. Ativar ambiente virtual

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Ativar dependências

pip install -r requirements.txt

### 4 Rodar migrações

python manage.py migrate

### 5 Criar super usuário

python manage.py createsuperuser


### 6 Rodar o servidor

python manage.py runserver



📖 Documentação

Decisões técnicas:

Uso de Class Based Views para CRUDs

Uso de reverse_lazy para redirecionamentos seguros

Templates padronizados com herança de base.html

Estilo responsivo com Bootstrap + variáveis de tema CSS

Autenticação nativa Django (UserCreationForm, AuthenticationForm)

Erros e melhorias registradas:

Ajustes em URLs de update/delete para incluir pk

Corrigida autenticação (logout redirecionava errado)

Melhorado design para tema escuro

👨‍💻 Autor

Pedro Ribeiro
