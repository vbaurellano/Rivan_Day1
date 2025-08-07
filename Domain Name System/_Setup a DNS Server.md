
<!-- Your monitor number = #$34T# -->


# 🌐 Domain Name System
*Connect to websites through IP addresses alone.*

~~~cmd
@cmd
ping google.com         ___.___.___.___
ping cisco.com          ___.___.___.___
ping rivanit.com        ___.___.___.___
~~~

&nbsp;
## 📋 Task 01 - Set up your own DNS Server.

### 📦 Install Windows DNS Server
~~~Powershell
@powershell
Install-WindowsFeature -name dns -includeManagementTools
~~~

<br>

### 📂 Create a Zone File for __rivan#$34T#.com__
  - Forward & Reverse lookup zones
    - DNS Records

~~~cmd
@cmd
ping ns.google.com
ping www
ping imap
ping pop
ping smtp
~~~

<br>
<br>

---

### 🎯 Exercise 01: Configure additional DNS records for the following devices:

| Alias |     | Device       | Host |     | Device       | Host |
| ---   | --- | ---          | ---  | --- | ---          | ---  | 
| Web   |     | __CoreBABA__ | cb   |     | __WLC__      | wc   |
| SMTP  |     | __CoreTaas__ | ct   |     | __Cam6__     | c6   |
| IMAP  |     | __CUCM__     | cm   |     | __Cam8__     | c8   |
| POP3  |     | __EDGE__     | ed   |     | __Ephone1__  | e1   |
|       |     | __AP__       | ap   |     | __Ephone2__  | e2   |

<br>
<br>

---

### 🎯 Exercise 02: Configure DNS for __`itsolutions#$34T#.com`__ with the following DNS records:

| Alias |     | Device       | Host     |     | Device       | Host     |
| ---   | --- | ---          | ---      | --- | ---          | ---      | 
| Web   |     | __CoreBABA__ | coreprim |     | __WLC__      | wifictrl |
| SMTP  |     | __CoreTaas__ | coresec  |     | __Cam6__     | cam6     |
| IMAP  |     | __CUCM__     | callm    |     | __Cam8__     | cam8     |
| POP3  |     | __EDGE__     | edge     |     | __Ephone1__  | ep1      |
|       |     | __AP__       | wifiap   |     | __Ephone2__  | ep2      |

<br>
<br>

---

## 📋 Task 02 - Create a website for __rivan#$34T#.com__

### 📦 Install Windows Web Server
~~~Powershell
@powershell
Install-WindowsFeature -name Web-Server -includeManagementTools
~~~

<br>

### 📂 Create the website

| Site name           | Physical path | Bindings |
| ---                 | ---           | ---      |
| __rivan#$34T#.com__ | officebiz     | All:80   |

<br>
<br>

---

### 🎯 Exercise 03: Configure a website for __`itsolutions#$34T#.com`__ using the web directory, cellbiz

| Site name                 | Physical path | Bindings |
| ---                       | ---           | ---      |
| __itsolutions#$34T#.com__ | cellbiz       | All:80   |

<br>
<br>

---

### 📦 Powershell Script for DNS Zones & Records
~~~powershell
@powershell
add-DnsServerPrimaryZone -Name "rivan#$34T#.com" -ZoneFile "rivan#$34T#.com.dns"

﻿add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ns -ipv4address 10.#$34T#.1.7
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name www -hostname ns.rivan#$34T#.com
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name imap -hostname ns.rivan#$34T#.com
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name pop -hostname ns.rivan#$34T#.com
add-DnsServerResourceRecord -zonename rivan#$34T#.com -Cname -name smtp -hostname ns.rivan#$34T#.com

add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name cb -ipv4address 10.#$34T#.1.4
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ct -ipv4address 10.#$34T#.1.2
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name cm -ipv4address 10.#$34T#.100.8
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ed -ipv4address 10.#$34T#.#$34T#.1
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name e1 -ipv4address 10.#$34T#.100.101
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name e2 -ipv4address 10.#$34T#.100.102
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name c6 -ipv4address 10.#$34T#.50.6
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name c8 -ipv4address 10.#$34T#.50.8
add-DnsServerResourceRecord -zonename rivan#$34T#.com -A -name ap -ipv4address 10.#$34T#.10.3
~~~

&nbsp;
---
&nbsp;

### 📦 Powershell Script for Website configuration
~~~powershell
@powershell
New-Website -name "rivan#$34T#.com" -hostheader "www.rivan#$34T#.com" -physicalpath "d:\webs\officebiz"
~~~

<br>
<br>

---
&nbsp;

### Exercise 03: Configure DNS and Web for bpiph#$34T#.com

  - The zone file must contain records for Web, eMail, CUCM,EDGE, ePhone1 and ePhone2.
  - Assign the bpi html as its own main page.



Internet Assigned Numbers Authority
Authoritative DNS Root Servers 

What happens when a dns server does not know how to map a domain name?


@cmd
nslookup -type=NS com. a.root-servers.net
nslookup -type=NS rivanit.com d.gtld-servers.net
nslookup -type=NS rivanit.com ns1.dns-parking.com


Root Servers
  > TLD
    > SLD
	  > DNS RECORDS

DNS Forwarders
Recursive



Lookup nemsu.edu.ph

@cmd
nslookup -type=NS



Configure Forwarders

#########################################################################
### Powershell Script for DNS Forwarders

! You do not forward things yourself

Remove-DnsServerForwarder -ipAddress 10.11.1.10, 10.12.1.10, 10.21.1.10, 10.22.1.10, 10.31.1.10, 10.32.1.10, 10.41.1.10, 10.42.1.10,10.51.1.10, 10.52.1.10, 10.61.1.10, 10.62.1.10, 10.71.1.10, 10.72.1.10, 10.81.1.10, 10.82.1.10 -PassThru
Add-DnsServerForwarder -ipAddress 10.11.1.10, 10.12.1.10, 10.21.1.10, 10.22.1.10, 10.31.1.10, 10.32.1.10, 10.41.1.10, 10.42.1.10,10.51.1.10, 10.52.1.10, 10.61.1.10, 10.62.1.10, 10.71.1.10, 10.72.1.10, 10.81.1.10, 10.82.1.10 -PassThru





Verify:

@Cisco
conf t
 ip domain lookup
 ip name-server 10.#$34T#.1.10
 end
ping ns.ccna#$34T#.com



__________
**********
2. File Transfer

Upload configurations to FTP Server. (CoreTaas, CoreBaba, CUCM, EDGE)

@Cisco
copy run ftp://ccna#$34T#.com


How to copy the current IOS of a Cisco Switch

@Cisco
archive upload-sw ftp://ccna#$34T#.com



__________
**********
3. Mail Exchanger

Create an MX record on the Zone file.
	Install .NET Framework 3.5 Features


Create users and emails for ccna#$34T#.com and bpiph#$34T#.com

  User1: ac
  Pass: C1sc0123
  
  User: Support

  Pass: C1sc0123





