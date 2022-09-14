pragma solidity ^0.5.0;

import "./J3Koin_mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";


// Have the KaseiCoinCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract J3KoinCrowdsale is Crowdsale, MintedCrowdsale { // UPDATE THE CONTRACT SIGNATURE TO ADD INHERITANCE
    
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint rate,
        address payable wallet,
        J3Koin token

    ) public Crowdsale(rate, wallet, token) {
        // constructor can stay empty
    }
}


contract J3KCrowdsaleDeployer {
    // Create an `address public` variable called `kasei_token_address`.
    address public j3koin_token_address;
    // Create an `address public` variable called `kasei_crowdsale_address`.
    address public j3koin_crowdsale_address;

    // Add the constructor.
    constructor(
       string memory name,
       string memory symbol,
       address payable wallet
    ) public {
        // Create a new instance of the KaseiCoin contract.
        J3Koin token = new J3Koin(name, symbol, 0);
        
        // Assign the token contract’s address to the `kasei_token_address` variable.
        j3koin_token_address = address(token);

        // Create a new instance of the `KaseiCoinCrowdsale` contract
        J3KoinCrowdsale j3koin_crowdsale  = new J3KoinCrowdsale(1, wallet, token); 
            
        // Aassign the `KaseiCoinCrowdsale` contract’s address to the `kasei_crowdsale_address` variable.
        j3koin_crowdsale_address = address(j3koin_crowdsale);

        // Set the `KaseiCoinCrowdsale` contract as a minter
        token.addMinter(j3koin_crowdsale_address);
        
        // Have the `KaseiCoinCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}
