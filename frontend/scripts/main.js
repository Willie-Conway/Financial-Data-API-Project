// frontend/scripts/main.js
const API_BASE_URL = 'https://your-backend-api-url.com'; // Replace with your actual backend URL

document.getElementById('searchBtn').addEventListener('click', fetchRealTimeData);
document.getElementById('historicalBtn').addEventListener('click', fetchHistoricalData);

async function fetchRealTimeData() {
    const symbol = document.getElementById('stockSymbol').value.trim();
    if (!symbol) {
        alert('Please enter a stock symbol');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/api/stocks/${symbol}`);
        if (!response.ok) {
            throw new Error('Stock not found or API error');
        }
        
        const data = await response.json();
        displayRealTimeData(data);
    } catch (error) {
        console.error('Error fetching real-time data:', error);
        alert('Error fetching data. Please try again.');
    }
}

function displayRealTimeData(data) {
    const quoteDisplay = document.getElementById('quoteDisplay');
    quoteDisplay.innerHTML = '';
    
    if (!data || Object.keys(data).length === 0) {
        quoteDisplay.innerHTML = '<p>No data available for this symbol</p>';
        return;
    }
    
    // Create display elements for each data point
    for (const [key, value] of Object.entries(data)) {
        const div = document.createElement('div');
        div.className = 'quote-item';
        
        const label = document.createElement('span');
        label.className = 'quote-label';
        label.textContent = `${key.replace(/_/g, ' ')}:`;
        
        const val = document.createElement('span');
        val.textContent = value;
        
        div.appendChild(label);
        div.appendChild(val);
        quoteDisplay.appendChild(div);
    }
    
    document.getElementById('realTimeData').classList.remove('hidden');
}

async function fetchHistoricalData() {
    const symbol = document.getElementById('stockSymbol').value.trim();
    if (!symbol) {
        alert('Please enter a stock symbol');
        return;
    }
    
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    
    let url = `${API_BASE_URL}/api/historical/${symbol}`;
    if (startDate || endDate) {
        url += `?start_date=${startDate}&end_date=${endDate}`;
    }
    
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Historical data not found or API error');
        }
        
        const data = await response.json();
        renderHistoricalChart(data);
    } catch (error) {
        console.error('Error fetching historical data:', error);
        alert('Error fetching historical data. Please try again.');
    }
}

function renderHistoricalChart(data) {
    const ctx = document.createElement('canvas');
    const container = document.getElementById('chartContainer');
    
    // Clear previous chart
    container.innerHTML = '';
    container.appendChild(ctx);
    
    if (!data || Object.keys(data).length === 0) {
        container.innerHTML = '<p>No historical data available for this symbol</p>';
        return;
    }
    
    // Prepare data for Chart.js
    const dates = Object.keys(data).sort();
    const closePrices = dates.map(date => parseFloat(data[date]['4. close']));
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Closing Price',
                data: closePrices,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price (USD)'
                    }
                }
            }
        }
    });
}