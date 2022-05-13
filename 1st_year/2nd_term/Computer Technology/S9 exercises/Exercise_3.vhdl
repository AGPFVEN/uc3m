library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
--Moore machine

--------
--Entity
--------
entity finite_state_machine is 
    port(
        --Inputs
        reset : in std_logic; --Asynchronous clear
        clk:    in std_logic; --Clock input
        e:      in std_logic; --1 bit

        --Outputs
        s:      out std_logic_vector(1 downto 0);
    );
end finite_state_machine;

--------------
--Architecture
--------------
architecture behaviour of finite_state_machine is 
    --Signals
    type state is (s0, s1, s2, s3, s4, s5);
    signal previous_state ,current_state, next_state: state;

    begin
        --State changer
        process(clk, reset) begin
            if reset = '1' then
                current_state <= s0;
            elsif clk'event and clk = '1' then
                if e = '1' then
                    current_state <= next_state;
                elsif e = '0' then
                    current_state <= previous_state;
                end if;
            end if;
        end process

        --Diagram behaviour
        process(current_state) begin
            case current_state  is
                when s0 =>
                    previous_state <= s0;
                    next_state     <= s1;
                    s              <= "00";
                when s1 =>
                    previous_state <= s4;
                    next_state     <= s2;
                    s              <= "00";
                when s2 =>
                    previous_state <= s2;
                    next_state     <= s3;
                    s              <= "01";
                when s3 =>
                    previous_state <= s5;
                    next_state     <= s4;
                    s              <= "10";
                when s4 =>
                    previous_state <= s5;
                    next_state     <= s2;
                    s              <= "11";
                when s5 =>
                    previous_state <= s2;
                    next_state     <= s1;
                    s              <= "01";
            end case;
        end process;
    end behaviour;