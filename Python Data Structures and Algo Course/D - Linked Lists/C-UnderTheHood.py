"""value and a pointer make up a node"""
"""what is this node? """

# so in a linkedin list it's basically a nested dictionary

head = {"value": 11,
        "next": {
            "value": 3,
            "next": {
                "value": 21,
                "next": {
                    "value": 12,
                    "next":  {
                        "value": 100,
                        "next": None
                    }
                }
            }

        }
        }

# it's just like a blockchain like prev hashes and hashes
# but in this, you contain the next variable as the next dictionary/node
# and the tail variable will be pointed towards the last node

# we call call values like print(my_LINKED_LIST.head.next.next.value) </p> only works with a lined list
