// Buy Me a Coffee cover: no text (the page shows the name and the avatar covers the middle),
// just the faint Hebrew and Greek letters and the gold bar, so any crop looks right.
//   NODE_PATH=~/Projects/node_modules node tools/bmc-cover.js
const { chromium } = require('playwright');
const path = require('path');
const LETTERS = [...'הקΣΛבνμשביטרμηυκζדשיγחΒכפטכλαגεδνπחβקΣ'];
const letters = n => Array.from({ length: n }, (_, i) => `<span>${LETTERS[(i * 7 + 3) % LETTERS.length]}</span>`).join('');
const html = `<style>html,body{margin:0}
.h { width: 1600px; height: 400px; background: #f4f4f1; position: relative; overflow: hidden; }
.l { position: absolute; inset: 0; display: grid; grid-template-columns: repeat(32, 50px); grid-auto-rows: 46px; padding: 16px 0 0 0;
     font: 28px 'DejaVu Serif', Georgia, serif; color: #c9a45c; opacity: .4; }
.l span { text-align: center; }
.bar { position: absolute; left: 0; right: 0; bottom: 0; height: 12px; background: #e2bc62; }
</style><div class="h"><div class="l">${letters(32 * 9)}</div><div class="bar"></div></div>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 400 }, deviceScaleFactor: 2 });
  await p.setContent(html);
  await p.screenshot({ path: path.resolve(__dirname, '..', 'profile/social/bmc-cover.png') });
  await b.close(); console.log('drawn');
})();
