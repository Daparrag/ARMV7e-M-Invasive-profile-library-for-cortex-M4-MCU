# ARMV7e-M invasive profile library for cortexM4 MCU
This is a simple library used to profile of your applications in the cortex M4 micro controller.


<img src="https://github.com/Daparrag/ARMV7e-M-Invasive-profile-library-for-cortex-M4-MCU/blob/master/Screenshots/profiling.png" alt="Profile Semihosting Architecture" width="1000px" />


this library makes use of Semihosting capabilities in the Cortex-M4 microcontroller's family, additionally uses the **no_instrument_functions** provided by the gnu compiler that returns two address  **(Call and Called function addresses)**.

As well it includes **a simple counter** used to approximate the **number of cycles** spending by each function. At the end the library returns a **XML file** with the whole profile information to be visualized by and external platform. 

**GUI**

The view of information had been done through a graphical user interface able to parse the XML and
showing the results in a friendly tree-table. This table contains: name of a function, number of cycles, 
and the address associated.

<img src="https://github.com/Daparrag/ARMV7e-M-Invasive-profile-library-for-cortex-M4-MCU/blob/master/Screenshots/GUI.jpg" alt="Profile Semihosting GUI" width="800px" /> 

**Note**:
**This is the first version** of this library, therefore you are welcome to  use, change or report any issue. I'm working on this during my free time and therefore I'll try to  update documentation soon and improve the code.

Form my point of view this is no an efficient implementation since I'm using a tree data-structure to allocate the different *calling paths* it is interesting because there is no any open source implementation of profiling for this MCU family exploiting the semihosting communication in the DBG mode.  
   


**thanks and enyoing**

