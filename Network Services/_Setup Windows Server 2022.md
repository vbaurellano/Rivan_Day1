
<!-- Monitor Number = #$34T# -->


## Requirements
1. Windows Server 2022 Evaluation ISO
2. Type 2 Hypervisor (Such as VMWare Workstation, VirtualBox, Hyper-V, etc)

<br>
<br>

---
&nbsp;

## Setup the Virtual Machine (VMware Workstation)
1. Select __New Virtual Machine__
<img width="2211" height="1565" alt="image" src="https://github.com/user-attachments/assets/8216f479-8262-4cac-9ee3-cbc8f055180e" />

&nbsp;
---
&nbsp;

2. For the type of configuration, choose __Typical (recommended)__
<img width="2190" height="1533" alt="image" src="https://github.com/user-attachments/assets/6b93619e-807c-4cd7-8f71-48d73bd9b17d" />

&nbsp;
---
&nbsp;

3. For guest operating system installation, choose __I will install the operating system later.__
<img width="2188" height="1531" alt="image" src="https://github.com/user-attachments/assets/b416474b-3c21-464b-9fda-656ce77ae406" />

&nbsp;
---
&nbsp;

4. The guest operating system will be __Microsoft Windows__ version __Windows Server 2022__
<img width="2200" height="1536" alt="image" src="https://github.com/user-attachments/assets/036ce964-8343-45ec-967b-14718e607330" />

&nbsp;
---

5. Keep the Disk Capacity to __60 GB__. Then, make sure to select __Split virtual disk into multiple files.__
<img width="2192" height="1532" alt="image" src="https://github.com/user-attachments/assets/ab65cfc0-2901-40e0-8843-f1045e225994" />

&nbsp;
---
&nbsp;

6. Select __Customize Hardware..__
<img width="2210" height="1530" alt="image" src="https://github.com/user-attachments/assets/5ee338c7-a788-46d8-acf8-e3b8e1c8e710" />

&nbsp;
---
&nbsp;

7. Set the following:
  - Memory: __8GB__
  - Processors: __4 Processor, 2 Cores/Per__
  - CD/DVD:__Use ISO Image File (Attach the ISO of Windows Server EVAL 2022)__
  - Network Adapter: __Bridge (Replicate)__
    - Add an additional Network Adapter:
      - __Network Adapter 2: NAT__
  Then select __Close__
<img width="2327" height="2016" alt="image" src="https://github.com/user-attachments/assets/318223ed-ff8e-4f92-a6af-4610f3497e3e" />

&nbsp;
---
&nbsp;

8. Finally, __Finish__ the setup
<img width="2201" height="1544" alt="image" src="https://github.com/user-attachments/assets/4f46ac54-c505-44e8-9905-0571e363e011" />

&nbsp;
---
&nbsp;

9. Before we can start the VM, we will __add 4 additional Hard Disks__ for another lab. Select __Edit Virtual Machine Settings__
<img width="2210" height="1530" alt="image" src="https://github.com/user-attachments/assets/41ba31bd-c583-4692-9fee-a0dc648df384" />

&nbsp;
---
&nbsp;

10. __Add__ Hardware. Then, select __Hard Disk__.
<img width="2366" height="2019" alt="image" src="https://github.com/user-attachments/assets/9d9701a5-bace-4a13-9904-1e2973aa3e81" />

&nbsp;
---
&nbsp;

11. Select the following settings:
  - Disk Type: __NVMe__
  - Select a Disk: __Create a new virtual disk__
  - Maximum Disk size: __6 GB__. Then __Split virtual disk into multiple files__
  - Leave the name at default.
  - Then __Finish__

Simply repeat this process to add 3 more hard disks with the following sizes: __7 GB__, __8 GB__, __9 GB__

Expected output:

<img width="2344" height="2016" alt="image" src="https://github.com/user-attachments/assets/4a46cc72-711a-405a-86bc-75e40a8bff8b" />

&nbsp;
---
&nbsp;

12. Finally, we can __Power On__ the virtual machine.
> [!Warning]
> Once the virtual machine is powered on, you __MUST__ click on the __Center__ of the VM. Then, press __Enter__ otherwise you will have to restart the VM.

<img width="1767" height="1441" alt="image" src="https://github.com/user-attachments/assets/eac9925e-0fcb-4761-b69d-4189f5c05ef7" />

&nbsp;
---
&nbsp;

13. When booted successfully, leave the language to default. Then, select __Next__ and __Install Now__
<img width="2143" height="1950" alt="image" src="https://github.com/user-attachments/assets/e059b1cf-9f44-4253-b11e-d1a0b45c85f6" />

&nbsp;
---
&nbsp;

14. For Operationg system, select the 2nd option __Windows Server 2022 Standard Evaluation (Desktop Experience)__
<img width="2139" height="1954" alt="image" src="https://github.com/user-attachments/assets/595aa7c9-cf57-4907-983b-ccf05b4f53f2" />

&nbsp;
---
&nbsp;

15. __Accept__ the license terms.
<img width="2139" height="1967" alt="image" src="https://github.com/user-attachments/assets/789fda49-a2d5-4c22-8baa-380c7ae7f266" />

&nbsp;
---
&nbsp;

16. Choose __Custom Install__
<img width="2142" height="1956" alt="image" src="https://github.com/user-attachments/assets/bb0fe5d8-73fe-491c-b1af-75aa2855aa40" />

&nbsp;
---
&nbsp;

17. Select __Drive 0__. Then, simply wait for the installation to finish.
> [!Note]
> The system will restart after installation.

<img width="2142" height="1950" alt="image" src="https://github.com/user-attachments/assets/e7746340-516d-4695-baf4-12f53b77a615" />
<img width="2136" height="1959" alt="image" src="https://github.com/user-attachments/assets/55e0f869-4e28-474b-8b30-4fbc4116214c" />

&nbsp;
---
&nbsp;

18. Set a password for the Administrator account. __C1sc0123__
<img width="2138" height="1953" alt="image" src="https://github.com/user-attachments/assets/fdc6f705-d1fe-407a-8f19-ee3236350b5b" />

&nbsp;
---
&nbsp;

19. Use CTRL + ALT + INSERT to login to the VM

<br>
<br>

---
&nbsp;

## Setup Winserver 2022 for network services.
### 1. Turn off the firewall

~~~powershell
@powershell
set-netfirewallprofile -name public,private,domain -enabled false
~~~

Verify:

~~~powershell
@powershell
get-netfirewallprofile
~~~

&nbsp;
---
&nbsp;

### 2. Set proper IP addressing.
Open the __Run__ window by pressing `Windows + R` button. Then enter `ncpa.cpl`
<img width="2137" height="1943" alt="image" src="https://github.com/user-attachments/assets/6b691204-97bb-482f-a63e-d192fdfcc728" />

<br>

First off, we need to verify which Network Adapter is connected to __NAT__, and which one is connected to __Bridge__.
To achieve this, __right click__ on one of the LAN Cards of the virtual machine. Then, select __Disconnect__.
<img width="2149" height="2014" alt="image" src="https://github.com/user-attachments/assets/4f3473a0-ff27-403b-b33c-eb8733f75000" />

When disconnected, one of the Network Adapters within the Virtual Machine will be __unplugged__
<img width="2132" height="1946" alt="image" src="https://github.com/user-attachments/assets/2d9520cf-c5cc-4129-b31b-77fba6fc72bf" />

That means, the LAN card we disconnected is the one that's connected to the VMs network adapter. In this example, the __Bridged LAN__ was disconnected, which means the __Ethernet0__ is the bridged connection.

For the sake of convenience, rename the network adapter as follows:
| LAN Card | WinServer Network Adapter |
| ---      | ---                       |
| Bridged  | TunayNaLAN                |
| NAT      | TunayNaWIFI               |

> [!Note]
> Don't forget to reconnect the LAN Card

Expected output:
<img width="2137" height="1963" alt="image" src="https://github.com/user-attachments/assets/92f6adc1-12e4-40d2-9d6d-0bb939e62fd2" />




### 3. 
