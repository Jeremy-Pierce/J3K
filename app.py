import os
import json
import re
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from decimal import Decimal

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

deployer_contract_path = './contracts/compiled/J3Koin_abi.json'
crowdsale_contract_path = './contracts/compiled/J3Koin_crowdsale_abi.json'
token_contract_path = './contracts/compiled/J3Koin_token_abi.json'
deployer_contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

@st.cache(allow_output_mutation=True)
def load_contract(path, contract_address):
    with open(Path(path)) as f:
        contract_abi = json.load(f)

    contract = w3.eth.contract(
        address = contract_address,
        abi = contract_abi
    )

    return contract

#st.title("Welcome to J3KOIN")
st.image('J3Koin-Logo.png')
st.markdown("---")

################################################################################
# Streamlit Style
st.markdown(""" <style> .orange-font { color: #FBD400; font-size: 300%; font-weight:bold} </style> """, unsafe_allow_html=True)
################################################################################


################################################################################
# Deployer Contract Details
################################################################################
st.markdown("<p class='orange-font' >Deployer Contract Details</P>", unsafe_allow_html=True)
st.markdown(f'Deployer Contract Address : {deployer_contract_address}')
deployer_contract = load_contract(deployer_contract_path, deployer_contract_address)

#breakpoint()

try:
    crowdsale_contract_address = deployer_contract.functions.j3koin_crowdsale_address().call()
    token_contract_address = deployer_contract.functions.j3koin_token_address().call()
except Exception as inst:
    print(f'Error in call to Deployer Contract Functions {inst}')

st.markdown(f'Crowdsale Contract Address : {crowdsale_contract_address}')
st.markdown(f'Token Contract Address : {token_contract_address}')

################################################################################
# Crowdsale
################################################################################
st.markdown("<p class='orange-font'>Crowdsale Contract Details</P>", unsafe_allow_html=True)
st.markdown(f'Crowdsale Contract Address : {crowdsale_contract_address}')
crowdsale_contract = load_contract(crowdsale_contract_path, crowdsale_contract_address)

#breakpoint()

try:
    crowdsale_contract_rate = crowdsale_contract.functions.rate().call()
    crowdsale_contract_token = crowdsale_contract.functions.token().call()
    crowdsale_contract_wallet = crowdsale_contract.functions.wallet().call()
    crowdsale_contract_weiRaised = crowdsale_contract.functions.weiRaised().call()
except Exception as inst:
    print(f'Error in call to Crowdsale Contract Functions {inst}')

st.markdown(f'Crowdsale Contract Rate : {crowdsale_contract_rate}')
st.markdown(f'Crowdsale Contract Token : {crowdsale_contract_token}')
st.markdown(f'Crowdsale Contract Wallet : {crowdsale_contract_wallet}')
st.markdown(f'Crowdsale Contract weiRaised : {crowdsale_contract_weiRaised}')

accounts = w3.eth.accounts
beneficiary_address = st.selectbox(label="Select Account", key='drpBenefAddress', options=accounts)
beneficiery_tokens = st.number_input("Number of Tokens Needed", value=0, step=1)
beneficiary_amount = beneficiery_tokens * crowdsale_contract_rate
if st.button("Buy Tokens"):
    print(f'Calling Crowdsale Contract Function buyTokens for Beneficiary {beneficiary_address} FromAddress {crowdsale_contract_wallet}')
    try:
        tx_hash = crowdsale_contract.functions.buyTokens(
            beneficiary_address
        ).transact({"from": crowdsale_contract_wallet, 'value': beneficiary_amount})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write(receipt)
    except Exception as ex1:
        print(f'Error in call to Crowdsale Contract Function buyTokens {ex1}')

################################################################################
# Token Details
################################################################################
st.markdown("<p class='orange-font'>Token Contract Details</P>", unsafe_allow_html=True)
st.markdown(f'Token Contract Address : {token_contract_address}')
token_contract = load_contract(token_contract_path, token_contract_address)

#breakpoint()

try:
    token_contract_name = token_contract.functions.name().call()
    token_contract_symbol = token_contract.functions.symbol().call()
    token_contract_totalSupply = token_contract.functions.totalSupply().call()
    token_contract_decimals = token_contract.functions.decimals().call()
except Exception as inst:
    print(f'Error in call to Token Contract Functions {inst}')

st.markdown(f'Token Contract name : {token_contract_name}')
st.markdown(f'Token Contract symbol : {token_contract_symbol}')
st.markdown(f'Token Contract totalSupply : {token_contract_totalSupply}')
st.markdown(f'Token Contract decimals : {token_contract_decimals}')


recipient_address = st.selectbox(label="Recipient Account", key='drpRecipientAddress', options=accounts)
transfer_tokens = st.number_input("Number of Tokens Needed", key='txtTransferTokens', value=0, step=1)
wallet_tokens = token_contract.functions.balanceOf(account=crowdsale_contract_wallet).call()
if st.button("Transfer"):
    if(deployer_contract_address != recipient_address):
        if(transfer_tokens<=wallet_tokens):
            try:
                print(f'Calling Token Contract Function transfer from Sender {crowdsale_contract_wallet} to Recipient {recipient_address}')
                tx_hash = token_contract.functions.transfer(
                    recipient_address,
                    transfer_tokens
                ).transact({"from": crowdsale_contract_wallet})
                receipt = w3.eth.waitForTransactionReceipt(tx_hash)
                st.write(receipt)
            except Exception as ex4:
                print(f'Error calling Token Contract Function transfer {ex4}')
        else:
            print(f'Not enough Tokens in Wallet')
    else:
        print(f'Sender and Recipient address cannot be same')

################################################################################
# Beneficiary Details
################################################################################
st.markdown("<p class='orange-font'>Beneficiary Details</P>", unsafe_allow_html=True)
dfBeneficiary = pd.DataFrame(accounts, columns=['BeneficiaryAccount'])
benef_balances = []
for benefAccount in dfBeneficiary['BeneficiaryAccount']:
    try:
        benefAmount = Decimal(token_contract.functions.balanceOf(account=benefAccount).call())
        benef_balances.append(benefAmount) 
    except Exception as ex5:        
        print('Error during conversion')
dfBeneficiary['TokenBalance'] = benef_balances

st.table(dfBeneficiary)

