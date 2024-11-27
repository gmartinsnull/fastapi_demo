"""
Create a FastAPI app
Root endpoint returns the app description
"""

from fastapi import FastAPI

app = FastAPI()


def get_app_description():
    """
    Define a function to return a description of the app
    """
    return (
        "Welcome to the Iris Species Prediction API!"
        "This API allows you to predict the species of an iris flower based on its sepal and petal measurements."
        "Use the '/predict/' endpoint with a POST request to make predictions."
        "Example usage: POST to '/predict/' with JSON data containing sepal_length, sepal_width, petal_length, and petal_width."
    )


@app.get("/predict/")
async def predict():
    """
    Prediction mock endpoint
    """
    return {"message": "This is the predict endpoint."}


@app.get("/")
async def root():
    """
    Define the root endpoint to return the app description
    """
    return {"message": get_app_description()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
