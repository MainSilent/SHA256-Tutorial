class Operations:
      def add(self, data1, data2):
            x = data1
            y = data2

            carry = 0
            result = ""

            for i in range(len(data1) -1, -1, -1):
                  r = carry
                  r += 1 if x[i] == '1' else 0
                  r += 1 if y[i] == '1' else 0
                  result = ('1' if r % 2 == 1 else '0') + result
                  carry = 0 if r < 2 else 1

            if carry != 0: result = '1' + result

            return result[-len(data1):]

      def xor(self, data1, data2):
            result = ""
            for i in range(len(data1)):
                  temp1 = data1[i]
                  temp2 = data2[i]
                  if (temp1 == "0" and temp2 == "0") or (temp1 == "1" and temp2 == "1"):
                        result += "0"
                  else:
                        result += "1"

            return result

      def shiftRight(self, data, turn):
            result = "0" * turn + data
            return result[:len(data)]

      def rotateRight(self, data, turn):
            result = None
            for i in range(turn):
                  if result:
                        temp = result[-1]
                        result = (temp + result)[:len(data)]
                  else:
                        temp = data[-1]
                        result = (temp + data)[:len(data)]

            return result