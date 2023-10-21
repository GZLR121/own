import json
from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.default_account = web3.eth.accounts[0]
abi = json.loads('[{"inputs":[],"name":"Greeter_2","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode = '608060405234801561001057600080fd5b506004361061004c5760003560e01c8063a413686214610051578063cfae32171461006d578063d88ae65e1461008b578063ef690cc014610095575b600080fd5b61006b60048036038101906100669190610387565b6100b3565b005b6100756100c6565b604051610082919061044f565b60405180910390f35b610093610158565b005b61009d61019f565b6040516100aa919061044f565b60405180910390f35b80600090816100c29190610687565b5050565b6060600080546100d5906104a0565b80601f0160208091040260200160405190810160405280929190818152602001828054610101906104a0565b801561014e5780601f106101235761010080835404028352916020019161014e565b820191906000526020600020905b81548152906001019060200180831161013157829003601f168201915b5050505050905090565b6040518060400160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908161019c9190610687565b50565b600080546101ac906104a0565b80601f01602080910402602001604051908101604052809291908181526020018280546101d8906104a0565b80156102255780601f106101fa57610100808354040283529160200191610225565b820191906000526020600020905b81548152906001019060200180831161020857829003601f168201915b505050505081565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6102948261024b565b810181811067ffffffffffffffff821117156102b3576102b261025c565b5b80604052505050565b60006102c661022d565b90506102d2828261028b565b919050565b600067ffffffffffffffff8211156102f2576102f161025c565b5b6102fb8261024b565b9050602081019050919050565b82818337600083830152505050565b600061032a610325846102d7565b6102bc565b90508281526020810184848401111561034657610345610246565b5b610351848285610308565b509392505050565b600082601f83011261036e5761036d610241565b5b813561037e848260208601610317565b91505092915050565b60006020828403121561039d5761039c610237565b5b600082013567ffffffffffffffff8111156103bb576103ba61023c565b5b6103c784828501610359565b91505092915050565b600081519050919050565b600082825260208201905092915050565b60005b8381101561040a5780820151818401526020810190506103ef565b60008484015250505050565b6000610421826103d0565b61042b81856103db565b935061043b8185602086016103ec565b6104448161024b565b840191505092915050565b600060208201905081810360008301526104698184610416565b905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b600060028204905060018216806104b857607f821691505b6020821081036104cb576104ca610471565b5b50919050565b60008190508160005260206000209050919050565b60006020601f8301049050919050565b600082821b905092915050565b6000600883026105337fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826104f6565b61053d86836104f6565b95508019841693508086168417925050509392505050565b6000819050919050565b6000819050919050565b600061058461057f61057a84610555565b61055f565b610555565b9050919050565b6000819050919050565b61059e83610569565b6105b26105aa8261058b565b848454610503565b825550505050565b600090565b6105c76105ba565b6105d2818484610595565b505050565b5b818110156105f6576105eb6000826105bf565b6001810190506105d8565b5050565b601f82111561063b5761060c816104d1565b610615846104e6565b81016020851015610624578190505b610638610630856104e6565b8301826105d7565b50505b505050565b600082821c905092915050565b600061065e60001984600802610640565b1980831691505092915050565b6000610677838361064d565b9150826002028217905092915050565b610690826103d0565b67ffffffffffffffff8111156106a9576106a861025c565b5b6106b382546104a0565b6106be8282856105fa565b600060209050601f8311600181146106f157600084156106df578287015190505b6106e9858261066b565b865550610751565b601f1984166106ff866104d1565b60005b8281101561072757848901518255600182019150602085019450602081019050610702565b868310156107445784890151610740601f89168261064d565b8355505b6001600288020188555050505b50505050505056fea26469706673582212203fa913b8984e3305c1edb7aac3dce41b3ca70d2ac15dcd0dfaa4c712a20e758d64736f6c63430008120033'

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()
print(tx_hash)
"tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)"

#"contract = web3.eth.contract(
    #"address=tx_receipt.contractAddress,
    #"abi=abi"

")"

#"print(contract.functions.greet().call())