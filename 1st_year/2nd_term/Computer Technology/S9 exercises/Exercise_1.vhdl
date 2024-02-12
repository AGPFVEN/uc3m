library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

---------
--Entity
---------
entity Ex1 is port(
    --Inputs
    clk:    in std_logic;                    --Clock
    reset:  in std_logic;                    --Asynchronous clear
    s:      in std_logic_vector(1 downto 0); --Mode select input
    d:      in std_logic_vector(3 downto 0); --Data input for parallel load
    es:     in std_logic_vector(1 downto 0); --Serial data imnput

    --Outputs
    q:      out std_logic_vector(3 downto 0) --Register output
    ss:     out std_logic_vector(1 downto 0) --Serial data output
);

---------------
--Architecture
---------------
architecture shift_register of Ex1 is
    --Signals
    begin
        process(clk, reset) begin
            if reset = '1' then
                s <= "0000"
            elsif clk'event and clk = '1' then
                