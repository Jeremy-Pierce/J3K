# J3K

## Project Overview

We founded a people-first DAO titled J3K with a goal to help those we serve achieve financial freedom in a secure, smart, and efficient way. This mission is firmly grounded through the minting and offering of J3KOIN.  J3KOIN is a fungible token built for the block chain utilizing solidity, smart contracts, streamlit, a Crowdsale, and the Polygon Network.  On September 22nd, 2022, J3K took a big step forward in helping bridge communities and assets worldwide with the launching of J3KOIN's Crowdsale.  J3KOIN went live on the Polygon Network and is available globally.  Post launch of J3KOIN, we were excited to see we had our first community transfer of J3KOIN via the Polygon Network from Columbia to the United States.  We are excited about the possiblities J3K and J3KOIN can deliver for people.    


## Technologies for Solidity

pragma solidity ^0.5.0;

import "./J3Koin_mintable.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

## Technologies for Python

import os

import json

import re

from web3 import Web3

from pathlib import Path

from dotenv import load_dotenv

import streamlit as st

import pandas as pd

from decimal import Decimal

## Usage


If you would like to see our full, interactive slide deck, we have included a Link to our [presentation][1]

[1]:https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

[Who is J3K?](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#3)

[J3KOIN Crowdsale Timeline](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#6)

[J3KOIN Crowdsale Smart Contract with Solidity](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#7)

[J3KOIN Token Smart Contract with Solidity](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#8)

[J3KOIN Deployed Smart Contract within IDE Remix Dev Environment](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#9)

[Purhcasing J3KOIN with IDE Remix Dev Environment](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#9)

[Transferring J3KOIN from one Metamask Account to another Metamask Account](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#11)

