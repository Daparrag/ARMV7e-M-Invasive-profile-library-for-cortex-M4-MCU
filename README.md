# ARMV7e-M invasive profile library for cortexM4 MCU
This is a simple library used for make a profile of your applications in the cortex M4 micro controller.


<img src="https://github.com/Daparrag/ARMV7e-M-Invasive-profile-library-for-cortex-M4-MCU/blob/master/Screenshots/profiling.png" alt="Profile Semihosting Architecture" width="1000px" />


this library exploites the Semihosting capabilities present in the Cortex-M4 microcontroller's family  and the  **no_instrument_function** gnu-facilities for acquire the pair  **Call and Called functions adresses**.

As well it includes **a simple counter** used for calculate an aproximated **number of cycles** spended in each function's in execution. At the end a **XML file** is generated with all the profile information Allowing an easy visualization independent of the platform used by his analysis. 

**Note**:
**This is the first version** of this library, therefore you are welcome to modified it, and report any issue. I'm working on this in my free time that's why I will try to update some documentation soon and improve the code.

Form my point of view this is no an effcient implmentation since I'm using a tree for allocate the diferent *calling paths* ut is interesting because there is no any open source implementation of profiling for this MCU family explioting the semihosting communication in the DBG mode.  

**thanks and enyoing**

