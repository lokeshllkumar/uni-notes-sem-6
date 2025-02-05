# Cloud Computing and Security notes

---

## Intro

- on-demand delivery of IT resources over the Internet on a pay-as-you-go model
- AWS
- uses
    - data backup
    - disaster recovery
    - email
    - S/W dev and testing
    - big data analytics
- benefits
    - agility
        - easy access to a broad range of tech
    - elasticity
        - don't need to over provision resources up front to handle more load in the future
        - can easily scale resources up and down as business needs change
    - cost savings
        - can treat fixed expenses such as data centers for varibale expenses, which is a lot cheaper due to difference in scale
    - deploy globally
        - can expand to new geo locations + deploy in mins

## Cloud Delivery Models

- IaaS(infra as a service)
    - basic building blocks for cloud IT
    - examples
        - networking features
        - comps(virtual/dedicated H/W)
        - data storage space
    - highest level of flexibility and control over resources
- PaaS(platform as a service)
    - remove the need for orgs to manage udnerlying infra(H/W, OS, etc.)
    - provides pre-configed envs for development/deployment
    - examples
        - middleware
        - runtime envs
        - database
    - built on top of IaaS; more abstraction, less flexibility than IaaS
- SaaS(S/W as a service)
    - S/W apps run and managed by vendor
    - not needed to worry about maintenance or underlying arch of S/W; only about its usage
    - examples
        - web-based email

## Bare Metal Servers vs Hypervisors

### Bare Metal Servers

- physical server with tangible components like RAM, CPU, etc.\
- performance
    - optimized performance + resource utilization; direct access to components
    - ideal for high performance apps like databases and real-tiem analytics
- security
    - preferred for secure apps since there is no intermediary layer, removing an additional attack surface

### Hypervisor

- S/W layers created a separation b/w H/W components and OS; creates many VMs
- flexibility + isolation
    - ideal for testing envs requiring isolation b/w workloads
- resource sharing
    - amongst multiple VMs; resource efficiency
- ease on mgmt
    - ease of managing VMs

---

- bare metal servers become more powerful when a hypervisor is added
- multiple VMs run isolated from each other parallelly

## On Premises vs On Cloud

### On Premises

- use to running of app done inside + backup, privacy, updates, etc. must be managed in-house
- complete ownershp
- additional power labourers, database prog, OS, etc. required

### On Cloud

- delivery of on-demand computing services over the Internet in a cost-effective manner

---

- the difference
    - scalability
        - on premises - difficult to scale up and down as the needs change; more expensive
        - on cloud - easier + faster to scale up and down; pay as per usage
    - server storage
        - on premises - more space, power and maintenance to store
        - on cloud - provider manages storage and its requirements
    - data security
        - on-premises - less secure as it is up to the owner
        - on-cloud - far more secure
    - data loss/recovery
        - on-premises - in case of loss, recovery is little to none in most cases
        - on-cloud - robust recovery options provided by cloud provider
    - maintenance
        - on-premises - additional cost for maintenace
        - on-cloud - maintenance handled by cloud provider

## DNS

- domain name system
- translates domain names to IP addresses so that browsers can load Internet resources