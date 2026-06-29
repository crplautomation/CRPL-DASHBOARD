async function openPendingPOD() {

    showLoading();

    try {

        const response = await fetch("/api/pending-pod");

        const data = await response.json();

        let html = "";

        data.summary.forEach(item => {

            html += `
                <tr>

                    <td>${item.party}</td>

                    <td>${item.count}</td>

                </tr>
            `;

        });

        document.getElementById("podTable").innerHTML = html;

        hideLoading();

        new bootstrap.Modal(
            document.getElementById("podModal")
        ).show();

    }

    catch (err) {

        hideLoading();

        console.error(err);

        alert("Unable to load Pending POD.");

    }

}


function exportPendingPOD() {

    window.location.href = "/api/pending-pod/export";

}