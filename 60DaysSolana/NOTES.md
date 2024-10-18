# Notes: 60 Days of Solana


## Day 2

- By default, a transaction is limited to 200,000 compute units. If this limit
is exceded, the transaction reverts.
- To save compute cost, set `overflow-checks` at `Cargo.toml` to `false` and
strategically defend against overflows in key junctures 
- `ERROR: account data too small for instruction`
[StackOverflow](https://stackoverflow.com/questions/71267943/solana-deploy-account-data-too-small-for-instruction)


## Day 3

- An `IDL file` in Solana plays a similar role as the ABI file in Solidity,
specifying how to interact with the program’s/contract’s.

