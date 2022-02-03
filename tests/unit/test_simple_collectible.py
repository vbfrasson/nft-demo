from scripts.helpful_scripts import *
from scripts.simple_collectible.deploy_and_create import *
from brownie import config, network, accounts
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
