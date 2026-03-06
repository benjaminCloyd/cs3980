(async () => {
    const tbody = document.querySelector('#year-list tbody');
    const url = "https://api.datausa.io/tesseract/data.jsonrecords?cube=acs_yg_total_population_5&measures=Population&drilldowns=Year";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const years = await response.json();
        console.log(years);
        years.data.forEach(item => {
            const tr = document.createElement('tr');
            // format population with commas
            const pop = Number(item.Population).toLocaleString();
            tr.innerHTML = `<td>${item.Year}</td><td>${pop}</td>`;
            tbody.appendChild(tr);
        });
    } catch (error) {
        console.error(error.message);
    }
})();

