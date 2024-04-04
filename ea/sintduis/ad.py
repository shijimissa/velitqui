# Optimized Smart Contract Transaction Code

# Assuming 'web3' has been imported and initialized
from web3 import Web3

# Assuming 'contract' is already instantiated Web3 Contract object
# and 'account' is a Web3 Account object for the sender

# Set the transaction parameters
transaction = {
    'nonce': nonce,
    'gasPrice': Web3.toWei(gas_price, 'gwei'),  # Convert gas price from Gwei to Wei for accuracy
    'gas': gas,
    'from': account.address  # Specify the sender's address
}

# Build the transaction with the swap function
contract_txn = contract.functions.swap(
    amount0_out,
    amount1_out,
    to,
    data
).buildTransaction(transaction)

# Sign the transaction
signed_txn = web3.eth.account.signTransaction(contract_txn, account.privateKey)

# Send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

# Get the transaction receipt (optional, if you want to wait for confirmation)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Output the transaction hash
print(f"Transaction hash: {tx_hash.hex()}")
