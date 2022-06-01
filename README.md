# ansible-role-sip-deploy
![Version](https://img.shields.io/github/v/release/mach1el/ansible-role-sip-deploy?color=brown&style=plastic) ![License](https://img.shields.io/github/license/mach1el/ansible-role-sip-deploy?color=purple&style=plastic)
Auto deploy SIP proxy and dependencies

## Role pathes
	 .
	├──  cred.txt
	├──  defaults
	│   └──  main.yml
	├──  handlers
	│   └──  main.yml
	├──  README.md
	├──  tasks
	│   ├──  add_devops.yml
	│   ├──  configure_prometheus.yml
	│   ├──  disable_swap.yml
	│   ├──  get_important_scripts.yml
	│   ├──  install_cronjob.yml
	│   ├──  install_k8s.yaml
	│   ├──  install_opensips_cli.yml
	│   ├──  install_opensips_cp.yml
	│   ├──  install_packages.yml
	│   ├──  install_zsh.yml
	│   ├──  main.yml
	│   ├──  pgpass.yaml
	│   └──  upgrade_debian.yml
	└──  templates
	    ├──  kubernetes.list.j2
	    ├──  opensips-cli.list.j2
	    ├──  pgpass.j2
	    ├──  prometheus.yml.j2
	    ├──  sources.list.j2
	    └──  zshrc.j2


## Role Playbook
	---
	- name: Run role.
	  hosts: localhost
	  roles:
	   - 'ansible-role-sip-deploy'
