
import flask
from flask import Flask, render_template, request

import pickle
import numpy as np


app = Flask(__name__)


# Load the trained KNN model

with open("KNN_Multi_level_Classification_Model.pkl", "rb") as p:

    model = pickle.load(p)


# Iris flower class names

iris_classes = {

    0: "Iris Setosa",

    1: "Iris Virginica",

    2: "Iris Versicolor"

}


@app.route("/", methods=["GET", "POST"])

def home():

    prediction = None

    error = None


    if request.method == "POST":

        try:

            # Get input values from HTML

            sepal_length = float(request.form["sepal_length"])

            sepal_width = float(request.form["sepal_width"])

            petal_length = float(request.form["petal_length"])

            petal_width = float(request.form["petal_width"])


            # Convert input values into 2D array

            input_data = np.array([[

                sepal_length,

                sepal_width,

                petal_length,

                petal_width

            ]])


            # Perform prediction

            result = model.predict(input_data)


            # Get predicted class

            predicted_class = int(result[0])


            # Get Iris flower name

            prediction = f"({predicted_class}) {iris_classes[predicted_class]}"


        except (ValueError, KeyError, IndexError):

            error = "Please enter valid numerical values."


        except Exception:

            error = "Something went wrong during prediction."


    return render_template(

        "index.html",

        prediction=prediction,

        error=error

    )


if __name__ == "__main__":

    app.run(debug=True)

