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

https://phoenixnap.com/kb/install-minikube-on-ubuntu





============================================================================== 
in /home/miko73/Projects/linuxdays2016-kubernetes-example/k8s




    Start local Kubernetes (k8s)

minikube start

    Deploy SimpleCrudServer into local k8s

./deploy

    Check that pods were deployed

kubectl --all-namespaces=true get pods

    Obtain ip of local k8s

minikube ip

    Ping SimpleCrudServer

curl $(minikube ip):80/persons
curl 192.168.99.100:3000/person
curl 192.168.99.100:30061/person

    Undeploy SimpleCrudServer from local k8s

./undeploy

    Stop local k8s

minikube stop

    Delete Minikube instance

minikube delete
\\\
example
============================================================================== 
https://www.youtube.com/watch?v=Oy5f8r5rCKo&t=2622s


export MINIKUBE_IP=`minikube ip`


curl $MINIKUBE_IP:30061/persons

curl -H "Content-Type: application/json" -X POST -d '{"id":"1", "name": "Jan", "surname": "Novak"}' $MINIKUBE_IP:30061/person
curl -H "Content-Type: application/json" -X POST -d '{"id":"2", "name": "Michal", "surname": "Kocandrle"}' $MINIKUBE_IP:30061/person
curl -H "Content-Type: application/json" -X POST -d '{"id":"3", "name": "Tomas", "surname": "Prenosil"}' $MINIKUBE_IP:30061/person

kubectl --namespace linuxdays scale --replicas=2 rc server

kubectl --namespace linuxdays describe pod  server-5svez

kubectl --namespace linuxdays scale --replicas=2 rc server

eval $(minikube docker-env)


curl $MINIKUBE_IP:30061/persons

kubectl --all-namespaces=true get pods

miko73@miko73-Latitude-E6420:~/Projects/linuxdays2016-kubernetes-example/k8s$ kubectl get nodes
NAME       STATUS   ROLES    AGE   VERSION
minikube   Ready    master   31m   v1.19.4


============================================================================== 
miko73@miko73-Latitude-E6420:~/Projects/linuxdays2016-kubernetes-example/k8s$ ./deploy.sh -s
Creating namespace ...
namespace/linuxdays created
Starting redis instance ...
replicationcontroller/redis created
service/redis created
Starting SimpleCrudServer instance with service...
replicationcontroller/server created
service/server created
============================================================================== 
miko73@miko73-Latitude-E6420:~/Projects/linuxdays2016-kubernetes-example/k8s$ ./deploy.sh
Creating namespace ...
namespace/linuxdays created
Starting redis instance ...
replicationcontroller/redis created
service/redis created
Starting SimpleCrudServer instance without service...
replicationcontroller/server created
============================================================================== 
kubectl --all-namespaces=true get pods
NAMESPACE     NAME                               READY   STATUS    RESTARTS   AGE
kube-system   coredns-f9fd979d6-xtfdw            1/1     Running   0          47m
kube-system   etcd-minikube                      1/1     Running   0          47m
kube-system   kube-apiserver-minikube            1/1     Running   0          47m
kube-system   kube-controller-manager-minikube   1/1     Running   0          47m
kube-system   kube-proxy-cw8nt                   1/1     Running   0          47m
kube-system   kube-scheduler-minikube            1/1     Running   0          47m
kube-system   storage-provisioner                1/1     Running   0          47m
linuxdays     redis-dfllp                        1/1     Running   0          92s
linuxdays     server-sjl2p                       1/1     Running   0          91s
============================================================================== 
to be able work with dockers install docker io 
eval $(minikube docker-env)
miko73@miko73-Latitude-E6420:~/Projects/linuxdays2016-kubernetes-example/k8s$ eval $(minikube docker-env)
miko73@miko73-Latitude-E6420:~/Projects/linuxdays2016-kubernetes-example/k8s$ docker ps -qf "name=k8s_server*"
5361394ecf98
a67a16654dbf
============================================================================== 
miko73@miko73-Latitude-E6420:~/Projects/linuxdays2016-kubernetes-example/k8s$ docker ps
CONTAINER ID        IMAGE                                       COMMAND                  CREATED             STATUS              PORTS               NAMES
5361394ecf98        kafkapre/linuxdays2016-simple-crud-server   "./server"               10 minutes ago      Up 10 minutes                           k8s_server_server-2rzqd_linuxdays_4fc4bc0f-f61e-406f-9f7e-32ec3abd42bb_0
22cb9fbab6ed        k8s.gcr.io/pause:3.2                        "/pause"                 10 minutes ago      Up 10 minutes                           k8s_POD_server-2rzqd_linuxdays_4fc4bc0f-f61e-406f-9f7e-32ec3abd42bb_0
a67a16654dbf        kafkapre/linuxdays2016-simple-crud-server   "./server"               12 minutes ago      Up 12 minutes                           k8s_server_server-sjl2p_linuxdays_b8015767-774d-48e8-8542-6e1cb093bb53_0
d82e8063e02f        43c923d57784                                "docker-entrypoint.s¿"   13 minutes ago      Up 13 minutes                           k8s_redis_redis-dfllp_linuxdays_a88e775a-14ea-4c80-ac8f-7444d1136167_0
5e25a8205ada        k8s.gcr.io/pause:3.2                        "/pause"                 13 minutes ago      Up 13 minutes                           k8s_POD_server-sjl2p_linuxdays_b8015767-774d-48e8-8542-6e1cb093bb53_0
3288aabb5baa        k8s.gcr.io/pause:3.2                        "/pause"                 13 minutes ago      Up 13 minutes                           k8s_POD_redis-dfllp_linuxdays_a88e775a-14ea-4c80-ac8f-7444d1136167_0
47c896be2e6d        bad58561c4be                                "/storage-provisioner"   About an hour ago   Up 58 minutes                           k8s_storage-provisioner_storage-provisioner_kube-system_a6043c36-3d7c-4df1-93ff-27324d3de862_0
ba3b29fe24fd        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 58 minutes                           k8s_POD_storage-provisioner_kube-system_a6043c36-3d7c-4df1-93ff-27324d3de862_0
e32fa41d026a        bfe3a36ebd25                                "/coredns -conf /etc¿"   About an hour ago   Up 59 minutes                           k8s_coredns_coredns-f9fd979d6-xtfdw_kube-system_f42142e2-f3ca-41f7-9c70-f1e69da9dc27_0
4437646ee920        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 59 minutes                           k8s_POD_coredns-f9fd979d6-xtfdw_kube-system_f42142e2-f3ca-41f7-9c70-f1e69da9dc27_0
cdd981fe80c1        635b36f4d89f                                "/usr/local/bin/kube¿"   About an hour ago   Up 59 minutes                           k8s_kube-proxy_kube-proxy-cw8nt_kube-system_136c831b-f5a6-4be5-837f-3fa4a4910bc2_0
f299f39ca5a6        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 59 minutes                           k8s_POD_kube-proxy-cw8nt_kube-system_136c831b-f5a6-4be5-837f-3fa4a4910bc2_0
0ac5984c9276        0369cf4303ff                                "etcd --advertise-cl¿"   About an hour ago   Up 59 minutes                           k8s_etcd_etcd-minikube_kube-system_606d2a090a7b8cf116483199a04c0b68_0
cf6bb0819843        4830ab618586                                "kube-controller-man¿"   About an hour ago   Up 59 minutes                           k8s_kube-controller-manager_kube-controller-manager-minikube_kube-system_6cb144f7d82285562d6fc7ed0aeee754_0
ce14256df400        14cd22f7abe7                                "kube-scheduler --au¿"   About an hour ago   Up 59 minutes                           k8s_kube-scheduler_kube-scheduler-minikube_kube-system_38744c90661b22e9ae232b0452c54538_0
87226df4c5c5        b15c6247777d                                "kube-apiserver --ad¿"   About an hour ago   Up 59 minutes                           k8s_kube-apiserver_kube-apiserver-minikube_kube-system_d2866b244c942b605989e621c99176a8_0
abe697367baa        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 59 minutes                           k8s_POD_kube-scheduler-minikube_kube-system_38744c90661b22e9ae232b0452c54538_0
a00a931df3db        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 59 minutes                           k8s_POD_kube-controller-manager-minikube_kube-system_6cb144f7d82285562d6fc7ed0aeee754_0
753c2932d378        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 59 minutes                           k8s_POD_kube-apiserver-minikube_kube-system_d2866b244c942b605989e621c99176a8_0
2ded810befaa        k8s.gcr.io/pause:3.2                        "/pause"                 About an hour ago   Up 59 minutes                           k8s_POD_etcd-minikube_kube-system_606d2a090a7b8cf116483199a04c0b68_0

============================================================================== 
install minikube on windows
https://technology.amis.nl/2017/10/24/installing-minikube-and-kubernetes-on-windows-10/

============================================================================== 
build pack io all minikube version
https://github.com/kubernetes/minikube/releases

micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
$ echo $MINIKUBE_PATH


micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
$ echo $MINIKUBE_HOME
/c/Users/micha/minikube

micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
$ cd /c/Users/micha/minikube

micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
$ ls
kubectl.exe*  minikube.exe*  minikube.ext*

micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
$ minikube start
bash: minikube: command not found

micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
$ ./minikube.exe start
* minikube v1.15.1 on Microsoft Windows 10 Pro 10.0.19042 Build 19042
  - MINIKUBE_HOME=C:/Users/micha/minikube
* Automatically selected the hyperv driver
* Downloading VM boot image ...
    > minikube-v1.15.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    > minikube-v1.15.0.iso: 181.00 MiB / 181.00 MiB [] 100.00% 8.75 MiB p/s 21s
* Starting control plane node minikube in cluster minikube
* Downloading Kubernetes v1.19.4 preload ...
    > preloaded-images-k8s-v6-v1.19.4-docker-overlay2-amd64.tar.lz4: 486.35 MiB
* Creating hyperv VM (CPUs=2, Memory=2200MB, Disk=20000MB) ...
! StartHost failed, but will try again: creating host: create: precreate: Hyper-V PowerShell Module is not available
* Creating hyperv VM (CPUs=2, Memory=2200MB, Disk=20000MB) ...
* Failed to start hyperv VM. Running "minikube delete" may fix it: creating host: create: precreate: Hyper-V PowerShell Module is not available

X Exiting due to PR_HYPERV_MODULE_NOT_INSTALLED: Failed to start host: creating host: create: precreate: Hyper-V PowerShell Module is not available
* Suggestion: Run: 'Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All'
* Documentation: https://www.altaro.com/hyper-v/install-hyper-v-powershell-module/
* Related issue: https://github.com/kubernetes/minikube/issues/9040

https://minikube.sigs.k8s.io/docs/drivers/hyperv/
Povolení technologie Hyper-V 
Otevrete konzolu PowerShell jako správce a spustte následující príkaz:

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

Používání
minikube start --driver=hyperv 
Chcete-li nastavit hyperv jako výchozí ovladac:

minikube config set driver hyperv

============================================================================== 
