# static.py

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mamma Mia</title>
    <link rel="icon" href="https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png" type="image/x-icon">

    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-size: 2.1vh;
            font-family: 'Inter', 'Open Sans', Arial, sans-serif;
            color: #ffffff;
            background:
                linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
                url('https://i.postimg.cc/ry3p76HY/italian-seamless-free-vector-pattern3.png')
                center center repeat;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            overflow-y: auto;
        }

        #addon {
            margin-top: 9vh;
            width: 65vh;
            max-width: 95%;
            padding: 2vh;
            border-radius: 14px;
            background: rgba(20, 20, 20, 0.85);
            backdrop-filter: blur(6px);
            box-shadow: 0 1vh 3vh rgba(0,0,0,0.4);
            text-align: center;
        }

        .logo {
            width: 11vh;
            margin: -6vh auto 2vh;
        }

        .logo img {
            width: 100%;
            filter: drop-shadow(0 0 1vh rgba(255,255,255,0.15));
        }

        h1 {
            font-size: 4.2vh;
            margin: 0;
            font-weight: 700;
            letter-spacing: 0.05vh;
        }

        h2 {
            font-size: 2vh;
            font-style: italic;
            opacity: 0.75;
            margin: 0.5vh 0 2vh;
        }

        h3 {
            font-size: 2.3vh;
            margin: 2vh 0 1vh;
        }

        .description {
            font-size: 1.9vh;
            opacity: 0.85;
            margin-bottom: 2vh;
        }

        #additionalText h2 {
            font-size: 1.8vh;
            line-height: 1.5;
        }

        .provider-group {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1vh;
            margin-bottom: 1.4vh;
            padding: 1.4vh;
            border-radius: 8px;
            background: rgba(255,255,255,0.08);
            transition: background 0.15s ease;
        }

        .provider-group:hover {
            background: rgba(255,255,255,0.14);
        }

        .provider-group label {
            display: flex;
            align-items: center;
            gap: 1.4vh;
            flex-grow: 1;
            font-size: 2.1vh;
            white-space: nowrap;
        }

        input[type="checkbox"] {
            width: 3.8vh;
            height: 3.8vh;
            cursor: pointer;
        }

        input[id$="_mfp"] {
            margin-left: 2vh;
        }

        button {
            border: none;
            border-radius: 999px;
            padding: 1.3vh 3.5vh;
            font-size: 2.1vh;
            font-weight: 600;
            color: #fff;
            cursor: pointer;
            background: linear-gradient(135deg, #8A5AAB, #6f3fa1);
            box-shadow: 0 0.6vh 1.4vh rgba(0,0,0,0.35);
            transition: transform 0.12s ease, box-shadow 0.12s ease;
            width: 80%;
            max-width: 36vh;
            margin: 1.2vh auto;
            display: block;
        }

        button:hover {
            transform: translateY(-0.2vh);
            box-shadow: 0 1vh 2vh rgba(0,0,0,0.45);
        }

        button:active {
            transform: translateY(0);
            box-shadow: inset 0 0 0.6vh rgba(255,255,255,0.5);
        }

        #generateManifestButton {
            background: linear-gradient(135deg, #4CAF50, #3fa046);
        }

        #installButton {
            background: linear-gradient(135deg, #FF5722, #e64a19);
        }

        #manifestBox {
            margin-top: 2vh;
            padding: 2vh;
            background: rgba(0,0,0,0.55);
            border-radius: 8px;
            display: none;
            text-align: left;
            font-family: monospace;
            font-size: 1.8vh;
            word-break: break-all;
            border: 1px solid rgba(255,255,255,0.15);
        }

        #mediaFlowProxyInputContainer input,
        #mediaFlowProxyPasswordContainer input {
            width: 100%;
            padding: 1.2vh;
            margin-top: 1vh;
            border-radius: 6px;
            border: none;
            font-size: 1.9vh;
        }
    </style>
</head>

<body>
<div id="addon">

    <div class="logo">
        <img src="https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png">
    </div>

    <h1>Mamma Mia</h1>
    <h2>v2.0.2</h2>

    <div id="additionalText">
        <h2>
            This addon provides Movie, Series, Anime, and Live TV HTTPS Streams.<br>
            https://github.com/UrloMythus/MammaMia/
        </h2>
    </div>

    <p class="description">
        🕵️‍♂️ = Mediaflowproxy might be needed<br>
        Select the box with this icon if you want to enable MFP for that source
    </p>

    <h3>Select Providers:</h3>

    <form id="provider-form">

        <div class="provider-group"><label><input type="checkbox" id="streamingwatch"> StreamingWatch</label></div>
        <div class="provider-group"><label><input type="checkbox" id="guardoserie"> Guardoserie</label></div>
        <div class="provider-group"><label><input type="checkbox" id="guardaflix"> Guardaflix</label></div>
        <div class="provider-group"><label><input type="checkbox" id="animeworld"> Animeworld</label></div>
        <div class="provider-group"><label><input type="checkbox" id="guardaserie"> Guardaserie</label></div>
        <div class="provider-group"><label><input type="checkbox" id="guardahd"> GuardaHD</label></div>
        <div class="provider-group"><label><input type="checkbox" id="cb01"> CB01 🕵️‍♂️</label></div>

        <div class="provider-group">
            <label>
                <input type="checkbox" id="streamingcommunity"> StreamingCommunity 🕵️‍♂️
                <input type="checkbox" id="streamingcommunity_mfp" checked> 🕵️‍♂️
            </label>
        </div>

        <div class="provider-group"><label><input type="checkbox" id="eurostreaming"> Eurostreaming 🕵️‍♂️</label></div>
        <div class="provider-group"><label><input type="checkbox" id="realtime"> Realtime</label></div>
        <div class="provider-group"><label><input type="checkbox" id="livetv"> LiveTV</label></div>

        <div class="provider-group">
            <label><input type="checkbox" id="mediaflowproxy"> MediaFlow Proxy</label>
            <button type="button" id="mediaFlowProxyButton">Insert Proxy Info</button>
        </div>

        <div id="mediaFlowProxyInputContainer" style="display:none;">
            <input type="text" id="mediaFlowProxyInput" placeholder="Proxy URL">
        </div>

        <div id="mediaFlowProxyPasswordContainer" style="display:none;">
            <input type="password" id="mediaFlowProxyPassword" placeholder="Insert Password">
        </div>

    </form>

    <button id="generateManifestButton">Generate Manifest</button>
    <div id="manifestBox"></div>
    <button id="installButton">Install in Stremio</button>

</div>

<script>
document.getElementById('mediaFlowProxyButton').addEventListener('click', () => {
    const i = document.getElementById('mediaFlowProxyInputContainer');
    const p = document.getElementById('mediaFlowProxyPasswordContainer');
    i.style.display = i.style.display === 'none' ? 'block' : 'none';
    p.style.display = p.style.display === 'none' ? 'block' : 'none';
});

function generateManifest() {
    let manifest = "|";
    const providers = {
        streamingcommunity: "SC",
        streamingwatch: "SW",
        animeworld: "AW",
        livetv: "LIVETV",
        cb01: "CB",
        guardaserie: "GS",
        guardahd: "GHD",
        guardoserie: "GO",
        guardaflix: "GF",
        eurostreaming: "ES",
        realtime: "RT",
        streamingcommunity_mfp: "SC_MFP",
        mediaflowproxy: "MFP"
    };

    for (const id in providers) {
        const el = document.getElementById(id);
        if (el && el.checked) {
            if (id === "mediaflowproxy") {
                const url = mediaFlowProxyInput.value.trim();
                const pass = mediaFlowProxyPassword.value.trim();
                manifest += url && pass ? `MFP[${url},${pass}]|` : "MFP|";
            } else {
                manifest += providers[id] + "|";
            }
        }
    }

    const encoded = btoa(manifest);
    const instanceUrl = "{instance_url}";
    return instanceUrl + "/" + encoded + "/manifest.json";
}

document.getElementById('generateManifestButton').onclick = () => {
    const box = document.getElementById('manifestBox');
    box.style.display = 'block';
    box.innerText = generateManifest();
};

document.getElementById('installButton').onclick = () => {
    let url = generateManifest().replace(/^https?:\\/\\//, '');
    window.location.href = "stremio://" + url;
};
</script>

</body>
</html>
"""
