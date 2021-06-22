## Comandos Django

### Inicia um projeto:
```bash
	django-admin startproject NAME .
```

### Inicia uma nova aplicação:
```bash
   django-admin startapp NAME 
```

### Start o servidor:
```bash
   python manage.py runserver 
```

### Criar um super usuário para acessar tela administrativa:
```bash
   python manage.py createsuperuser 
```

### Atualizar as migrations do projeto django:
```bash
    python manage.py makemigrations
```

### Aplicar as mudanças da migration:
```bash
   python manage.py migrate 
```

### Ajuda interativa do Django:
```bash
   python manage.py shell 
```