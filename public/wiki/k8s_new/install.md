1. Install ubuntu 24 server (Default installation process)
2. Install microk8s
    * sudo snap install microk8s --classic --channel=1.33
3. Expand cluster
4. Enable ingress
5. Enable nfs storage
    * microk8s helm3 repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
    * microk8s helm3 repo update
    * Add storage class
    ```yaml
    # sc-nfs.yaml
    ---
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
    name: nfs-crucial
    provisioner: nfs.csi.k8s.io
    parameters:
    server: 192.168.0.50
    share: /mnt/Crucial_Pool/Crucial_Dataset/TNK8Store
    reclaimPolicy: Delete
    volumeBindingMode: Immediate
    mountOptions:
    - hard
    - nfsvers=4.1

    ```
    * Add test pvc
    ```yaml
    # pvc-nfs.yaml
    ---
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: my-pvc
    spec:
    storageClassName: nfs-crucial
    accessModes: [ReadWriteOnce]
    resources:
        requests:
        storage: 5Gi

    ```
6. Enable Prometheus `microk8s enable prometheus`