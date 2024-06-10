document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('clubGraph').getContext('2d');
    var clubChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Club 1', 'Club 2'], // Add more club names as needed
            datasets: [{
                label: 'Club Popularity',
                data: [12, 19], // Add more data as needed
                backgroundColor: [
                    'rgba(255, 215, 0, 0.2)', // Gold color
                    'rgba(0, 128, 0, 0.2)', // Green color
                    // Add more colors as needed
                ],
                borderColor: [
                    'rgba(255, 215, 0, 1)',
                    'rgba(0, 128, 0, 1)',
                    // Add more border colors as needed
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
