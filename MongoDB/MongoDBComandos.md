## Comandos mongoDB 
### para filtrar:
    {coluna:"item"}
filtrar por numero igual ou maior que 21 e menor que 70
    {coluna:{"$gte":21,"$lt":70} }
### para na linha de comando do mongo:
    ver as databases:
    ```bash
        show dbs   
    ```
    ver as tabelas :
        ```bash
         show collections 
        ```
    ver o conteúdo das tabelas:
        ```bash
         db.nomeDaTabela.find().pretty() 
        ```
    ver um conteúdo especifico da tabela:
        ```bash
         db.nomeDaTabela.find({coluna:"valor",coluna2:"valor"}) 
        ```
    ver um conteúdo da tabela que está em array:
        ```bash
         db.nomeDaTabela.find({"coluna.array.coluna":"valor"}) 
        ```
    para inserir dados na tabela:
        ```bash
         db.nomeDaTabela.insertOne({campo:"valor",campo:valor}) 
        ```
    para atualizar um dado na tabela:
        ```bash
         db.nomeDaTabela.updateOne({campo:"valor"},{$set:{campo:"valor"}}) 
        ```
    para atualizar um dado na tabela e incrementar o seu valor:       
        ```bash
        db.nomeDaTabela.updateOne({campo:"valor"},{$inc:{campo:"valor"}}) 
        ```
    para deletar um dado na tabela:       
        ```bash
         db.nomeDaTabela.deleteOne({_id:ObjectId("")}); 
        ```
    para deletar varios dados de uma tabela com campos em comum:
        ```bash
        db.nomeDaTabela.deleteMany({campo:valor}); 
        ```
    para procurar um valor que está na tabela com o operador $in:
        ```bash
         db.nomeDaTabela.find({campo:{$in:["valor","valor"]}}) 
        ```
    para procurar por tipo de dados armazenado:
        ```bash
         db.movies.find({campo: {$type: "double"}}).pretty() 
        ```
    para verificar se tal campo existe na tabela:       
        ```bash
         db.data.find({atmosphericPressureChange: {$exists: false}}).count()   
        ```
