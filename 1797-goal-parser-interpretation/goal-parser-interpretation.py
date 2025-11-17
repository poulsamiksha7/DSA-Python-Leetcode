class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        if not command:
            return ""
        if command.startswith("G"):
            return "G" + self.interpret(command[1:])
        if command.startswith("()"):
            return "o" + self.interpret(command[2:])
        if command.startswith("(al)"):
            return "al" + self.interpret(command[4:])
    

        