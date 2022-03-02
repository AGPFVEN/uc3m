library ieee;
use ieee.std_logic_1164.all;

entity problem4 is
    port(
        A, B: in std_logic;
        K, Q in std_logic_vector(2 downto 0);
        X out std_logic;
        P out std_logic_vector(2 downto 0)
    );
end problem4;