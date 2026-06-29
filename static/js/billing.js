async function openPendingBilling() {

    showLoading();

    try {

        const response = await fetch("/api/pending-billing");

        const data = await response.json();

        let html = "";

        data.summary.forEach(item => {

            html += `
                <tr>

                    <td>${item.party}</td>

                    <td>₹${item.amount_lakh} L</td>

                    <td>${item.trips}</td>

                    <td>${item.oldest_days} Days</td>

                </tr>
            `;

        });

        document.getElementById("billingTable").innerHTML = html;

        hideLoading();

        new bootstrap.Modal(
            document.getElementById("billingModal")
        ).show();

    }

    catch (err) {

        hideLoading();

        console.error(err);

        alert("Unable to load Pending Billing.");

    }

}


function exportPendingBilling() {

    window.location.href = "/api/pending-billing/export";

}