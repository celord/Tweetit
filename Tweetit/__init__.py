#!/usr/bin/env python
import rb
class Tweetit(rb.Plugin):
"""
Tweetit class derived from rb.Plugin at te moment it only activates and 
deactivates the plugin that does not do nothing 
"""
    def activate(self, shell):
        print "Activate!"
    def deactivate(self, shell):
        print "Deactivate!"
