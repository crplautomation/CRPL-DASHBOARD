async function openPendingPhotos() {

    showLoading();

    try {

        const response = await fetch("/api/pending-photos");

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

        document.getElementById("photoTable").innerHTML = html;

        hideLoading();

        new bootstrap.Modal(
            document.getElementById("photoModal")
        ).show();

    }

    catch (err) {

        hideLoading();

        console.error(err);

        alert("Unable to load Pending Photos.");

    }

}


function exportPendingPhotos() {

    window.location.href = "/api/pending-photos/export";

}