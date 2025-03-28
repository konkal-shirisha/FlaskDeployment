from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load saved models
product_similarity = joblib.load('product_similarity.pkl')
user_encoder = joblib.load('user_encoder.pkl')
product_encoder = joblib.load('product_encoder.pkl')

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend_products():
    """
    Recommend similar products based on the input product ID.
    """
    product_id = request.args.get('product_id')

    # Validate the product ID
    if product_id not in product_encoder.classes_:
        return jsonify({"error": "Product ID not found"}), 404

    # Get product index and find similar products
    product_idx = product_encoder.transform([product_id])[0]
    similar_indices = np.argsort(-product_similarity[product_idx])[1:4]  # Top 3 recommendations

    # Decode indices back to product IDs
    similar_products = product_encoder.inverse_transform(similar_indices)

    return jsonify({"similar_products": similar_products.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
