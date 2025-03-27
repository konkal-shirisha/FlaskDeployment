const form = document.getElementById('recommendationForm');
const recommendationsDiv = document.getElementById('recommendations');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const inputType = document.getElementById('inputType').value;
    const inputId = document.getElementById('inputId').value;

    // Your Render-hosted backend URL
    const renderUrl = "https://your-backend-service.onrender.com"; // Replace with your Render URL

    try {
        // Send request to backend
        const response = await fetch(`${renderUrl}/recommend?type=${inputType}&id=${inputId}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        displayRecommendations(data.recommendations);
    } catch (error) {
        recommendationsDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    }
});

function displayRecommendations(recommendations) {
    recommendationsDiv.innerHTML = `
        <h3>Recommendations:</h3>
        <ul>
            ${recommendations.map(rec => `<li>${rec}</li>`).join('')}
        </ul>
    `;
}
