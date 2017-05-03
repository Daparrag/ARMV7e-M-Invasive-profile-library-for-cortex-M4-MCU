# ARMV7e-M-invasive-profile-library-for-cortex-M4-MCU
This is a simple library used for make a profile of your applications in the cortex M4 micro controller.


This is a library which exploites the Semihosting capabilities present in the Cortex-M4 microcontroller family this library implement the  no_instrument_function facilities for acquire the pair of address of the function who call and the function called, as well a simple counter of the microcontroller is used for calculate the aproximate cycles spended in the execution of each function.

At the end a XML file is generated making easy its visulization. 

Note:
This is the first version of this library, therefore you are welcome to modified it, and report any issue. I'm working on this in my free time that's why I will try to update some documentation soon and improve the code.

Form my point of view this is no an effcient implmentation since I'm using a tree for allocate the diferent "calling paths" but is interesting because there is no any open source implementation of profiling for this MCU family explioting the semihosting communication in the DBG mode.  

