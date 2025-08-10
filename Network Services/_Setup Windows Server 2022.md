
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

11. Select the following settings:
  - Disk Type: __NVMe__
  - Select a Disk: __Create a new virtual disk__
  - Maximum Disk size: __6 GB__. Then __Split virtual disk into multiple files__
  - Leave the name at default.
  - Then __Finish__

Simply repeat this process to add 3 more hard disks with the following sizes: __7 GB__, __8 GB__, __9 GB__

Expected output:

<img width="2344" height="2016" alt="image" src="https://github.com/user-attachments/assets/4a46cc72-711a-405a-86bc-75e40a8bff8b" />
