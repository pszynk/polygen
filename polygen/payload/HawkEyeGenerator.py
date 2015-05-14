
from copy import deepcopy
from random import random, randint, shuffle
from polygen.signature import SnortRule, Token
from polygen.payload.methods import generate_ordered

class HawkEyeGenerator(object):
    """Generator for HawkEye Trojan"""

    _signature = SnortRule(
        name = 'Win.Trojan.HawkEye',
        desc = 'MALWARE-CNC keylogger exfiltration attempt',
        tokens = [
            Token('Subject\x3A\x20HawkEye Keylogger\x20\x7C\x20'),
            Token(r'=0D=0APC'),
            Token(r'=0D=0AInstalled'),
            Token(r'=0D=0AOperating System', within=75, distance=15),
            Token(r'=0D=0AInternal IP', within=200, distance=10),
            Token(r'=0D=0AExternal IP', within=50, distance=5),
        ]
    )

    _short = 'hawkeye'

    @property
    def short(self): return self._short

    @property
    def signature(self): return self._signature

    def generate(self, rand_byte_func, min_size, max_size,
                 rand_size_func=randint):

        preProb = 0.3
        postProb = 0.2

        unordered = deepcopy(self.signature.tokens[:2])
        shuffle(unordered)

        ordered = deepcopy(self.signature.tokens[2:])

        for t in unordered:
            p = random();
            if p <= preProb:
                ordered[0].distance = 0
                ordered.insert(0, t)
                continue
            if p <= (preProb + postProb):
                t.distance = 0
                ordered.append(t)
                continue

            #print('t ' , t)
            #print('len t' , len(t))
            while True:
                # wylosowac przerwe
                pos = randint(1, len(ordered)-1)
                nxt = ordered[pos]
                #print('pos ' , pos)
                #print('nxt ' , nxt)
                if(nxt.within):
                    space = nxt.within - len(nxt) + nxt.distance
                    #print('space ' , space)
                    if (space < len(t)):
                        continue

                    start = randint(0, space - len(t))
                    #print('start' , start)
                    t.distance = start
                    t.within = start + len(t)

                    nxt.within = nxt.distance + nxt.within - t.within
                    nxt.distance = max(0, nxt.distance - t.within)
                    #print('nxt.distance', nxt.distance)
                    ordered.insert(pos, t)
                    break

                t.distance = 0
                ordered.insert(pos, t)


        #for o in ordered:
            #print (o, o.distance, o.within)
        return generate_ordered(ordered, rand_byte_func, min_size, max_size, rand_size_func)



                # sprawdzic czy da rade wsadzic
                #zmodyfikowac znaczniki
                # wszdzic i przewac






        #return generate_ordered(
        #    list(self.signature.tokens), rand_byte_func, min_size, max_size,
        #    rand_size_func);
