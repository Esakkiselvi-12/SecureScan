function startScan() {
    const target = document.getElementById("target").value;
    const output = document.getElementById("output");

    if (!target) {
        output.innerHTML = "<p>Please enter a target</p>";
        return;
    }

    output.innerHTML = "<p>Scanning...</p>";

    fetch("/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ target: target })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            output.innerHTML = `<p>Error: ${data.error}</p>`;
            return;
        }

        output.innerHTML = `
            <div class="result-box">
                <h3>Scan Result</h3>
                <p><b>Target:</b> ${data.target}</p>
                <p><b>Server:</b> ${data.server}</p>
                <p><b>Status:</b> ${data.status}</p>
                <p><b>Open Ports:</b></p>
                <ul>
                    ${data.ports.map(p => `<li>Port ${p} OPEN</li>`).join("")}
                </ul>
            </div>
        `;
    })
    .catch(() => {
        output.innerHTML = "<p>Error occurred</p>";
    });
}
