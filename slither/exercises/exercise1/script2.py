import sys
from slither import Slither

# Init slither
slither = Slither('coin.sol')

whitelist = ["_mint(address,uint256)"]

for contract in slither.contracts:
    for function in contract.functions:
        # look for public and external functions to call onlyOwner
        if(function.full_name in whitelist):
            continue
        if(function.visibility == "public" or function.visibility == "external"):
            if("onlyOwner" not in function.modifiers):
                print('%s.%s is not in whitelist for onlyOwner' % (contract.name, function.full_name))
