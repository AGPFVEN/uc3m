library ieee;
use ieee.std_logic_1164.all;
entity exercise1 is
    port (
        A, B, C: IN STD_LOGIC;
        s0, s1: OUT STD_LOGIC;
    );
end exercise1;
    
architecture circuit1 of exercise1 is
    signal X: std_logic;
    begin
        process(A, B, C)
        begin
            X <= (A nor B) or (not C); --Define X

            --Decoder
            if x = '0' then
                s0 <= '1';
                s1 <= '0';
            else
                s0 <= '0';
                s1 <= '1';
            end if;
        end process;
    end circuit1;