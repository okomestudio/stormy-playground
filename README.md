# stormy-playground

Playground for Storm with VMs managed through Vagrant.

## Getting Started

1. From the vm directory, start the vagrant VMs:

```bash
$ cd vm
$ vagrant up
$ cd ..
```

2. Add the 'sshkey' to your ssh-agent:

```bash
$ ssh-add sshkey
```

3. A storm-ui is running on the nimbus host (storm's master), available at
   http://192.168.56.2:8080/
