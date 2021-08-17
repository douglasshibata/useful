# CRON
 * O Cron é um programa daemon de agendamento de trabalhos baseado em tempo
 * O Cron executa em segundo plano e as tarefas agendadas com o cron, conhecidas como “cron jobs” (trabalhos do cron), são executadas automaticamente, o que torna o cron útil para automatizar tarefas relacionadas à manutenção.


## Instalando o CRON no Ubuntu

```bash
sudo apt install cron
```


### Ativando o cron

```bash
sudo systemctl enable cron
```

### Como Funciona ?

* Os trabalhos do cron são registrados e gerenciados em um arquivo especial conhecido como **crontab**
* Cada perfil de usuário no sistema pode ter seu próprio arquivo crontab - onde o usuário poderá agendar trabalhos - que fica armazenado em ***/var/spool/cron/crontabs/***

#### Exemplo 
```bash
==minute== ==hour== ==day_of_month== ==month== ==day_of_week== ==command_to_run==
```
* Essa Expressão executa o comando **curl**, toda terça feira as 17hs(5:30pm)
```bash
30 17 * * 2 curl http://www.google.com
```
