from copy import copy
from functions import Functions

k = [
      0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
      0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
      0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
      0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
      0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
      0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
      0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
      0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
      0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
      0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
      0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
      0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
      0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
      0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
      0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
      0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

h = [
      0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

class SHA256(Functions):
      blocks = []   

      def message_to_blocks(self, message):
            # convert input to binary
            data = [format(ord(x), 'b').zfill(8) for x in message]
            data = ''.join(data)

            # get the length
            size_length = 64
            length =  f'{len(data):b}'

            # start padding
            data += '1'
            while (len(data) + size_length) % 512 != 0:
                  data += "0"

            # add message length
            data += length.zfill(64)

            # add to blocks
            n = 512
            self.blocks = [(data[i:i+n]) for i in range(0, len(data), n)]

      def message_schedule(self, data):
            schedule = []
            n = 32
            # first 16 words
            schedule = [(data[i:i+n]) for i in range(0, len(data), n)]
            # generate the rest
            for i in range(16, 64):
                  temp1 = self.lower_sigma1(schedule[-2])
                  temp2 = self.lower_sigma0(schedule[-15])
                  result = self.add(temp1, self.add(schedule[-7], self.add(temp2, schedule[-16])))
                  schedule.append(result)

            return schedule

      def compress(self):
            _k = [f'{i:b}'.zfill(32) for i in k]
            _h = [f'{i:b}'.zfill(32) for i in h]  

            for block in self.blocks:
                  temp_h = copy(_h)
                  _w = self.message_schedule(block)
                  for i in range(64):
                        T1 = [self.upper_sigma1(_h[4]), self.choice(_h[4], _h[5], _h[6]), _h[7], _k[i], _w[i]]
                        T1 = self.add(T1[0], self.add(T1[1], self.add(T1[2], self.add(T1[3], T1[4]))))

                        T2 = [self.upper_sigma0(_h[0]), self.majority(_h[0], _h[1], _h[2])]
                        T2 = self.add(T2[0], T2[1])
                        
                        # shift all constants down
                        _h[7] = _h[6] # h
                        _h[6] = _h[5] # g
                        _h[5] = _h[4] # f
                        _h[4] = _h[3] # e
                        _h[3] = _h[2] # d
                        _h[2] = _h[1] # c
                        _h[1] = _h[0] # b

                        # compress
                        _h[0] = self.add(T1, T2)
                        _h[4] = self.add(_h[4], T1)

                  # add with initial values
                  _h[0] = self.add(_h[0], temp_h[0])
                  _h[1] = self.add(_h[1], temp_h[1])
                  _h[2] = self.add(_h[2], temp_h[2])
                  _h[3] = self.add(_h[3], temp_h[3])
                  _h[4] = self.add(_h[4], temp_h[4])
                  _h[5] = self.add(_h[5], temp_h[5])
                  _h[6] = self.add(_h[6], temp_h[6])
                  _h[7] = self.add(_h[7], temp_h[7])

            return self.digest(_h)

      def digest(self, hashes):
            final_hash = ""
            for hash in hashes:
                  t = hex(int(hash, 2))
                  final_hash += t[2:].zfill(8)

            return final_hash
