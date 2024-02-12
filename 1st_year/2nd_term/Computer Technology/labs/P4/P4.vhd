library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

--------
--Entity
--------

entity P4 is
    port(
        --Inputs
        clk:    in std_logic;
        button: in std_logic;

        --Outputs
        red:   out std_logic;
        amber: out std_logic;
        green: out std_logic
    );
end P4;

---------------
--Architecture
---------------
architecture traffic_light_controller of P4 is
    --SIGNALS
        --Edge detector
    signal reg1      : std_logic;
    signal reg2      : std_logic;
    signal button_e  : std_logic;

        --Timer
    signal count       : unsigned(2 downto 0);
    signal E           : std_logic; -- Enable
    signal F           : std_logic; -- End of count
    signal reset       : std_logic := '0';

        --State Changer
    type state is (amber_state, green_state, red_state);
    signal current_state, next_state: state;

    begin
        --Default setting of the clock
        defau: process(clk, reset)
        begin
            if reset = '1' then
                current_state <= green_state;
            elsif clk'event and clk = '1' then
                current_state <= next_state;
            end if;
        end process;

        --Edge Detector
        ed: process(reset, clk)
            begin
                if reset = '1' then
                    reg1 <= '0';
                    reg2 <= '0';
                elsif clk'event and clk = '1' then
                    reg1 <= button;
                    reg2 <= reg1;
                end if;

            button_e <= reg1 and (not reg2);
        end process;

        --Timer
        timer: process(reset, clk, E)
            begin
                if reset = '1' then
                    count <= "000";
                elsif clk'event and clk = '1' then
                    if E = '1' then
                        if count = "100" then
                            count <= "000";
                        else
                            count <= count + 1;
                        end if;
                    else
                        if count /= "000" and count /= "100" then
                            count <= count + 1;
                        else
                            count <= "000";
                        end if;
                    end if;
                end if; 
        end process;
        
        --Stop counting
        F <= '1' when
        count = "100" else '0';

        --State Machine
        State_machine: process(button_e, current_state, F)
        begin
            case current_state is
                when red_state    =>
                    green <= '0';
                    amber <= '0';
                    red   <= '1';

                    if F = '1' then
                        next_state <= green_state;
                        E          <= '0';
                    else
                        next_state <= red_state;
                    end if;

                    E <= '1';
                
                when amber_state  =>
                    green <= '0';
                    amber <= '1';
                    red   <= '0';

                    E     <= '1';

                    if F = '1' then
                        next_state <= red_state;
                    else
                        next_state <= amber_state;
                    end if;
                    
                when green_state  =>
                    green <= '1';
                    amber <= '0';
                    red   <= '0';

                    if button_e = '1' then
                        E <= '1';
                    else
                        E <= '0';
                    end if;

                    if F = '1' then
                        next_state <= amber_state;
                    else
                        next_state <= green_state;
                    end if;
            end case; 
        end process;
    end traffic_light_controller;