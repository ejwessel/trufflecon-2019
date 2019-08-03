from manticore.ethereum import ManticoreEVM
from manticore.core.smtlib import Operators, solver
from manticore.ethereum.abi import ABI

m = ManticoreEVM() # initiate the blockchain

# Generate the accounts
user_account = m.create_account(balance=1000)
with open('overflow.sol') as f:
    contract_account = m.solidity_create_contract(f, owner=user_account)

#First add won't overflow uint256 representation
x = m.make_symbolic_value()
contract_account.add(x, caller=user_account)
#Potential overflow
y = m.make_symbolic_value()
contract_account.add(y, caller=user_account)
contract_account.sellerBalance(caller=user_account)

bug_found = False

# Explore all the forks
for state in m.ready_states:
    # if z is less than x then y never added properly
    end_val = state.platform.transactions[-1].return_data
    end_val = ABI.deserialize("uint", end_val)

    condition = Operators.ULT(end_val, x)
    if m.generate_testcase(state, name="BugFound", only_if=condition):
        print("Bug found! see {}".format(m.workspace))
        bug_found = True

if not bug_found:
    print('No bug were found')





