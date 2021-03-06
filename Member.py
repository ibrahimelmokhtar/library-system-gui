class Member():
    def __init__(self, id="", name="", address=""):
        """Create a new member.

        Args:
            id (string): ID of the member.
            name (string): Name of the member.
            address (string): Address of the member.
        """
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        """ Print the Member object to the terminal.
        """

        output = """\tMember's Info.
        \tID\t: {}
        \tName\t: {}
        \tAddress\t: {}
        """
        return output.format(self.id, self.name, self.address)

    def __eq__(self, other):
        """Used to compare two objects.

        Args:
            other (object): object of Book type.

        Returns:
            bool: the result of the comparison.
        """
        return self.__dict__ == other.__dict__

# Setter and Getter functions:
    def setID(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address

    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
