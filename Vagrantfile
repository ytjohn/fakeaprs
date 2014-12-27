# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"

  #
  config.vm.provider "vmware_fusion" do |v, override|
    override.vm.box = "nitrous-io/trusty64"
  end

  # Use puppet to install requirements.
  config.vm.provision "puppet" do |puppet|
    puppet.manifests_path = "vagrant"
    puppet.manifest_file = "default.pp"
  end
end
