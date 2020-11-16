kuberneties (kiberneties)
docker

Master Node

  api serever busines logika, rozsire pluginama
  komunikuje se vsim a stavy si uklada persistance
  dale se schedulerem , kde je ulozeno kde jsou nodes, 
  kam se maji nove kontejnery nainstalovat

  condtrol manager = demon set a replication  controlery
  
  ETCD  distribuovana databze k ulozeni configurace
  
  kubectl klient pro komunikace is api 

  Worker Nodes
    on worker nody are deplyed aplications

worker se nastartuje a zaregistruje se na master node.
kubelet (kiblet) bez na vsech worker nodech
podspec definuje, kde ma bezet container, jake node, porty atd.
kub-porxy bezi na kazdem workeru (routovani a networking k servisam)

vsechno tosluzi ke nasazovani PODu 

kam se kuberneties instaluje
AVS ?
beremetal servery

vytvoreni service
apyserver -> kube-proxy definuje IP tales a vytvori ServiceIP -> ta ma notvirane Pody
clien jde pres ServiceIP na Pody
Ty pody jsou jednotlivé linux containery pro jednotlivé user requesty ??

Dalsi features on kuberneties NFS, Flocker, 
DNS kdyz si to nakonfigurujeme muzeme tu mit hostnames.
namespaces.
  dodeleni kdyz se nasazuje vice domen aplikace

Daemon set pro generovani démonu
Jobs pro definici uloh
secrets pro uchovani hesel
config maps pro definovani konfigurace
limitovani resourcu pamet a cpu pro jednotlive PODy

Install if
  Minikube = run VM
  Kubeadm  = install k8s na PC
  
alternativy pro kubernetes
  Mesos
  Docker Swarm
https://github.com/kafkapre/linuxdays2016-kubernetes-example
============================================================================== 
ukazka na Minikube
minikube start
kubectl get nodes
kubectl --all-namespaces=true get pods

nasazeni aplikace 
./deploy.sh


troubleshooting
  kubectl --namespace=linuxdays describe pod servr-nnuov

sesazeni
  ./undeploy.sh 

export MINIKUBE_IP='minikube ip'

nasazeni se servisou

./deploy.sh -s

kubectl --namespace=linuxdays scale --replcas=2 rc server

prepnuti do dockeru
eval $(minikube docker-env)
docker ps
vypise kontejnery

./kill-container.sh
zabije jden pod a snazi se prihlasit get ne service.
============================================================================== 
HOW to install minikube

https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-with-curl-on-linux




curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.19.0/bin/windows/amd64/kubectl.exe
