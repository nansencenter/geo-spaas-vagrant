# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://atlas.hashicorp.com/ubuntu/trusty64"

  config.vm.define "course", primary: true do |course|
    course.vm.network :private_network, ip: "192.168.33.10"
  end

  config.vm.define "geospaas_core", autostart: false do |geospaas_core|
    geospaas_core.vm.network :private_network, ip: "192.168.33.11"
  end

  config.vm.define "doppler", autostart: false do |doppler|
    doppler.vm.network :private_network, ip: "192.168.33.12"
  end

  config.vm.define "metsarvind", autostart: false do |metsarvind|
    metsarvind.vm.network :private_network, ip: "192.168.33.14"
  end

  config.vm.define "globcurrent", autostart: false do |globcurrent|
    globcurrent.vm.network :private_network, ip: "192.168.33.15"
  end

  config.vm.define "icedrifters", autostart: false do |icedrifters|
    icedrifters.vm.network :private_network, ip: "192.168.33.16"
    icedrifters.vm.synced_folder "/files/site_media/", "/site_media"
    icedrifters.vm.provider "virtualbox" do |v|
      v.memory = 10000
      v.cpus = 7
    end
  end

  config.vm.define "doppler_prod", autostart: false do |doppler_prod|
    doppler_prod.vm.network :private_network, ip: "192.168.33.17"
  end

  config.vm.define "cmems", autostart: false do |cmems|
    cmems.vm.network :private_network, ip: "192.168.33.18"
  end

  config.vm.define "icetype", autostart: false do |icetype|
    icetype.vm.network :private_network, ip: "192.168.33.19"
    icetype.vm.synced_folder "/files/site_media/", "/site_media"
    icetype.vm.provider "virtualbox" do |v|
      v.memory = 10000
      v.cpus = 6
    end

  config.vm.define "fabio", autostart: false do |cmems|
    cmems.vm.network :private_network, ip: "192.168.33.20"
  end


  config.vm.provider "virtualbox" do |v|
    v.memory = 4000
    v.cpus = 2
  end

  # If true, then any SSH connections made will enable agent forwarding.
  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "provisioning/site.yml"
    ansible.inventory_path = "provisioning/hosts"
    ansible.provisioning_path = "/vagrant"
    ansible.verbose = "vvv"
    ansible.install = true
    ansible.install_mode = "pip"
  end

end
