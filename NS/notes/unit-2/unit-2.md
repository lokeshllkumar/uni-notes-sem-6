# UNIT-2

- network protocol
    - a set of rules that govern how data is transmitted b/w devices on a network
    - OSI is the most widely employed model communication b/w computers on a network
    - every layer communicates using a different protocol

> TCP/IP for packet routing and connections; BGP for route discovery; DNS for IP address discovery

- TCP/IP model
    - defines how data is transmitted over networks, ensuring reliable communication between devices
    - divides packets and one end, transfers them and assembles them at the other end
    - layers
        - app layer
            - functions - provides protocols for user-facing applications; HTTP, FTP, SMTP
            - sec challenges
                - vulnerable to attacks like phishing, buffer overflows and malware injection
                - weak or absent authentication
                - encryption is critical to protect sensitive data
        - transport layer
            - functions - manages end-to-end comm b/w devices; TCP and UDP
            - sec challenges
                - TCP susceptible to SYN flooding
                - session hijacking attacks can intercept and manipulate comm
                - TLS is used to encrypt data and provide secure communications
        - internet layer
            - functions - responsible for routing and addressing data packets using IP
            - sec challenges
                - IP spoofing allows attakers to impersonate others
                - fragmentation attacks can exploit the division and reassembling of packets
                - IPSec is used to authenticate and encrypt data packets
        - network access layer
            - functions - deals with physical and data link layers, ensuring transmission over physical media
            - sec challenges
                - ARP poisoning, MAC spoofing and VLAN hopping
                - strong authentication and encryption protocols can mitigate risks
    ![alt text](image.png)
    ![alt text](<Screenshot from 2025-02-11 18-57-02.png>)

- IPSec
    - protocol suite designed by IETF for securing IP comm by authenticating and encrypting data packets
    - network layer security
    - modes
        - transport - encrypts payload of IP packet; onl;y protects info coming from transport layer
        - tunnel - encrypts entire IP packet
        ![alt text](<Screenshot from 2025-02-11 20-56-22.png>)
    - protocols
        - authentication header(AH) - procides authentication and data integirty but no privacy
        ![alt text](<Screenshot from 2025-02-11 20-57-31.png>)
        - encapsulating security payload(ESP) - provides authentication, intergrity and privacy
        ![alt text](<Screenshot from 2025-02-11 20-58-49.png>)

- SSL/TLS
    - protocol suite to establish secure communciation channel b/w 2 parties across a network
    - transport layer security
    - SSL - cryptographic protocol for secure communication over the Internet
         - protocols
            - Handshake protocol - involves key exchange b/w client and server
            - ChangeCipherSpec protocol
            - Alert protocol
            - Record Protocol
        ![alt text](<Screenshot from 2025-02-11 22-08-16.png>)
    - TLS - ensures secure communication by encryptng data in transit using protocols like HTTPS
    - features
        - encryption
        - authentication
        - integrity

- SFTP
    - secure file transfer protocol
    - built on SSH
    - features
        - encryption of data under transfer
        - authentication via SSH keys/passwords
        - protection against eavesdropping and data tampering

- SSH
    - cryptograpic protocol for secure remote login and command exec
    - features
        - strong encryption for communication; public key authentication
        - protection against DNS spoofing and IP spoofing

- DNS
    - domain name system
        - DNS resolver
        - root nameserver
        - TLD server
        - authoritative nameserver
    - a system to translate domain names to the respective servers' IP addresses
    - vulnerabiliteis
        - DNS spoofing - manipulating DNS repsonses to redirect users to malicious sites
        - cache poisoning - injecting false data into a DNS resolver's cache
    - authentication occurs with the help of a random 16-bit TXID, abd response stays in cache only if teh TXID is the same at each stage; attackers guess TXID to deceive the resolver into thinking the response is valid
    - DNSSEC - adds cryptographic signatures to DNS records to ensure data integrity and authentication
        - types
            - public key
            - symmetric key
        - features
            - does nothing to imporve DNS availability
            - does nothing to improve DNS confidentiality
            - can still lead to buffer overflows

- routing protocols
    - routing 
        - intradomain - within an autonomous system
            - distance vector - RIP
            - link state - OSPF
        - interdomain - b/w autonomous systems
            - path vector - BGP
    - RIP
        - routing information protocol
        - least cost route  b/w 2 nodes is min distance; each node maintains a vector of min distances to every node; each node shares routing table with its immedaite neighbours periodically and when there is a change
        - uses UDP services on port 520
        - vulnerable to route poisoning and spoofing due to lack of authentication
    - OSPF
        - open shortest path first
        - uses Dijkstra's algo to build a routing table where each node has the entire topology of the domain
        - types of links
            - p2p
            - transient
            - stub
            - virtual
        - packets are encapsulated in IP datagrams
        - susceptible to attacks if authentication is not properly configured
    - BGP
        - border gateway protocol
        - similar to distane vector routing; atleast one "speaker" node in an AS that creates routing table and broadcasts to speaker nodes in neighbouring ASs
        - supports classless addressing
        - uses TCP services on port 179
        - vulnerable to prefix hijacking, route leaks and session hijacking due to the trust-based architecture it employs