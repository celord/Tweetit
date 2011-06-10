#!/usr/bin/env python
import rb
class Tweetit(rb.Plugin):
    def activate(self, shell):
        print "Activate!"
    def deactivate(self, shell):
        print "Deactivate!"
