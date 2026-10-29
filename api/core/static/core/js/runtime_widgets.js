function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
    // --- Token widget ---
    const tokenInput = document.getElementById("id_token");
    const generateButton = document.getElementById("generate-token-btn");
    const copyButton = document.getElementById("copy-token-btn");
    const hashButton = document.getElementById("hash-token-btn");

    if (generateButton) {
        generateButton.addEventListener("click", function () {
            const randomBytes = new Uint8Array(32);
            crypto.getRandomValues(randomBytes);
            tokenInput.value = btoa(String.fromCharCode(...randomBytes))
                .replace(/\+/g, "-")
                .replace(/\//g, "_")
                .replace(/=/g, "");
        });
    }

    if (copyButton) {
        copyButton.addEventListener("click", async function () {
            if (!tokenInput.value) {
                alert("There is no token to copy");
                return;
            }
            await navigator.clipboard.writeText(tokenInput.value);
            alert("Token successfully copied");
        });
    }

    if (hashButton) {
        hashButton.addEventListener("click", async function () {
            if (!tokenInput.value) {
                alert("There is no token to hash.");
                return;
            }
            const url = hashButton.dataset.url;
            const response = await postForm(url, { token: tokenInput.value });
            handleResponse(response);
        });
    }


    // --- Status widget ---
    const statusCheck = document.getElementById("id_status");
    const clearButton = document.getElementById("clear-cache-btn");

    if (clearButton) {
        clearButton.addEventListener("click", async function () {
            const url = clearButton.dataset.url;
            const response = await postForm(url, {
                status: statusCheck.checked ? "true" : "false",
            });
            handleResponse(response);
        });
    }


    // --- Password widget ---
    const passwordInput = document.getElementById("id_password");
    const generateButtonPass = document.getElementById("generate-password-btn");
    const copyButtonPass = document.getElementById("copy-password-btn");
    const clearCacheButtonPass = document.getElementById("clear-cache-password-btn");

    if (generateButtonPass) {
        generateButtonPass.addEventListener("click", function () {
            passwordInput.value = crypto.randomUUID();
        });
    }

    if (copyButtonPass) {
        copyButtonPass.addEventListener("click", async function () {
            if (!passwordInput.value) {
                alert("There is no password to copy");
                return;
            }
            await navigator.clipboard.writeText(passwordInput.value);
            alert("password successfully copied");
        });
    }

    if (clearCacheButtonPass) {
        clearCacheButtonPass.addEventListener("click", async function () {
            if (!passwordInput.value) {
                alert("There is no password to hash.");
                return;
            }
            const url = clearCacheButtonPass.dataset.url;
            const response = await postForm(url, { password: passwordInput.value });
            handleResponse(response);
        });
    }


    // --- function help ---
    async function postForm(url, body) {
        const csrfToken = getCookie("csrftoken");
        return fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams(body),
        });
    }

    async function handleResponse(response) {
        const data = await response.json();
        if (response.ok) {
            alert(data.detail);
            window.location.reload();
        } else {
            alert(data.error || "Something went wrong.");
        }
    }
});