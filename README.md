[![Build Status](https://travis-ci.org/nansencenter/geo-spaas-vagrant.svg?branch=master)](https://travis-ci.org/nansencenter/geo-spaas-vagrant)

Configuration of Nansen-Cloud provisioning with vagrant
=======================================================
All Virtual machines (VMs) use miniconda to install python and various libraries.

Usage
=====
```
git clone https://github.com/nansencenter/geo-spaas-vagrant
cd geo-spaas-vagrant
vagrant up
```
Requires vagrant >= 1.8.4

Virtual machines:
=================
* nansat : 192.168.33.10
* course : 192.168.33.11
* catalog : 192.168.33.12
* doppler : 192.168.33.13

Shared directories
==================
 * /vagrant/shared -> geo-spaas-vagrant/shared
  * this directory is shared also between virtual machines
  * conda_pkgs: cached conda packages
  * test_data: sample data

 * /vagrant/shared/catalog_vm -> geo-spaas-vagrant/shared/catalog_vm
  * this directory is specific for virtual machine
  * nansat
  * geo-spaas-catalog

NB! **You better destroy all your machines before git clone**
