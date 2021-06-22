## Comandos Rasa Framework

### Inicia um projeto:
```bash
	rasa init
```

### Start rasa actions (servidor):
```bash
	rasa run actions
```

### Conversa com bot no terminal:
```bash
	rasa shell
```

### Para treinar o bot:
```bash
	rasa train
```

### Iniciar conversa com bot com modelo treinado:
```bash
	rasa run -m models --enable-api --cors "*" --debug
```

### Treinar o bot em modo interativo com Rasa X:
```bash
	rasa interactive
```

### Testar histórias do Rasa usando NLU:
```bash
	rasa test
```

### Para gerar fluxo de conversa do bot:
```bash
	rasa visualize
```

### Para iniciar Rasa X (ferramenta visual de desenvolvimento do Rasa):
```bash
	rasa x
```