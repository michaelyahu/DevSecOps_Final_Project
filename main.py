from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Load data from the JSON file
with open("data.json") as f:
    data = json.load(f)

@app.get("/")
def read_root():
    return {"Welcome to Moshe's Book API"}

@app.get("/authors/{author_id}")
def find_author(author_id: int):
    if author_id < 0 or author_id >= len(data["authors"]):
        raise HTTPException(status_code=404, detail="Author not found")
    
    author = data["authors"][author_id]
    return author

@app.get("/books/{search_term}")
def find_book_by_name(search_term: str):
    results = []
    for author in data["authors"]:
        # Search for the book by checking if the search term is in the author's name or description
        if search_term.lower() in author["name"].lower() or search_term.lower() in author["description"].lower():
            results.append(author)

    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail="Author not found for the given name or description")

@app.get("/authors-by-letter/{letter}")
def find_authors_by_letter(letter: str):
    results = [author for author in data["authors"] if author["name"].lower().startswith(letter.lower())]
    
    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail="Authors not found for the given letter")

@app.get("/books-by-letter/{letter}")
def find_books_by_letter(letter: str):
    results = [book for author in data["authors"] for book in author["books"] if book.lower().startswith(letter.lower())]
    
    if results:
        return {"books": results}
    else:
        raise HTTPException(status_code=404, detail="Books not found for the given letter")

@app.get("/search-by-word/{word}")
def search_by_word(word: str):
    results = {
        "authors": [author for author in data["authors"] if word.lower() in author["name"].lower() or word.lower() in author["description"].lower()],
        "books": [book for author in data["authors"] for book in author["books"] if word.lower() in book.lower()]
    }

    if results["authors"] or results["books"]:
        return results
    else:
        raise HTTPException(status_code=404, detail="No matching authors or books found for the given word")

@app.get("/search-by-description/{description}")
def find_book_by_description(description: str):
    results = [author for author in data["authors"] if description.lower() in author["description"].lower()]
    
    if results:
        return results
    else:
        raise HTTPException(status_code=404, detail="Authors not found for the given description")


#test#
