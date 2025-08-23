from textnode import TextNode, TextType

def main():
    text_node = TextNode("some text", TextType.PLAIN, "https://www.boot.dev")
    print(text_node)

main()