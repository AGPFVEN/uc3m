library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

---------
--Entity
---------
entity q2 is port(
    --Inputs
    a:    in std_logic;
    b:    in std_logic;

    --Output
    result: out std_logic;
);
end q2;

------------
--Architecture
------------
architecture behaviour of q2 is
    --signals
    signal ab: std_logic_vector(1 downto 0);
    signal ab <= a & b;

    --State declaration
    type state is (s1, s2, s3, s4);
    signal current_state, next_state: state;

    begin
        --state changer
        process(clk, reset) begin
            if reset = '0' then
                current_state <= s1;
            elsif clk'event and clk = '1' then
                current_state <= next_state;
            end if;
        end process;

        --State Machine behaviour
        process(current_state) begin
            case current_state is 
                when s1 =>
                    result <= '0';

                    if a = '0' then
                        next_state <= s1;
                    else
                        next_state <= s2;
                    end if;

                when s2 =>
                    result <= '0';

                    if ab = "00" then
                        next_state <= s2;
                    elsif ab = "01" then
                        next_state <= s3;
                    elsif ab = "10" then
                        next_state <= s3;
                    else 
                        next_state <= s4;
                    end if;

                when s3 =>
                    result <= '0';
                    
                    if a = 1 then
                        next_state <= s3;
                    else 
                        next_state <= s4;
                    end if;
                
                when s4 =>
                    result <= '1';

                    if ab = "00" or ab = "11" then
                        next_state <= s4;
                    elsif ab = "01" then
                        next_state <= s3;
                    elsif ab = "10" then
                        next_state <= s1;
                    end if;
                end case;
            end process;
    end behaviour;
