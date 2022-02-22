library ieee;
use ieee.std_logic_1164.all;

entity problem3 is
    port (
        x, s1, s2, s3: in std_logic;
        p1, p2, p3: out std_logic
    );
end problem3;

architecture a of problem3 is
    --begin
        --process(s1, s2, s3)
        --begin
            --p3 <= s3;
            --p1 <= (s3 nor s2) & s1;
            --p2 <= ((s3 nor s1) & s2) or ((s2 & s1) & (not s3))
        --end process;
    --declare signals
    begin
        --describe
        process(x, s1, s2, s3)
        begin 
            if x = '1' then
                p1 <= '1';
                p2 <= '1';
                p3 <= '1';

            elsif s1 = '0' and s2 = '0' and s3 = '0' then
                p1 <= '0';
                p2 <= '0';
                p3 <= '0';

            elsif s1 = '1' and (s2 = '1' or s3 = '1') then
                p1 <= '0';
                p2 <= '0';
                p3 <= '1';

            elsif s1 = '1' and s2 = 
    
    end a;