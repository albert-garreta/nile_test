import asyncio
import os
import pytest
from starkware.starknet.testing.starknet import Starknet
# Some test fixtures are defined here

CONTRACT = os.path.join("contracts", "contract.cairo")

@pytest.fixture(scope="module")
def event_loop():
    return asyncio.new_event_loop()

@pytest.fixture(scope="module")
async def starknet_factory():
    starknet = await Starknet.empty()
    return starknet

@pytest.fixture(scope="module")
async def test_contract(starknet_factory):
    starknet = starknet_factory
    # Deploy the account contract
    contract = await starknet.deploy(source=CONTRACT)
    return contract
