class Solution:
    def decodeString(self, s: str) -> str:
        # I think the main idea for me to yet to understand is that in the stack if you got n[char char char] and then n2 [char char char] you save it in the stack as (empty, n1) and then (char1, n2) and then (char2, n3) etc.. so that when you pop you pop with current assembled string with the prev number you had before
        # example: 3[a2[c]] --> stack will be [('', 3), ('a', 2)]
        # so with first pop current is 'a' and prev  is '' so you do prev + current * n
        stack = []

        current_num = 0
        current_string = ""

        for char in s:
            # digit
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            # opening bracket
            elif char == '[':
                stack.append((current_string, current_num))

                current_string = ""
                current_num = 0

            # closing bracket
            elif char == ']':
                prev_string, repeat = stack.pop()

                current_string = (
                    prev_string +
                    current_string * repeat
                )

            # letters
            else:
                current_string += char

        return current_string
                

