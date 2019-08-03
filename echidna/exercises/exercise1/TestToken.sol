pragma solidity ^0.5.3;

import "token.sol";

contract TestToken is Token {
    constructor() public {
        paused(); //pause the contract 
        owner = address(0x0); //lose ownership
    }

    //add property
    function echidna_unpause() public returns(bool) {
        return is_paused;
    }
}
