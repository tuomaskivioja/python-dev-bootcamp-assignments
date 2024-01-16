
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the playlist is empty

    def add_song_to_start(self, song):
        """
        Adds a new song to the start of the playlist.
        """
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node

    def display_playlist(self):
        """
        Prints out the songs in the playlist.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next
