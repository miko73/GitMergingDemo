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
#! /bin/bash

currentDir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
source $currentDir/namespace.conf
echo "Creating namespace ..."
sed -e "s/%namespaceName%/$namespace/" $currentDir/namespace.yaml | kubectl create -f -
echo "Starting redis instance ..."
kubectl --namespace=$namespace create -f $currentDir/redis.yaml
case "$1" in
-s )
   echo "Starting SimpleCrudServer instance with service..."
   kubectl --namespace=$namespace create -f $currentDir/simpleCrudServer-with-service.yaml
   ;;
* )
   echo "Starting SimpleCrudServer instance without service..."
   kubectl --namespace=$namespace create -f $currentDir/simpleCrudServer.yaml
   ;;
esac





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
miko start
miko minikube start

 /home/miko73/Projects/linuxdays2016-kubernetes-example/k8s




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


export MINIKUBE_IP='minikube ip'


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

PS C:\Users\micha\minikube > minikube version

minikube version: v1.15.1
commit: 23f40a012abb52eff365ff99a709501a61ac5876




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

miko minikube start

micha@DESKTOP-O9QT0O1 MINGW64 ~/minikube
export MINIKUBE_HOME=/c/Users/micha/minikube
set MINIKUBE_HOME=C:\Users\micha\minikube

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

miko minikube start
How to start

Otevrete konzolu PowerShell jako správce a spustte následující príkaz:

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

in same terminal

PS C:\Users\micha\minikube> ./minikube start
* minikube v1.15.1 on Microsoft Windows 10 Pro 10.0.19042 Build 19042
* Automatically selected the hyperv driver
* Downloading VM boot image ...
    > minikube-v1.15.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    > minikube-v1.15.0.iso: 181.00 MiB / 181.00 MiB [] 100.00% 6.11 MiB p/s 30s
* Starting control plane node minikube in cluster minikube
* Downloading Kubernetes v1.19.4 preload ...
    > preloaded-images-k8s-v6-v1.19.4-docker-overlay2-amd64.tar.lz4: 486.35 MiB
* Creating hyperv VM (CPUs=2, Memory=2200MB, Disk=20000MB) ...
* Preparing Kubernetes v1.19.4 on Docker 19.03.13 ...
* Verifying Kubernetes components...
* Enabled addons: storage-provisioner, default-storageclass

! kubectl.exe is version 1.8.0, which may have incompatibilites with Kubernetes 1.19.4.
  - Want kubectl v1.19.4? Try 'minikube kubectl -- get pods -A'
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default



miko minikube
cd /c/Users/micha/minikube

Používání
./minikube.exe start --driver=hyperv

Chcete-li nastavit hyperv jako výchozí ovladac:

minikube config set driver hyperv

running
PS C:\Users\micha\minikube> ./minikube dashboard
* Enabling dashboard ...
* Verifying dashboard health ...
* Launching proxy ...
* Verifying proxy health ...
* Opening http://127.0.0.1:52634/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...

./minikube addons enable ingress


./kubectl run my-nginx –image=nginx –port=80


==============================================================================
miko docker
PS C:\users\micha\Projects\docker_python_flask> docker image ls
REPOSITORY                           TAG                                              IMAGE ID            CREATED              SIZE
docker_python_flask                  v1                                               d268a113317f        About a minute ago   885MB                                                                                hello-python                         latest                                           c052afb57ddf        14 hours ago         885MB
dockerpython                         latest                                           27e26a53b519        26 hours ago         941MB
docker101tutorial                    latest                                           c3a0f71c19df        26 hours ago         27.2MB
alpine/git                           latest                                           76a4083eacef        2 days ago           28.4MB
gcr.io/k8s-minikube/kicbase          v0.0.14                                          7ed8827b36a5        12 days ago          876MB
docker/desktop-kubernetes            kubernetes-v1.19.3-cni-v0.8.5-critools-v1.17.0   7f85afe431d8        5 weeks ago          285MB
k8s.gcr.io/kube-proxy                v1.19.3                                          cdef7632a242        5 weeks ago          118MB
k8s.gcr.io/kube-apiserver            v1.19.3                                          a301be0cd44b        5 weeks ago          119MB
k8s.gcr.io/kube-controller-manager   v1.19.3                                          9b60aca1d818        5 weeks ago          111MB
k8s.gcr.io/kube-scheduler            v1.19.3                                          aaefbfa906bd        5 weeks ago          45.7MB
k8s.gcr.io/etcd                      3.4.13-0                                         0369cf4303ff        2 months ago         253MB
k8s.gcr.io/coredns                   1.7.0                                            bfe3a36ebd25        5 months ago         45.2MB
docker/desktop-storage-provisioner   v1.1                                             e704287ce753        8 months ago         41.8MB
docker/desktop-vpnkit-controller     v1.0                                             79da37e5a3aa        8 months ago         36.6MB
k8s.gcr.io/pause                     3.2                                              80d28bedfe5d        9 months ago         683kB
miko docker run

PS C:\users\micha\Projects\docker_python_flask> docker run -p 5001:5000 docker_python_flask


docker: Error response from daemon: driver failed programming external connectivity on endpoint brave_meninsky (77e8567ccdc85794059762c6e0d95b11ac7577697087bc55d2363f9778e374e1):
Bind for 0.0.0.0:5001 failed: port is already allocated.

PS C:\users\micha\Projects\docker_python_flask> docker ps --all
CONTAINER ID        IMAGE                                 COMMAND                  CREATED             STATUS                      PORTS                                                                                                      NAMES
bba246b3b694        hello-python                          "python index.py"        58 seconds ago      Created                                                                                                                                brave_meninsky
5d5665bb7764        hello-python                          "python index.py"        14 hours ago        Up 14 hours                 0.0.0.0:5001->5000/tcp                                                                                     magical_curie
849c5a4208c4        gcr.io/k8s-minikube/kicbase:v0.0.14   "/usr/local/bin/entr…"   14 hours ago        Up 14 hours                 127.0.0.1:32771->22/tcp, 127.0.0.1:32770->2376/tcp, 127.0.0.1:32769->5000/tcp, 127.0.0.1:32768->8443/tcp   minikube
147d2ab4f4ed        dockerpython:latest                   "python index.py"        25 hours ago        Exited (255) 17 hours ago                                                                                                              sharp_allen
bbc32ed264a8        dockerpython                          "python index.py"        25 hours ago        Exited (255) 17 hours ago   0.0.0.0:5000->5000/tcp                                                                                     nervous_hamilton
1bc28fdc3675        dockerpython                          "python index.py"        26 hours ago        Exited (137) 25 hours ago                                                                                                              crazy_gates
deaf5f0a2105        alpine/git                            "git clone https://g…"   26 hours ago        Exited (0) 26 hours ago                                                                                                                repo




==============================================================================
minikube error
X Problems detected in kubelet:
  - Nov 21 20:08:51 minikube kubelet[146484]: E1121 20:08:51.846351  146484 pod_workers.go:191] Error syncing pod dc84553016e160751acb4150c2341708 ("etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"), skipping: failed to "StartContainer" for "etcd" with CrashLoopBackOff: "back-off 1m20s restarting failed container=etcd pod=etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"
  - Nov 21 20:09:04 minikube kubelet[146484]: E1121 20:09:04.807241  146484 pod_workers.go:191] Error syncing pod dc84553016e160751acb4150c2341708 ("etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"), skipping: failed to "StartContainer" for "etcd" with CrashLoopBackOff: "back-off 1m20s restarting failed container=etcd pod=etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"
  - Nov 21 20:09:18 minikube kubelet[146484]: E1121 20:09:18.371108  146484 pod_workers.go:191] Error syncing pod dc84553016e160751acb4150c2341708 ("etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"), skipping: failed to "StartContainer" for "etcd" with CrashLoopBackOff: "back-off 2m40s restarting failed container=etcd pod=etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"
  - Nov 21 20:09:19 minikube kubelet[146484]: E1121 20:09:19.444995  146484 pod_workers.go:191] Error syncing pod dc84553016e160751acb4150c2341708 ("etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"), skipping: failed to "StartContainer" for "etcd" with CrashLoopBackOff: "back-off 2m40s restarting failed container=etcd pod=etcd-minikube_kube-system(dc84553016e160751acb4150c2341708)"
  - Nov 21 20:09:19 minikube kubelet[146484]: E1121 20:09:19.477470  146484 pod_workers.go:191] Error syncing pod 3db2d5a1f1d85f0105d1061e3c754e0f ("kube-apiserver-minikube_kube-system(3db2d5a1f1d85f0105d1061e3c754e0f)"), skipping: failed to "StartContainer" for "kube-apiserver" with CrashLoopBackOff: "back-off 1m20s restarting failed container=kube-apiserver pod=kube-apiserver-minikube_kube-system(3db2d5a1f1d85f0105d1061e3c754e0f)"
resolved with

./minikube delete
==============================================================================
enabled kuberneties according with
https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/


and
./minikube start
==============================================================================
PS C:\Users\micha\minikube> kubectl version
Client Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.3", GitCommit:"1e11e4a2108024935ecfcb2912226cedeafd99df", GitTreeState:"clean", BuildDate:"2020-10-14T12:50:19Z", GoVersion:"go1.15.2", Compiler:"gc", Platform:"windows/amd64"}
Server Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.4", GitCommit:"d360454c9bcd1634cf4cc52d1867af5491dc9c5f", GitTreeState:"clean", BuildDate:"2020-11-11T13:09:17Z", GoVersion:"go1.15.2", Compiler:"gc", Platform:"linux/amd64"}
==============================================================================
PS C:\Users\micha\minikube> kubectl config get-contexts
CURRENT   NAME       CLUSTER    AUTHINFO   NAMESPACE
*         minikube   minikube   minikube   default

PS C:\Users\micha\minikube> kubectl config use-context minikube
Switched to context "minikube".
==============================================================================
PS C:\Users\micha\minikube> kubectl get nodes
NAME       STATUS   ROLES    AGE   VERSION
minikube   Ready    master   32m   v1.19.4
==============================================================================

PS C:\Users\micha\Projects\docker_python_flask> kubectl apply -f deployment.yaml
service/docker-python-flask-service created
deployment.apps/docker-python-flask created
==============================================================================
PS C:\users\micha\Projects\docker_python_flask> kubectl get deployment
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
docker-python-flask   0/2     2            0           8m1s
==============================================================================
PS C:\Users\micha\Projects\docker_python_flask> kubectl get pods
NAME                                  READY   STATUS              RESTARTS   AGE
docker-python-flask-c6ddfc869-b9vpb   0/1     ErrImageNeverPull   0          76s
docker-python-flask-c6ddfc869-bh6l2   0/1     ErrImageNeverPull   0          76s
docker-python-flask-c6ddfc869-nvdwz   0/1     ErrImageNeverPull   0          76s
docker-python-flask-c6ddfc869-x8fc6   0/1     ErrImageNeverPull   0          76s
==============================================================================
kubectl delete -n default deployment docker-python-flask
kubectl delete -n default deployment hello-python
==============================================================================
troubleshooting of ErrImageNeverPull

kubectl describe pods docker-python-flask-c6ddfc869-2ltck


https://github.com/knative/serving/issues/6101
How to use locally built docker image?



==============================================================================
Vyvoj a nasazujte rozhraní Python API s Kubernetes a Docker
https://www.metricfire.com/blog/develop-and-deploy-a-python-api-with-kubernetes-and-docker/

Vývoj a nasazení Python API s Kubernetes a Docker - cást II
https://www.metricfire.com/blog/develop-and-deploy-a-python-api-with-kubernetes-and-docker-part-ii/
==============================================================================
miko niginx for windows

http://nginx.org/en/docs/windows.html



==============================================================================
miko remove docker

docker --version

PS C:\users\micha\webapplication> docker images
REPOSITORY                           TAG                                              IMAGE ID            CREATED             SIZE
webapplication_web                   latest                                           a8f36c2b619b        21 minutes ago      94MB
hello-python                         latest                                           3f4893612a43        19 hours ago        885MB
alpine/git                           latest                                           76a4083eacef        3 days ago          28.4MB
gcr.io/k8s-minikube/kicbase          v0.0.14                                          7ed8827b36a5        13 days ago         876MB
redis                                alpine                                           c1949ec48c51        3 weeks ago         31.2MB
docker/desktop-kubernetes            kubernetes-v1.19.3-cni-v0.8.5-critools-v1.17.0   7f85afe431d8        5 weeks ago         285MB
k8s.gcr.io/kube-proxy                v1.19.3                                          cdef7632a242        5 weeks ago         118MB
k8s.gcr.io/kube-controller-manager   v1.19.3                                          9b60aca1d818        5 weeks ago         111MB
k8s.gcr.io/kube-apiserver            v1.19.3                                          a301be0cd44b        5 weeks ago         119MB
k8s.gcr.io/kube-scheduler            v1.19.3                                          aaefbfa906bd        5 weeks ago         45.7MB
k8s.gcr.io/etcd                      3.4.13-0                                         0369cf4303ff        2 months ago        253MB
k8s.gcr.io/coredns                   1.7.0                                            bfe3a36ebd25        5 months ago        45.2MB
docker/desktop-storage-provisioner   v1.1                                             e704287ce753        8 months ago        41.8MB
docker/desktop-vpnkit-controller     v1.0                                             79da37e5a3aa        8 months ago        36.6MB
k8s.gcr.io/pause                     3.2                                              80d28bedfe5d        9 months ago        683kB
hello-world                          latest                                           bf756fb1ae65        10 months ago       13.3kB
python                               3.4-alpine                                       c06adcf62f6e        20 months ago       72.9MB


docker pull ubuntu

PS C:\users\micha\webapplication> docker run -it -d ubuntu
3ae7892a70264df4c0271976813e78c63560ddd1e921cca7e216668939842573
PS C:\users\micha\webapplication> docker ps -a
CONTAINER ID        IMAGE                                 COMMAND                  CREATED             STATUS                     PORTS                                                                                                      NAMES
3ae7892a7026        ubuntu                                "/bin/bash"              6 seconds ago       Up 4 seconds
pensive_carson

PS C:\users\micha\webapplication> docker exec -it 3ae7892a7026 bash
root@3ae7892a7026:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@3ae7892a7026:/# pwd
/
root@3ae7892a7026:/# ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 14:08 pts/0    00:00:00 /bin/bash
root           9       0  0 14:10 pts/1    00:00:00 bash
root          17       9  0 14:10 pts/1    00:00:00 ps -ef
root@3ae7892a7026:/#

if you meke misstake in python code, its necessary to stop pot
docker ps -a
PS C:\users\micha\webapplication> docker ps -a
CONTAINER ID        IMAGE                                 COMMAND                  CREATED             STATUS                          PORTS                                                                                                      NAMES
637eb63bdef8        webapplication_web                    "python webapp.py"       4 minutes ago       Exited (1) About a minute ago                                                                                                              webapplication_web_1

docker stop 637eb63bdef8
docker rm 637eb63bdef8

docker images

then to delete image
docker rmi 637eb63bdef8

try python code first
PS C:\users\micha\webapplication> python webapp.py
* Serving Flask app "webapp" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 349-282-690
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


PS C:\users\micha\webapplication> docker-compose up
Building web
Step 1/5 : FROM python:3.7-alpine
3.7-alpine: Pulling from library/python
188c0c94c7c5: Already exists
55578f60cda7: Already exists
3d0ed0f04a02: Pull complete
98762f4040a9: Pull complete
01a62382ea2b: Pull complete
Digest: sha256:f1c33695422af596fb1d9d826d148134b10638dcad778eebd950fdefd00bf33f
Status: Downloaded newer image for python:3.7-alpine
---> 6b73b71fd64e
Step 2/5 : ADD . /code
---> b5f131cfd882
Step 3/5 : WORKDIR /code
---> Running in bd40a12ca1e7
Removing intermediate container bd40a12ca1e7
---> 1ea187990408
Step 4/5 : RUN pip install -r requirements.txt
---> Running in ab91cafdbbcc
Collecting flask
Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting redis
Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
Collecting click>=5.1
Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting itsdangerous>=0.24
Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Werkzeug>=0.15
Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting Jinja2>=2.10.1
Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe>=0.23
Downloading MarkupSafe-1.1.1.tar.gz (19 kB)
Building wheels for collected packages: MarkupSafe
Building wheel for MarkupSafe (setup.py): started
Building wheel for MarkupSafe (setup.py): finished with status 'done'
Created wheel for MarkupSafe: filename=MarkupSafe-1.1.1-py3-none-any.whl size=12627 sha256=5eee192d42a6cd28cfe0b61001874658d49ca6da1375d4d95aceee4fa0c88f4c
Stored in directory: /root/.cache/pip/wheels/b9/d9/ae/63bf9056b0a22b13ade9f6b9e08187c1bb71c47ef21a8c9924
Successfully built MarkupSafe
Installing collected packages: click, itsdangerous, Werkzeug, MarkupSafe, Jinja2, flask, redis
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0 redis-3.5.3
Removing intermediate container ab91cafdbbcc
---> eb356a4fd90c
Step 5/5 : CMD ["python", "webapp.py"]
---> Running in 394bf6e7922a
Removing intermediate container 394bf6e7922a
---> 1c318e48fd53
Successfully built 1c318e48fd53
Successfully tagged webapplication_web:latest
WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Starting webapplication_redis_1 ... done
Creating webapplication_web_1   ... done
Attaching to webapplication_redis_1, webapplication_web_1
redis_1  | 1:C 23 Nov 2020 14:38:51.184 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis_1  | 1:C 23 Nov 2020 14:38:51.184 # Redis version=6.0.9, bits=64, commit=00000000, modified=0, pid=1, just started
redis_1  | 1:C 23 Nov 2020 14:38:51.184 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
redis_1  | 1:M 23 Nov 2020 14:38:51.186 * Running mode=standalone, port=6379.
redis_1  | 1:M 23 Nov 2020 14:38:51.186 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1  | 1:M 23 Nov 2020 14:38:51.186 # Server initialized
redis_1  | 1:M 23 Nov 2020 14:38:51.186 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel.
This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo madvise > /sys/kernel/mm/transparent_hugepage/enabled' as root,
and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled (set to 'madvise' or 'never').
redis_1  | 1:M 23 Nov 2020 14:38:51.187 * Loading RDB produced by version 6.0.9
redis_1  | 1:M 23 Nov 2020 14:38:51.187 * RDB age 650 seconds
redis_1  | 1:M 23 Nov 2020 14:38:51.187 * RDB memory usage when created 0.77 Mb
redis_1  | 1:M 23 Nov 2020 14:38:51.187 * DB loaded from disk: 0.000 seconds
redis_1  | 1:M 23 Nov 2020 14:38:51.187 * Ready to accept connections
web_1    |  * Serving Flask app "webapp" (lazy loading)
web_1    |  * Environment: production
web_1    |    WARNING: This is a development server. Do not use it in a production deployment.
web_1    |    Use a production WSGI server instead.
web_1    |  * Debug mode: on
web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1    |  * Restarting with stat
web_1    |  * Debugger is active!
web_1    |  * Debugger PIN: 709-761-771
==============================================================================
miko youtube kubernetes

https://www.youtube.com/watch?v=tqr581_bBM0&list=PLot-YkcC7wZ9xwMzkzR_EkOrPahSofe5Q

/*========================================================================*/
gcr.io/k8s-minikube/kicbase



userdel miko
adduser miko
su miko
# adduser miko sudo
Adding user 'miko' to group 'sudo' ...
Adding user miko to group sudo
Done.


/*========================================================================*/
tutorial on
https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/


$ df -k
Filesystem                  1K-blocks     Used Available Use% Mounted on
udev                          1236752        0   1236752   0% /dev
tmpfs                          252032      856    251176   1% /run
/dev/mapper/host01--vg-root  49142428 14016628  32599800  31% /
tmpfs                         1260148        0   1260148   0% /dev/shm
tmpfs                            5120        0      5120   0% /run/lock
tmpfs                         1260148        0   1260148   0% /sys/fs/cgroup
tmpfs                          252028       16    252012   1% /run/user/124
tmpfs                          252028        0    252028   0% /run/user/0
$ minikube start
* minikube v1.6.2 on Ubuntu 18.04
* Selecting 'none' driver from user configuration (alternates: [])
* Running on localhost (CPUs=2, Memory=2461MB, Disk=47990MB) ...
* OS release is Ubuntu 18.04.3 LTS
* Preparing Kubernetes v1.17.0 on Docker '18.09.7' ...
  - kubelet.resolv-conf=/run/systemd/resolve/resolv.conf

* Pulling images ...
* Launching Kubernetes ...
* Configuring local host environment ...
* Waiting for cluster to come online ...
* Done! kubectl is now configured to use "minikube"

$ kubectl cluster-info
Kubernetes master is running at https://172.17.0.56:8443
KubeDNS is running at https://172.17.0.56:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
$ ^C
$
$ kubectl get nodes
NAME       STATUS   ROLES    AGE     VERSION
minikube   Ready    master   2m24s   v1.17.0

PS C:\projects\minikube> kubectl cluster-info
Kubernetes master is running at https://127.0.0.1:49153
KubeDNS is running at https://127.0.0.1:49153/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
PS C:\projects\minikube> kubectl get pods
NAME                                   READY   STATUS              RESTARTS   AGE
docker-python-flask-769b79b4b7-sc9n5   0/1     ErrImageNeverPull   0          75d
docker-python-flask-769b79b4b7-zl7fr   0/1     ErrImageNeverPull   0          75d
PS C:\projects\minikube> kubectl describe pods
Name:         docker-python-flask-769b79b4b7-sc9n5
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Sun, 22 Nov 2020 12:19:42 +0100
Labels:       app=docker-python-flask
              pod-template-hash=769b79b4b7
Annotations:  <none>
Status:       Pending
IP:           172.17.0.5
IPs:
  IP:           172.17.0.5
Controlled By:  ReplicaSet/docker-python-flask-769b79b4b7
Containers:
  docker-python-flask:
    Container ID:
    Image:          docker-python-flask:v1
    Image ID:
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ErrImageNeverPull
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-l2q8k (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  default-token-l2q8k:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-l2q8k
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason             Age                   From     Message
  ----     ------             ----                  ----     -------
  Warning  Failed             10m (x4186 over 25h)  kubelet  Error: ErrImageNeverPull
  Warning  ErrImageNeverPull  25s (x4232 over 25h)  kubelet  Container image "docker-python-flask:v1" is not present with pull policy of Never


Name:         docker-python-flask-769b79b4b7-zl7fr
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Sun, 22 Nov 2020 12:19:42 +0100
Labels:       app=docker-python-flask
              pod-template-hash=769b79b4b7
Annotations:  <none>
Status:       Pending
IP:           172.17.0.6
IPs:
  IP:           172.17.0.6
Controlled By:  ReplicaSet/docker-python-flask-769b79b4b7
Containers:
  docker-python-flask:
    Container ID:
    Image:          docker-python-flask:v1
    Image ID:
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ErrImageNeverPull
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-l2q8k (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  default-token-l2q8k:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-l2q8k
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason             Age                     From     Message
  ----     ------             ----                    ----     -------
  Warning  ErrImageNeverPull  5m33s (x4228 over 25h)  kubelet  Container image "docker-python-flask:v1" is not present with pull policy of Never
  Warning  Failed             30s (x4251 over 25h)    kubelet  Error: ErrImageNeverPull


/*========================================================================*/

kubectl get po -o vide
watch kubectl get po,svc
kubectl apply -f some_file.yml
sudo -j
docker ps | wc -l
kubectl describe po <po_id>
kubectl patch -f file.yml  --patch "$(cat file_name.yml)"
kubectl delete -f keyforce.yml #zruší konfiguraci věcí v file_name.yml
kubectl logs -f pod/<pod_id>
kubectl exec -it <pod_id> bash # napojí se do containeru.
  ps aux
  ip a

/*========================================================================*/
tutorials
https://www.youtube.com/watch?v=TMD_PhlLuPw

PS C:\projects\minikube> git clone https://github.com/overnightdigital/kubernetes-example.git

==============================================================================
miko kubectl login
miko login
# apt update && apt install kube-login
# kube-login admins5 --> v browseru se autentizovat (po me to chtelo dvoufazove overeni)
# kubectl config use-context ftxt-dev
# pokud tam chcete pristupovat z VM, tak prekopcit ~/.kube/config na VM

prihlasit se z browseru pres dvoufazove overeni.
je treba byt pryhlasen do VPN
potom by vse melo fugovat

cd ~/Downloads
michal-kocanrdle@kocandrle-m:~/Downloads$ ./kube-login-linux-1.2.9 admins5

INFO[2021-03-03T09:46:20+01:00] Spawning http server to receive callbacks
INFO[2021-03-03T09:46:20+01:00] Starting auth browser session. Please check your browser instances...
INFO[2021-03-03T09:46:20+01:00] Waiting for http server to receive callback
INFO[2021-03-03T09:46:21+01:00] callback received
INFO[2021-03-03T09:46:21+01:00] authCode and state verification passed. Fetching JWT
INFO[2021-03-03T09:46:21+01:00] exchanged authCode for JWT token. Refresh token was supplied
INFO[2021-03-03T09:46:21+01:00] writing credentials to /home/michal-kocanrdle/.kube/config
INFO[2021-03-03T09:46:22+01:00] Shutdown completed
michal-kocanrdle@kocandrle-m:~/Downloads$ kubectl cluster-info
Error in configuration: context was not found for specified context: kube1.ko
michal-kocanrdle@kocandrle-m:~/Downloads$ kubectl config use-context ftxt-dev
Switched to context "ftxt-dev".
michal-kocanrdle@kocandrle-m:~/Downloads$ kubectl cluster-info
Kubernetes control plane is running at https://ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz:6443
CoreDNS is running at https://ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz:6443/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.


pak uz
kubectl get pods --namespace=ftxt-rum-indexer

a pripadne rovnou pod
kubectl exec -it ftxt-merge-complete-5cdc9897cd-s5pgh -- /bin/bash
kubectl exec -it ftxt-merge-daily-66987dcc6-j582 -- /bin/bash




in seznam nakofigurvat podle\
https://srch.gitlab.seznam.net/overview/tech/kubernetes/
spustit script, vygeneruje prihlaseni
https://gitlab.seznam.net/srch/k8s-infra/-/raw/master/services/kube-dex-login2.sh?inline=false



michal-kocanrdle@kocandrle-m:~/Downloads$ kubectl get nodes
NAME                                                   STATUS                        ROLES    AGE    VERSION
ftxt-falpha-1.fulltext-dedicated-dev.ko1.os.scif.cz    Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-10.fulltext-dedicated-dev.ko1.os.scif.cz   Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-11.fulltext-dedicated-dev.ko1.os.scif.cz   Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-12.fulltext-dedicated-dev.ko1.os.scif.cz   Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-13.fulltext-dedicated-dev.ko1.os.scif.cz   Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-14.fulltext-dedicated-dev.ko1.os.scif.cz   Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-15.fulltext-dedicated-dev.ko1.os.scif.cz   Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-2.fulltext-dedicated-dev.ko1.os.scif.cz    Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-3.fulltext-dedicated-dev.ko1.os.scif.cz    Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-4.fulltext-dedicated-dev.ko1.os.scif.cz    Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-5.fulltext-dedicated-dev.ko1.os.scif.cz    Ready                         <none>   356d   v1.17.4-dirty
ftxt-falpha-6.fulltext-dedicated-dev.ko1.os.scif.cz    Ready                         <none>   356d   v1.17.4-dirty


michal-kocanrdle@kocandrle-m:~/Downloads$ kubectl get namespace|grep ftxt|grep indexer
ftxt-calib-indexer           Active   450d
ftxt-hadoop2-indexer         Active   450d
ftxt-news-indexer            Active   447d
ftxt-rum-indexer             Active   450d
ftxt-snippet-indexer         Active   399d
ftxt-video-indexer           Active   378d
ftxt-vodka-indexer           Active   450d



michal-kocanrdle@kocandrle-m:~/Downloads$ kubectl get pods --namespace=ftxt-rum-indexer                                                                                                              [90/185]

NAME                                             READY   STATUS        RESTARTS   AGE
ftxt-kube-state-metrics-65df54c77b-629nw         1/1     Running       0          279d
ftxt-merge-complete-6c8599d57-6cfft              1/1     Running       0          44h
ftxt-merge-daily-69645d9c9-c52pp                 1/1     Running       0          44h
ftxt-merge-fresh-7df76968ff-hc7xg                1/1     Running       0          44h
ftxt-rum-guard-control-0-1614762000-48b6s        0/1     Completed     0          9m48s
ftxt-rum-guard-dailyeraser-0-1614762000-f766t    0/1     Completed     0          9m48s
ftxt-rum-guard-feeds-0-1614762300-72rdp          0/1     Completed     0          4m51s
ftxt-rum-guard-feeds-1-1614762300-qt47m          0/1     Completed     0          4m51s
ftxt-rum-guard-feeds-2-1614762300-xb4xn          0/1     Completed     0          4m50s
ftxt-rum-guard-feeds-3-1614762300-5qcdj          0/1     Completed     0          4m50s
ftxt-rum-guard-feeds-4-1614762300-clshp          0/1     Completed     0          4m50s
ftxt-rum-guard-feedtrash-0-1614762000-rvlv9      0/1     Completed     0          9m46s
ftxt-rum-guard-increments-0-1614762300-r6qb8     0/1     Completed     0          4m49s
ftxt-rum-guard-increments-1-1614762300-mn6mv     0/1     Completed     0          4m49s
ftxt-rum-guard-incrtrash-0-1614762000-ccpnf      0/1     Completed     0          9m46s
ftxt-rum-guard-outdated-0-1614762000-8gzsd       0/1     Completed     0          9m45s
ftxt-rum-guard-queues-0-1614762000-w7vkd         0/1     Completed     0          9m45s
1ftxt-rum-incontrol-6b5f86746c-8dvtj              1/1     Running       0          103d
ftxt-rum-indexer-resources-2zfbz                 1/1     Running       0          15h
ftxt-rum-indexer-55bfdbf495-2cbfx                2/2     Running       0          15h
........................... many ftxt-rum-indexer pods ................................

ftxt-rum-indexer-test-service-6b98864b7c-t94jd   2/2     Running       0          56d
tiller-deploy-67fc7484f-tfbwf                    1/1     Running       2          396d


miko set namespace

kubectl config set-context --current --namespace=ftxt-rum-indexer

................................................................
................................................................
................................................................
dderror message

kubectl get nodes
The connection to the server localhost:8080 was refused - did you specify the right host or port?
fixed y chnigin

current-context: ""

changed with

current-context: "ftxt-dev"
users:
- name: michal.kocandrle-ftxt-dev


==============================================================================
kubectl cluster-info
Kubernetes control plane is running at https://ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz:6443
CoreDNS is running at https://ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz:6443/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

michal-kocanrdle@kocandrle-m:~$ kubectl get namespace|grep ftxt|grep indexer
ftxt-calib-indexer           Active   442d
ftxt-hadoop2-indexer         Active   442d
ftxt-news-indexer            Active   440d
ftxt-rum-indexer             Active   442d
ftxt-snippet-indexer         Active   392d
ftxt-video-indexer           Active   371d
ftxt-vodka-indexer           Active   442d

kubectl get pods --namespace=ftxt-rum-indexer

kubectl config set-context --current --namespace=ftxt-rum-indexer

michal-kocanrdle@kocandrle-m:~$ kubectl get pods --namespace=ftxt-rum-indexer
NAME                                             READY   STATUS        RESTARTS   AGE
ftxt-kube-state-metrics-65df54c77b-629nw         1/1     Running       0          272d
ftxt-merge-complete-66dd8dbc9b-fjh6t             1/1     Running       4          97d
ftxt-merge-daily-7cff76f99d-7csm2                1/1     Running       69         20d
ftxt-merge-fresh-5c64f9bd98-lbtzj                1/1     Running       496        81d
ftxt-rum-guard-control-0-1614156000-x9d88        0/1     Completed     0          8m23s
ftxt-rum-guard-dailyeraser-0-1614153600-wnc8h    0/1     Completed     0          48m
ftxt-rum-guard-feeds-0-1614156300-f9cpk          0/1     Completed     0          3m15s
ftxt-rum-guard-feeds-1-1614156300-mlh45          0/1     Completed     0          3m14s
ftxt-rum-guard-feeds-2-1614156300-lspsn          0/1     Completed     0          3m14s
ftxt-rum-guard-feeds-3-1614156300-pxm87          0/1     Completed     0          3m14s
ftxt-rum-guard-feeds-4-1614156300-wqmff          0/1     Completed     0          3m14s
ftxt-rum-guard-feedtrash-0-1614156300-mjm5r      0/1     Completed     0          3m13s
ftxt-rum-guard-increments-0-1614156300-lq9gf     0/1     Completed     0          3m13s
ftxt-rum-guard-increments-1-1614156300-zrjbs     0/1     Completed     0          3m13s
ftxt-rum-guard-incrtrash-0-1614156300-wtz7g      0/1     Completed     0          3m13s
ftxt-rum-guard-outdated-0-1614156300-cqgbt       0/1     Completed     0          3m12s
ftxt-rum-guard-queues-0-1614156300-zwq9b         0/1     Completed     0          3m12s
ftxt-rum-incontrol-6b5f86746c-8dvtj              1/1     Running       0          96d
ftxt-rum-indexer-55bfdbf495-fkp6q                2/2     Running       0          19h
ftxt-rum-indexer-55bfdbf495-vm28p                2/2     Running       0          19h
ftxt-rum-indexer-resources-2nbgq                 1/1     Running       0          19h
ftxt-rum-indexer-resources-4nths                 1/1     Running       0          19h
ftxt-rum-indexer-resources-7gcn7                 1/1     Running       0          19h
ftxt-rum-indexer-resources-blzcg                 1/1     Terminating   1          26d
ftxt-rum-indexer-resources-frjvp                 1/1     Running       0          19h
ftxt-rum-indexer-resources-n546m                 1/1     Running       0          19h
ftxt-rum-indexer-resources-snbbm                 1/1     Running       0          19h
ftxt-rum-indexer-resources-v4zsc                 1/1     Running       0          19h
ftxt-rum-indexer-resources-zzzbz                 1/1     Running       0          19h
ftxt-rum-indexer-test-service-6b98864b7c-t94jd   2/2     Running       0          49d
tiller-deploy-67fc7484f-tfbwf                    1/1     Running       2          389d
==============================================================================
kubectl get pods --namespace=ftxt-rum-indexer
kubectl get pods -o wide --namespace=ftxt-rum-indexer
NAME                                             READY   STATUS        RESTARTS   AGE     IP              NODE                                              NOMINATED NODE   READINESS GATES
ftxt-kube-state-metrics-65df54c77b-629nw         1/1     Running       0          272d    10.238.41.140   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-merge-complete-66dd8dbc9b-fjh6t             1/1     Running       4          97d     10.238.44.161   ftxt-k8s6.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-merge-daily-7cff76f99d-7csm2                1/1     Running       69         20d     10.238.39.101   ftxt-k8s2.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-merge-fresh-5c64f9bd98-lbtzj                1/1     Running       496        81d     10.238.33.71    ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-control-0-1614156000-x9d88        0/1     Completed     0          9m58s   10.238.41.193   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-dailyeraser-0-1614153600-wnc8h    0/1     Completed     0          50m     10.238.41.250   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-feeds-0-1614156300-f9cpk          0/1     Completed     0          4m50s   10.238.41.145   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-feeds-1-1614156300-mlh45          0/1     Completed     0          4m49s   10.238.41.174   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-feeds-2-1614156300-lspsn          0/1     Completed     0          4m49s   10.238.34.41    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-feeds-3-1614156300-pxm87          0/1     Completed     0          4m49s   10.238.41.132   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-feeds-4-1614156300-wqmff          0/1     Completed     0          4m49s   10.238.34.39    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-feedtrash-0-1614156300-mjm5r      0/1     Completed     0          4m48s   10.238.34.18    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-increments-0-1614156300-lq9gf     0/1     Completed     0          4m48s   10.238.34.43    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-increments-1-1614156300-zrjbs     0/1     Completed     0          4m48s   10.238.34.19    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-incrtrash-0-1614156300-wtz7g      0/1     Completed     0          4m48s   10.238.34.51    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-outdated-0-1614156300-cqgbt       0/1     Completed     0          4m47s   10.238.34.95    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-guard-queues-0-1614156300-zwq9b         0/1     Completed     0          4m47s   10.238.34.99    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-incontrol-6b5f86746c-8dvtj              1/1     Running       0          96d     10.238.17.68    ftxt-k8s3.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-55bfdbf495-fkp6q                2/2     Running       0          19h     10.238.35.16    ftxt-k8s8.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-55bfdbf495-vm28p                2/2     Running       0          19h     10.238.34.78    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-2nbgq                 1/1     Running       0          19h     10.238.25.182   ftxt-k8s4.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-4nths                 1/1     Running       0          19h     10.238.17.98    ftxt-k8s3.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-7gcn7                 1/1     Running       0          19h     10.238.35.104   ftxt-k8s8.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-blzcg                 1/1     Terminating   1          26d     10.238.29.204   ftxt-k8s5.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-frjvp                 1/1     Running       0          19h     10.238.34.15    ftxt-k8s7.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-n546m                 1/1     Running       0          19h     10.238.33.64    ftxt-k8s1.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-snbbm                 1/1     Running       0          19h     10.238.39.107   ftxt-k8s2.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-v4zsc                 1/1     Running       0          19h     10.238.41.213   ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-resources-zzzbz                 1/1     Running       0          19h     10.238.44.192   ftxt-k8s6.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
ftxt-rum-indexer-test-service-6b98864b7c-t94jd   2/2     Running       0          49d     10.238.39.98    ftxt-k8s2.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
tiller-deploy-67fc7484f-tfbwf                    1/1     Running       2          389d    10.238.42.197   ftxt-k8s3.fulltext-dedicated-dev.ko1.os.scif.cz   <none>           <none>
==============================================================================

kubectl config set-context --current --namespace=ftxt-rum-indexer

kubectl logs ftxt-rum-indexer-resources-zzzbz


==============================================================================
michal-kocanrdle@kocandrle-m:~$ kubectl get pods --show-labels
NAME                                             READY   STATUS        RESTARTS   AGE     LABELS
ftxt-kube-state-metrics-65df54c77b-629nw         1/1     Running       0          272d    app.kubernetes.io/name=kube-state-metrics,app.kubernetes.io/version=v1.9.0,k8s-app=kube-state-metrics,pod-template-
hash=65df54c77b
ftxt-merge-complete-66dd8dbc9b-fjh6t             1/1     Running       4          97d     chart=merge-0.1.3,complete=true,deployment-id=manual,ftxt-merge-complete=true,merge-complete=true,merge=true,pod-te
mplate-hash=66dd8dbc9b,release-name=merge,release-revision=1
ftxt-merge-daily-7cff76f99d-7csm2                1/1     Running       69         20d     chart=merge-0.1.3,daily=true,deployment-id=manual,ftxt-merge-daily=true,merge-daily=true,merge=true,pod-template-ha
sh=7cff76f99d,release-name=merge,release-revision=1
ftxt-merge-fresh-5c64f9bd98-lbtzj                1/1     Running       496        81d     chart=merge-0.1.3,deployment-id=manual,fresh=true,ftxt-merge-fresh=true,merge-fresh=true,merge=true,pod-template-ha
sh=5c64f9bd98,release-name=merge,release-revision=1
ftxt-rum-guard-control-0-1614156600-xmbqt        0/1     Completed     0          6m39s   controller-uid=94e6b872-4065-4b1a-85d0-2bf3bee5caa6,job-name=ftxt-rum-guard-control-0-1614156600
ftxt-rum-guard-dailyeraser-0-1614153600-wnc8h    0/1     Completed     0          56m     controller-uid=0d82d16a-8d62-4265-9b4d-75a6d3abdba4,job-name=ftxt-rum-guard-dailyeraser-0-1614153600
ftxt-rum-guard-feeds-0-1614156900-xp89b          0/1     Completed     0          95s     controller-uid=8abbb53b-d500-483c-8340-aa7604a7a5c2,job-name=ftxt-rum-guard-feeds-0-1614156900
ftxt-rum-guard-feeds-1-1614156900-c8zkj          0/1     Completed     0          95s     controller-uid=c92fc63c-0d3b-4b29-9732-00a85c76585f,job-name=ftxt-rum-guard-feeds-1-1614156900
ftxt-rum-guard-feeds-2-1614156900-vnvlh          0/1     Completed     0          94s     controller-uid=189de0ad-e741-492f-9a35-fc106946983b,job-name=ftxt-rum-guard-feeds-2-1614156900
ftxt-rum-guard-feeds-3-1614156900-l9lmg          0/1     Completed     0          94s     controller-uid=9929efcf-4a86-4537-99cb-02875260b88f,job-name=ftxt-rum-guard-feeds-3-1614156900
ftxt-rum-guard-feeds-4-1614156900-qpd5q          0/1     Completed     0          94s     controller-uid=e2f7816a-cc7e-46be-8479-034bd07bc8df,job-name=ftxt-rum-guard-feeds-4-1614156900
ftxt-rum-guard-feedtrash-0-1614156300-mjm5r      0/1     Completed     0          11m     controller-uid=11d98af6-27b9-44f6-ac19-dd4af0b95dd1,job-name=ftxt-rum-guard-feedtrash-0-1614156300
ftxt-rum-guard-increments-0-1614156900-fxlqn     0/1     Completed     0          94s     controller-uid=cea957ad-58ba-406e-87bc-d727eaeded78,job-name=ftxt-rum-guard-increments-0-1614156900
ftxt-rum-guard-increments-1-1614156900-68lmt     0/1     Completed     0          93s     controller-uid=d327b8ce-8234-4fce-b338-7b0b64de3e0f,job-name=ftxt-rum-guard-increments-1-1614156900
ftxt-rum-guard-incrtrash-0-1614156300-wtz7g      0/1     Completed     0          11m     controller-uid=d95e72ec-8cc9-46f1-9a65-fd571f494772,job-name=ftxt-rum-guard-incrtrash-0-1614156300
ftxt-rum-guard-outdated-0-1614156300-cqgbt       0/1     Completed     0          11m     controller-uid=431ff67c-e1fe-4692-9ed6-a81cbe339452,job-name=ftxt-rum-guard-outdated-0-1614156300
ftxt-rum-guard-queues-0-1614156300-zwq9b         0/1     Completed     0          11m     controller-uid=31134fdc-904c-4625-b9a4-9a2261051fb9,job-name=ftxt-rum-guard-queues-0-1614156300
ftxt-rum-incontrol-6b5f86746c-8dvtj              1/1     Running       0          96d     ftxt-rum-incontrol=true,incontrol=true,pod-template-hash=6b5f86746c
ftxt-rum-indexer-55bfdbf495-fkp6q                2/2     Running       0          20h     ftxt-rum-indexer=true,indexer=true,name=ftxt-rum-indexer,pod-template-hash=55bfdbf495
ftxt-rum-indexer-55bfdbf495-vm28p                2/2     Running       0          20h     ftxt-rum-indexer=true,indexer=true,name=ftxt-rum-indexer,pod-template-hash=55bfdbf495
ftxt-rum-indexer-resources-2nbgq                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-4nths                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-7gcn7                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-blzcg                 1/1     Terminating   1          26d     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-frjvp                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-n546m                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-snbbm                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-v4zsc                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-resources-zzzbz                 1/1     Running       0          20h     controller-revision-hash=5744bd5fdc,ftxt-rum-indexer-resources=true,indexer=true,name=ftxt-rum-indexer-resources,po
d-template-generation=1
ftxt-rum-indexer-test-service-6b98864b7c-t94jd   2/2     Running       0          49d     app=ftxt-rum-indexer-test-service,ftxt-rum-indexer-test-service=true,name=ftxt-rum-indexer-test-service,pod-templat
e-hash=6b98864b7c
tiller-deploy-67fc7484f-tfbwf                    1/1     Running       2          389d    app=helm,name=tiller,pod-template-hash=67fc7484f

==============================================================================
Interacting with running Pods

kubectl logs my-pod                                 # dump pod logs (stdout)
kubectl logs -l name=myLabel                        # dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod --previous                      # dump pod logs (stdout) for a previous instantiation of a container
kubectl logs my-pod -c my-container                 # dump pod container logs (stdout, multi-container case)
kubectl logs -l name=myLabel -c my-container        # dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod -c my-container --previous      # dump pod container logs (stdout, multi-container case) for a previous instantiation of a container
kubectl logs -f my-pod                              # stream pod logs (stdout)
kubectl logs -f my-pod -c my-container              # stream pod container logs (stdout, multi-container case)
kubectl logs -f -l name=myLabel --all-containers    # stream all pods logs with label name=myLabel (stdout)
kubectl run -i --tty busybox --image=busybox -- sh  # Run pod as interactive shell
kubectl run nginx --image=nginx -n
mynamespace                                         # Run pod nginx in a specific namespace
kubectl run nginx --image=nginx                     # Run pod nginx and write its spec into a file called pod.yaml
--dry-run=client -o yaml > pod.yaml

kubectl attach my-pod -i                            # Attach to Running Container
kubectl port-forward my-pod 5000:6000               # Listen on port 5000 on the local machine and forward to port 6000 on my-pod
kubectl exec my-pod -- ls /                         # Run command in existing pod (1 container case)
kubectl exec --stdin --tty my-pod -- /bin/sh        # Interactive shell access to a running pod (1 container case)
kubectl exec my-pod -c my-container -- ls /         # Run command in existing pod (multi-container case)
kubectl top pod POD_NAME --containers               # Show metrics for a given pod and its containers
kubectl top pod POD_NAME --sort-by=cpu              # Show metrics for a given pod and sort it by 'cpu' or 'mem
==============================================================================
miko Deployments

ftxt-rum-indexer
ftxt-merge-complete
ftxt-merge-daily
ftxt-merge-fresh
ftxt-rum-indexer-test-service
ftxt-rum-incontrol
ftxt-kube-state-metrics
tiller-deploy
==============================================================================
miko pods
kubectl get pods --namespace=ftxt-rum-indexer


ftxt-rum-indexer-55bfdbf495-fkp6q
 ftxt-rum-indexer-55bfdbf495-vm28p

 kubectl exec -it ftxt-rum-indexer-resources-2zfbz -- /bin/bash

 kubectl logs --tail=20 ftxt-rum-indexer-resources-lwqzr
 ftxt-rum-indexer-resources-2zfbz




==============================================================================
miko kubectl login on my locale
miko kubectl seznam

in /home/michal-kocanrdle/Downloads/
./kube-login-linux-1.2.10 admins5

kubectl config use-context ftxt-dev

all should work fine then
kubectl get pods --show-labels



==============================================================================

kubectl config set-context --current --namespace=ftxt-rum-indexer

miko containers
kubectl get pods --namespace=ftxt-rum-indexer -o=jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |sort > rum_items.txt

michal-kocanrdle@kocandrle-m:~/kube$ grep 55bfdbf495-fkp6q rum_containers.txt
ftxt-rum-indexer-55bfdbf495-fkp6q:      docker.dev.dszn.cz/fulltext/indexer-buster:master, docker.dev.dszn.cz/admins5/pushgateway:0.3.1-1,


 ==============================================================================
 miko log '
kubectl logs -f $a_pod -c $a_con             # stream pod container logs (stdout, multi-container case)
kubectl logs -f ftxt-rum-indexer-55bfdbf495-fkp6q -c docker://3e84ac73ea67be6cf812ad878d548009f6389696934559ea24064aadbfe27f1d




kubectl get pods --show-labels
label
ftxt-rum-indexer-55bfdbf495-fkp6q                2/2     Running       0          26h     ftxt-rum-indexer=true,indexer=true,name=ftxt-rum-indexer,pod-template-hash=55bfdbf495


kubectl describe pod ftxt-rum-indexer-55bfdbf495-fkp6q
michal-kocanrdle@kocandrle-m:~/kube$ kubectl describe pod ftxt-rum-indexer-55bfdbf495-fkp6q|grep 'Container ID'
    Container ID:   docker://3e84ac73ea67be6cf812ad878d548009f6389696934559ea24064aadbfe27f1d
    Container ID:   docker://dd8189e23cd1f0c8080197ee8fd9bbdb8afdb75e33a1b02f13d93a6802539163

miko container
kubectl logs -f ftxt-rum-indexer-resources-lwqzr indexer> indexer.log


==============================================================================

miko merge pod
kubectl describe pod ftxt-rum-indexer-resources-lwqzr

kubectl logs -f ftxt-rum-indexer-resources-lwqzr > indexer-resource.log

kubectl exec -it ftxt-rum-indexer-resources-lwqzr -- /bin/bash



==============================================================================

michal-kocanrdle@kocandrle-m:~/kube/log_files$ kubectl describe pod ftxt-rum-indexer-resources-lwqzr
Name:         ftxt-rum-indexer-resources-lwqzr
Namespace:    ftxt-rum-indexer
Priority:     0
Node:         ftxt-k8s9.fulltext-dedicated-dev.ko1.os.scif.cz/10.244.9.150
Start Time:   Tue, 02 Mar 2021 18:19:15 +0100
Labels:       controller-revision-hash=5744bd5fdc
              ftxt-rum-indexer-resources=true
              indexer=true
              name=ftxt-rum-indexer-resources
              pod-template-generation=1
Annotations:  <none>
Status:       Running
IP:           10.238.41.145
IPs:
  IP:           10.238.41.145
Controlled By:  DaemonSet/ftxt-rum-indexer-resources
Containers:
  ftxt-rum-indexer-resource-updater:
    Container ID:   docker://c3769e22cee574b5889a11077486213dc01fdbf3f54aeb0a003d45ad4a6a5902
    Image:          docker.dev.dszn.cz/fulltext/indexer-buster:master
    Image ID:       docker-pullable://docker.dev.dszn.cz/fulltext/indexer-buster@sha256:6cbcfa0daf201742067eb94845f19a46ec950268f98b63515c72fbcb5fd0bd9a
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Tue, 02 Mar 2021 18:20:24 +0100
    Ready:          True
    Restart Count:  0
    Limits:
      memory:  400M
    Requests:
      cpu:     1
      memory:  400M
    Environment:
      ROLE:  resource_updater
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-zf4x4 (ro)
      /www/fulltext/indexer/conf/ from indexer-config (ro)
      /www/fulltext/indexer/resources from resources (rw)
      /www/kubernetes/ftxt-indexer/data from data (rw)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  data:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:
    SizeLimit:  <unset>
  resources:
    Type:          HostPath (bare host directory volume)
    Path:          /www/kubernetes/ftxt-rum-indexer/resources
    HostPathType:
  indexer-config:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      indexer-config
    Optional:  false
 default-token-zf4x4:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-zf4x4
    Optional:    false
QoS Class:       Burstable
Node-Selectors:  ftxt-rum-indexer=true
Tolerations:     node.kubernetes.io/disk-pressure:NoSchedule op=Exists
                 node.kubernetes.io/memory-pressure:NoSchedule op=Exists
                 node.kubernetes.io/not-ready:NoExecute op=Exists
                 node.kubernetes.io/pid-pressure:NoSchedule op=Exists
                 node.kubernetes.io/unreachable:NoExecute op=Exists
                 node.kubernetes.io/unschedulable:NoSchedule op=Exists
Events:          <none>
==============================================================================

Vývoj android aplikací v jazyce python 

https://dspace5.zcu.cz/bitstream/11025/31871/1/Vyvoj%20android%20aplikaci%20v%20jazyce%20Python.pdf
==============================================================================

