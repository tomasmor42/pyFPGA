from myhdl import (always, block, Signal,
    toVerilog, traceSignals, delay, Simulation)

@block
def dff(d, f, clk):
    @always(clk.posedge)
    def logic():
        d.next = f

    return logic

def convert():
    d, f, clk = [Signal(bool(0)) for i in range(3)]
    top_dff = dff(d, f, clk)
    top_dff.convert(hdl="Verilog", initial_values=True)

from random import randrange

def test_dff():
    d, f, clk = [Signal(bool(0)) for i in range(3)]
    dff_inst = dff(d, f, clk)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @always(clk.negedge)
    def stimulus():
        f.next = randrange(2)

    return dff_inst, clkgen, stimulus

def simulate(timesteps):
    tb = traceSignals(test_dff)
    sim = Simulation(tb)
    sim.run(timesteps)


if __name__ == '__main__':
    #simulate(2000)
    convert()
