library ieee;
use ieee.std_logic_1164.all;
entity exercise1 is
    port (
        A, B, C: IN STD_LOGIC;
        S0, S1: OUT STD_LOGIC;
    );
end exercise1;
    
architecture circuit1 of exercise1 is
    signal X: std_logic;

    begin
        X <= (A nor B) or (not C);