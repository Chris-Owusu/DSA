### Choose Your Own Adventure: Wilderness Escape
print("Once upon a time…")

class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        valid_input = ['1', '2']  # Changed valid_input to strings

        while story_node.choices:  # Use while loop with a condition
            choice = input("Enter 1 or 2 to continue the story: ")
            if choice not in valid_input:
                print("Error: Enter valid input, either 1 or 2")
            else:
                chosen_index = int(choice) - 1  # Fixed the chosen_index calculation
                if chosen_index < len(story_node.choices):  # Check if it's a valid choice
                    chosen_child = story_node.choices[chosen_index]  # Get the chosen child
                    print(chosen_child.story_piece)
                    story_node = chosen_child
                else:
                    print("Invalid choice. Enter 1 or 2")

# Define the story nodes
story_root = TreeNode(
    """
    You are in a forest clearing. There is a path to the left.
    A bear emerges from the trees and roars!
    Do you: 
    1 ) Roar back!
    2 ) Run to the left...
    """
)

choice_a = TreeNode(
    """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
    """
)

choice_b = TreeNode(
    """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
    """
)

choice_a_1 = TreeNode(
    """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
    """
)

choice_a_2 = TreeNode(
    """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
    """
)

choice_b_1 = TreeNode(
    """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
    """
)

choice_b_2 = TreeNode(
    """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
    """
)

# Build the story tree
story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

# Start the story
story_root.traverse()
