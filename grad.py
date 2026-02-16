import gradio as gr

# Step 1: Create a class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Step 2: Function to use the class
def create_book(title, author):
    book1 = Book(title, author)
    return f"Title: {book1.title}\nAuthor: {book1.author}"

# Step 3: Gradio Interface
app = gr.Interface(
    fn=create_book,
    inputs=[
        gr.Textbox(label="Enter Book Title"),
        gr.Textbox(label="Enter Author Name")
    ],
    outputs=gr.Textbox(label="Book Details"),
    title="Book Information App by Shashank",
    description="Enter book title and author to see details using class & object"
)

# Step 4: Launch app
app.launch()