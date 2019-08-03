from manticore.ethereum import ManticoreEVM, ABI
from manticore.core.smtlib import Operators


m = ManticoreEVM()

with open('token.sol') as f:
    source_code = f.read()

# create one account
user_account = m.create_account(balance=1000)
contract_account = m.solidity_create_contract(source_code, owner=user_account, balance=0)

symbolic_token_amount = m.make_symbolic_value()
symbolic_wei_amount = m.make_symbolic_value()
# Transfer is called with symbolic values
contract_account.is_valid_buy(symbolic_token_amount, symbolic_wei_amount)

bug_found = False
# Explore all the forks
for state in m.ready_states:

    condition_1 = (symbolic_wei_amount == 0)
    condition_2 = (symbolic_token_amount >= 1)
    condition = Operators.AND(condition_1, condition_2)
    if m.generate_testcase(state, name="BugFound", only_if=condition):
        print("Bug found! see {}".format(m.workspace))
        bug_found = True

    if not bug_found:
        print('No bug were found')

