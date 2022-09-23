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

### Theme for Streamlit:

[theme]

primaryColor="#FBD400"

backgroundColor="#000000"

secondaryBackgroundColor="#000000"

textColor="#FFFFFF"

font="sans serif"

font-size='150%'

## Usage

![J3KOIN](https://github.com/kcrachapudi/J3K/blob/main/J3Koin-Logo-small.png)

If you would like to see our full, interactive slide deck, we have included a Link to our [presentation][1]

[1]:https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

[Who is J3K?](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#3)

[J3KOIN Crowdsale Timeline](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#6)

Presentation Link to [J3KOIN Crowdsale Smart Contract with Solidity](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#7)

### J3KOIN Crowdsale Contract
![Crowdsale Contract](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/crowdsaleContract.png)

[J3KOIN Token Smart Contract with Solidity](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#8)

### J3KOIN Token Smart Contract
![J3KOIN Token Smart Contract](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/tokenContract.png)

Presentation link to see a video of [J3KOIN Deployed Smart Contract within IDE Remix Dev Environment](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#9)

Github link to the ![J3KOIN Deployeed Smart Contract within IDE Remix Dev Environment](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/deploy.mov)

Presentation link to see a video of [Purhcasing J3KOIN with IDE Remix Dev Environment](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#10)

Github link to see a video of ![Purchasing J3KOIN with IDE Remix Dev Environment](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/purchase.mov)

### J3KOIN account balance on dev environment metamask
![J3KOIN Account Balance on Metamask](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/account7Balance.png)

Presentation link to see video of [Transferring J3KOIN from one Metamask Account to another Metamask Account](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#11)

Github link to see a video of [Transferring J3KOIN from one Metamaks Account to another Metamask Account](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/transfer.mov)

### J3KOIN recieved by another account on metamask with the dev envrionment
![J3KOIN Account Recieved on Metamask](https://github.com/kcrachapudi/J3K/blob/main/Media/J3Koin_supportingMedia/account4Recieve.png)

Presentation link to see a video of [J3KOIN User Interface utilizing Python and Streamlit](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#12)

Github link to see a video of [J3KOIN User Interface utilizing Python and Streamlit](https://github.com/kcrachapudi/J3K/blob/main/Media/J3K-Streamlit-Demo.webm)

Presentation link to the [Introduction and Benefits of the Polygon Network](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#13)

![Introduction and Benefits of the Polygon Network](

Presentation link to [J3KOIN Live on the Polygon Network!!](https://www.canva.com/design/DAFMqis6x3s/h14EbDxPtMhpMsBDZAeYTw/view?utm_content=DAFMqis6x3s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton#14)

![J3KOIN live on the Polygon Network!!](


## Contributors

Jay Wiley

Jeremy Pierce

James Willis

Kalyan Rachapudi


