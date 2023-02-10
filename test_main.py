# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:59:46 2023

@author: m4fri
"""

from main import fair_sharer

def test_fair_sharer():
    # general function test:
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0], "fair_sharer failed"
    
    # tests if multiple iterations are working:
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90], "multiple iterations failed"
    
    # tests highest value in first index
    assert fair_sharer([2000, 0, 600, 0], 1) == [1600.0, 200.0, 600, 200.0], "fair_sharer failed, because highest value was in first index"
    
    # tests highest value in last index
    assert fair_sharer([1500, 500, 900, 0], 1) == [1200.0, 650.0, 900, 150.0], "fair_sharer failed, because highest value was in last index"

    # tests changing share    
    assert fair_sharer([500, 400, 900, 0], 1, 0.2) == [500, 580.0, 540.0, 180.0], "changing share failed"
    
    # tests multiple high values
    assert fair_sharer([2000, 2000, 600, 0], 1) == [1600.0, 2200.0, 600, 200.0], "fair_sharer failed, because of multiple max values"

