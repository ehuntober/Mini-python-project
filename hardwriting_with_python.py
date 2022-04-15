
import pywhatkit as pw

txt = """
Buyer personas are one of the most fundamental aspects of great marketing. A buyer persona represents a distinct group of potential customers, or an archetypal person whom you want your marketing to
reach. Targeting your work to buyer personas prevents you from sitting
on your butt in your comfortable office just making stuff up about your
products, which is the cause of most ineffective marketing. 
"""

pw.text_to_handwriting(txt, "demo1.png", [0,0,138])
print("END")
