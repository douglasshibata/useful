# Instalar Kubernetes no Windows
Baixar o docker desktop e habilitar o kubernetes nas configurações.

NOTE: Minimo de 4GB para conseguir rodar.
# Instalar Kubernetes no Linux`
```bash
sudo apt-get install curl -y
```
```bash
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
```
```bash
chmod +x ./kubectl
```
```bash
sudo mv ./kubectl /usr/local/bin/kubectl
```

Minikube:
 - Cria um ambiente virtualizado pronto para poder utilizar o kubernet no ambiente local
 - Necessário baixar driver de virtualização ( Eg: Virtualbox)

```bash
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v1.12.1/minikube-linux-amd64 \ && chmod +x minikube
```
```bash
sudo install minikube /usr/local/bin/
```
## Comandos
Criando um Pod com a imagem do nginx 
```bash
kubectl run nginx-pod --image=nginx:latest   
```
Eg.
```bash
kubectl run <pod-name> --image=<docker-image>   
```
Listar os nodes do kubernetes
```bash
kubectl get nodes
```

Listar os pods
```bash
kubectl get pods
```

Monitorar os Pods
```bash
kubectl get pods --watch
```

Informações sobre o POD
```bash
kubectl describe pod nginx-pod
```
Eg:
```bash
kubectl describe pod <pod-name>
```