from operations import Operations

class Functions(Operations):
      def lower_sigma0(self, data):
            temp1 = self.rotateRight(data, 7)
            temp2 = self.rotateRight(data, 18)
            temp3 = self.shiftRight(data, 3)
            result = self.xor(temp3, self.xor(temp1, temp2))
            return result

      def lower_sigma1(self, data):
            temp1 = self.rotateRight(data, 17)
            temp2 = self.rotateRight(data, 19)
            temp3 = self.shiftRight(data, 10)
            result = self.xor(temp3, self.xor(temp1, temp2))
            return result

      def upper_sigma0(self, data):
            temp1 = self.rotateRight(data, 2)
            temp2 = self.rotateRight(data, 13)
            temp3 = self.rotateRight(data, 22)
            result = self.xor(temp3, self.xor(temp1, temp2))
            return result

      def upper_sigma1(self, data):
            temp1 = self.rotateRight(data, 6)
            temp2 = self.rotateRight(data, 11)
            temp3 = self.rotateRight(data, 25)
            result = self.xor(temp3, self.xor(temp1, temp2))
            return result

      def choice(self, x, y, z):
            result = ""
            for i in range(len(x)):
                  result += y[i] if x[i] == "1" else z[i]

            return result

      def majority(self, x, y, z):
            result = ""
            for i in range(len(x)):
                  temp0 = 0
                  temp1 = 0

                  temp0 += 1 if x[i] == "0" else 0 
                  temp1 += 1 if x[i] == "1" else 0

                  temp0 += 1 if y[i] == "0" else 0                  
                  temp1 += 1 if y[i] == "1" else 0

                  temp0 += 1 if z[i] == "0" else 0
                  temp1 += 1 if z[i] == "1" else 0
                  
                  if temp0 > temp1:
                        result += "0"
                  else:
                        result += "1"

            return result