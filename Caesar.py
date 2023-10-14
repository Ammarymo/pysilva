def shift_amount(i):
    return i%26

def encrypt(text,required_shift):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    out_string = ""
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string += char
        else:
            alpha_index = alphabet.find(char)
            out_string += alphabet[shift_amount(alpha_index+required_shift)]
    return out_string

complex_text = """
In the vast realm of artificial intelligence, the intersection of machine learning and natural language processing is where the future seems brightest. From self-driving cars that understand and respond to spoken commands to virtual assistants capable of holding conversations, AI and NLP have permeated our daily lives in ways we couldn't have imagined just a few years ago.

The algorithms powering these advancements are becoming increasingly sophisticated. Deep learning models, neural networks with many layers, have revolutionized how we tackle complex tasks. They can recognize objects in images, translate languages in real-time, and even generate human-like text.

However, the rapid advancement of AI and NLP comes with ethical and societal challenges. Questions about privacy, bias in algorithms, and the potential misuse of AI are at the forefront of discussions. Striking a balance between innovation and responsibility is essential as we navigate this new era of technology.

As researchers, engineers, and policymakers continue to push the boundaries of what AI and NLP can achieve, it's crucial to keep a critical eye on the impact of these technologies on our lives, society, and the world at large.
"""

y =(encrypt(complex_text,30))