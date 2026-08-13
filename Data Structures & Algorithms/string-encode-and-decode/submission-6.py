class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(str(len(s)) + "#" + s)

        result = "".join(arr)
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        print(s)

        length = len(s)
        i = 0

        while (i < length):
            k = i
            while s[k] != "#" and k < length:
                k += 1

            print(i, k)
            if (s[i:k].isnumeric()):
                num_encode = int(s[i:k])
                #print(num_encode)
            else:
                break
            
            # print(num_encode)

            read = s[(k+1): (k+1+num_encode)]
            result.append(read)

            i = k+1+num_encode
            #print(i, "and this is ", s[i])              
            
        return result