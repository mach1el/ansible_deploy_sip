# SIP proxy provisioning
Auto deploy SIP proxy and dependencies ![License](https://img.shields.io/github/license/mach1el/ansible_deploy_sip?color=purple&style=plastic)

## Role tree

```
 .
├──  handlers
│   └──  main.yml
├──  LICENSE
├──  meta
│   └──  main.yml
├──  README.md
├──  tasks
│   ├──  add_devops.yml
│   ├──  configure_prometheus.yml
│   ├──  disable_swap.yml
│   ├──  get_important_scripts.yml
│   ├──  install_cronjob.yml
│   ├──  install_k8s.yml
│   ├──  install_opensips_cli.yml
│   ├──  install_opensips_cp.yml
│   ├──  install_packages.yml
│   ├──  install_zsh.yml
│   ├──  main.yml
│   ├──  pgpass.yml
│   └──  upgrade_debian.yml
├──  templates
│   ├──  kubernetes.list.j2
│   ├──  opensips-cli.list.j2
│   ├──  pgpass.j2
│   ├──  prometheus.yml.j2
│   ├──  sources.list.j2
│   └──  zshrc.j2
└──  vars
    └──  main.yml
```


## Role Playbook
```
---
- name: Run role.
  hosts: localhost
  roles:
   - 'ansible-role-sip-deploy'
```
