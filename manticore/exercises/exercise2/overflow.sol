pragma solidity^0.5.3;

contract Overflow {
    uint public sellerBalance=0;

    function add(uint value) public returns (bool){
        uint checkpoint_val = sellerBalance;
        sellerBalance += value; // complicated math, possible overflow
        require(checkpoint_val < sellerBalance);
    }
}
