FPGA talk plan 
? Who knows what FPGA is? 
? Who has been working with FPGA before? 
? Who done it with Python? 

* FPGA — what is it 
* Why FPGA
    * Fast 
    * Easy to use
    * Parallel computing
```FPGAs really shine when it comes to doing things like vector mathematics computations. Vector math isn’t just for physics class: Programmers use it whenever they have to perform the same operation on each one of a large set of numbers.  If you have a 128-element matrix, you can build 128 arithmetic “pipelines” so all these operations can execute simultaneously, giving you huge gains in performance and power usage. 

```
* How is it used and why today it’s even more popular 
* How does it work from the inside 
    * Beads and string metaphor
* Fields where FPGA is more commonly used (partly because it’s just a common parts that are shared over the years):
    * network data I/O
    * graphics processing 
    * microprocessors
* Steps of creating FPGA 
    * Design 
    * Implementation 
    * Debugging (with simulators)
* Verilog & vhdl
    * Hardware Describing Language 
    * Verilog https://github.com/seldridge/verilog/blob/master/sim/t_sqrt_generic.v (nice and readable example)
* Nobody knows HDL but want to develop for FPGA
    * OpenCL
    * Python and FPGA
* Testing 
* PYNQ 
* Getting started with PYNQ
* MyHDL
* Getting started withMyHDL

