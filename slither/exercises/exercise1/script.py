import sys
from slither import Slither

# Init slither
slither = Slither('coin.sol')

for contract in slither.contracts:
    if contract.name != "Coin":
        for function in contract.functions: 
            if "mint" in function.full_name:
                for c in contract.inheritance:
                    print(c.name)
                    if c == "Coin":
                        print("BUG")
                        exit()

