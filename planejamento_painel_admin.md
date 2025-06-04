# Planejamento do Painel Administrativo - Pachamama Ecoturismo

## Estrutura de Navegação

### 1. Login e Autenticação
- Tela de login com campos para usuário e senha
- Opção "Esqueci minha senha"
- Redirecionamento para dashboard após autenticação

### 2. Dashboard Principal
- Visão geral do site
- Estatísticas básicas (visitas, reservas pendentes)
- Acesso rápido às principais funcionalidades
- Menu de navegação lateral

### 3. Gerenciamento de Serviços
- Lista de todos os serviços com filtros e busca
- Botão para adicionar novo serviço
- Opções para editar/visualizar/excluir cada serviço
- Formulário de edição com campos para:
  - Nome do serviço (em PT, EN, ES)
  - Categoria
  - Descrição (em PT, EN, ES)
  - Preço
  - Capacidade
  - Itens inclusos
  - Informações adicionais
  - Imagem principal
  - Galeria de imagens

### 4. Gerenciamento de Imagens
- Biblioteca de imagens com visualização em grade
- Upload de novas imagens (individual ou múltiplo)
- Organização por categorias/pastas
- Opções para renomear, substituir ou excluir imagens
- Editor básico de imagens (recorte, redimensionamento)

### 5. Edição de Conteúdo
- Seleção da página a ser editada
- Editor visual WYSIWYG para textos
- Opções para formatação básica
- Inserção de imagens da biblioteca
- Visualização prévia das alterações
- Publicação das mudanças

### 6. Gerenciamento de Reservas
- Lista de reservas com status (pendente, confirmada, concluída, cancelada)
- Filtros por data, serviço e status
- Detalhes completos de cada reserva
- Opções para aprovar, rejeitar ou cancelar reservas
- Histórico de comunicações com o cliente
- Exportação de dados para CSV/Excel

### 7. Configurações
- Dados do estabelecimento
- Informações de contato
- Configurações de e-mail
- Gerenciamento de usuários e permissões
- Backup e restauração de dados

## Fluxos de Usuário

### Fluxo 1: Adicionar Novo Serviço
1. Login no painel administrativo
2. Acesso à seção "Serviços"
3. Clique em "Adicionar Novo Serviço"
4. Preenchimento do formulário com dados do serviço
5. Upload da imagem principal
6. Adição de imagens à galeria
7. Visualização prévia
8. Publicação do serviço

### Fluxo 2: Gerenciar Reservas
1. Login no painel administrativo
2. Acesso à seção "Reservas"
3. Visualização da lista de reservas pendentes
4. Seleção de uma reserva específica
5. Revisão dos detalhes da reserva
6. Aprovação ou rejeição da solicitação
7. Envio de confirmação ao cliente

### Fluxo 3: Atualizar Conteúdo da Home
1. Login no painel administrativo
2. Acesso à seção "Conteúdo"
3. Seleção da página "Home"
4. Edição dos textos usando o editor visual
5. Substituição da imagem de capa (se necessário)
6. Visualização prévia das alterações
7. Publicação das mudanças

## Permissões e Níveis de Acesso

### Administrador
- Acesso completo a todas as funcionalidades
- Gerenciamento de usuários e permissões
- Configurações do sistema
- Backup e restauração de dados

### Editor
- Gerenciamento de serviços
- Upload e organização de imagens
- Edição de conteúdo
- Visualização de reservas (sem poder de aprovação)

## Tecnologias e Implementação

### Frontend
- Framework: Bootstrap para interface responsiva
- JavaScript/jQuery para interatividade
- TinyMCE para editor de texto WYSIWYG
- Dropzone.js para upload de imagens
- DataTables para tabelas interativas

### Backend
- Flask (Python) - mantendo consistência com o site atual
- SQLAlchemy para ORM
- Flask-Login para autenticação
- Flask-WTF para formulários seguros
- Pillow para processamento de imagens

### Segurança
- Autenticação com senha criptografada
- Proteção CSRF em formulários
- Validação de dados de entrada
- Sanitização de conteúdo HTML
- Controle de sessão com timeout

## Próximos Passos
1. Configuração do ambiente de desenvolvimento
2. Implementação da estrutura básica e autenticação
3. Desenvolvimento dos módulos principais
4. Testes de funcionalidade e segurança
5. Documentação e treinamento
