library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

---------
--Entity
---------
entity die is 
    port(
        --inputs
        clk:     in std_logic; --Clock input
        reset:   in std_logic; --Asynchronous clear
        e:       in std_logic; --Enable input

        --outputs
        q: out std_logic_vector(2 downto 0); --Count value (3 bits)
    );
end die;

architecture electronic of die is
    --Signals
    signal count: integer range 0 to 5;

    --Timer
    begin process(clk, reset) begin
        if reset = '1' then
            count <= '0';
        elsif clk'event and clk = '1'then
            if e = '1' then
                count <= count + 1;
            else
                q <= std_logic_vector(to_unsigned(count, 3));
                count <= '0';
            end if;
        end if;
    end process;

end electronic;