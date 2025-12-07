async function processVideo() {
    const url = document.getElementById("videoUrl").value;
    document.getElementById("status").innerText = "Processing...";

    const formData = new FormData();
    formData.append("url", url);

    const res = await fetch("/process_video", {
        method: "POST",
        body: formData,
    });

    const data = await res.json();
    document.getElementById("summary").innerText = data.summary;
    document.getElementById("status").innerText = "Done!";
}
