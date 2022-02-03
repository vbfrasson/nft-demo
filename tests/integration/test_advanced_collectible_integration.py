from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import *
from scripts.advanced_collectible.deploy_and_create import *
import pytest
import time


def test_can_create_advanced_collectible_integration():
    skip_integration_test()
    # Act
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(300)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    print(advanced_collectible.tokenCounter())
