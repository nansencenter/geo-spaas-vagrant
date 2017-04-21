[![Build Status](https://travis-ci.org/nansencenter/geo-spaas-vagrant.svg?branch=master)](https://travis-ci.org/nansencenter/geo-spaas-vagrant)

Configuration of Nansen-Cloud provisioning with vagrant
=======================================================
All virtual machines use miniconda to install python and various libraries.

Usage
=====
```
git clone https://github.com/nansencenter/geo-spaas-vagrant
cd geo-spaas-vagrant
vagrant up
```
Requires vagrant >= 1.8.4

Stable virtual machines:
=================
* course : 192.168.33.10
* geospaas_core : 192.168.33.11

Shared directories
==================
 * /vagrant/shared -> geo-spaas-vagrant/shared
  * this directory is shared also between virtual machines
  * conda_pkgs: cached conda packages
  * test_data: sample data

 * /vagrant/shared/course_vm -> geo-spaas-vagrant/shared/course_vm
  * this directory is specific for a virtual machine
  
Mounting network folders
========================
To mount network folders, you'll need to create a file ```main.yml``` in
```provisioning/roles/localvm/defaults/```. This file should contain a username
and password to access the network folders, so make sure to keep it out of
version control ++...

Here is an example setup:

```
---
mount_folders:
  - {mount_name: /mnt/<ip-like>, mount_src: //<ip-like> folder: <some-folder>}
  - {mount_name: /mnt/<ip-like>, mount_src: //<ip-like> folder: <some-other-folder>}

uid: <uid>
gid: <gid>
username: <username>
password: <passwd>
domain: <domain>
```

The items in ```mount_folders``` will then be mounted in the localvm tasks.
