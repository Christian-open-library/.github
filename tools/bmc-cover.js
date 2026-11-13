// Buy Me a Coffee cover and X (Twitter) header: no text (the page shows the name and the avatar covers the middle),
// just the faint Hebrew and Greek letters and the gold bar, so any crop looks right.
//   NODE_PATH=~/Projects/node_modules node tools/bmc-cover.js
const { chromium } = require('playwright');
const path = require('path');
const LETTERS = [...'הקΣΛבνμשביטרμηυκζדשיγחΒכפטכλαגεδνπחβקΣ'];
const letters = n => Array.from({ length: n }, (_, i) => `<span>${LETTERS[(i * 7 + 3) % LETTERS.length]}</span>`).join('');
const page = (w, h) => `<style>html,body{margin:0}
.h { width: ${w}px; height: ${h}px; background: #f4f4f1; position: relative; overflow: hidden; }
.l { position: absolute; inset: 0; display: grid; grid-template-columns: repeat(${Math.ceil(w / 50)}, 50px); grid-auto-rows: 46px; padding: 16px 0 0 0;
     font: 28px 'DejaVu Serif', Georgia, serif; color: #c9a45c; opacity: .4; }
.l span { text-align: center; }
.bar { position: absolute; left: 0; right: 0; bottom: 0; height: 12px; background: #e2bc62; }
</style><div class="h"><div class="l">${letters(Math.ceil(w / 50) * Math.floor((h - 20) / 46))}</div><div class="bar"></div></div>`;
(async () => {
  const b = await chromium.launch();
  for (const [w, h, f] of [[1600, 400, 'bmc-cover.png'], [1500, 500, 'x-header.png']]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await p.setContent(page(w, h));
    await p.screenshot({ path: path.resolve(__dirname, '..', 'profile/social', f) }); await p.close();
  }
  await b.close(); console.log('drawn');
})();
