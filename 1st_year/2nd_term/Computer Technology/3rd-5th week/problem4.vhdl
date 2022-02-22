library ieee;
use ieee.std_logic_1164.all;

entity problem4 is
    port(
        A, B, Q: in std_logic;
        K in bit_vector;
        X out std_logic;
        P out bit_vector
    );
end problem4;