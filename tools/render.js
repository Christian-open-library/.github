// Draw the front page banner, the GitHub avatar and the sign-in page logos from profile/brand/icon.svg,
// in the website's look (Geist, ink and gold). The icon itself comes from the website repo (docs/img/icon.svg).
//   NODE_PATH=~/Projects/node_modules node tools/render.js ~/library-work/website/docs/fonts/geist-latin-wght-normal.woff2
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const P = path.resolve(__dirname, '..', 'profile');
const svg = fs.readFileSync(path.join(P, 'brand/icon.svg'), 'utf8');
const icon = 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');
const square = 'data:image/svg+xml;base64,' + Buffer.from(svg.replace('rx="56"', 'rx="0"')).toString('base64');
const font = 'data:font/woff2;base64,' + fs.readFileSync(process.argv[2]).toString('base64');
const LETTERS = [...'הקΣΛבνμשביטרμηυκζדשיγחΒכפטכλαגεδνπחβקΣ'];
const letters = n => Array.from({ length: n }, (_, i) => `<span>${LETTERS[(i * 7 + 3) % LETTERS.length]}</span>`).join('');
const THEME = {
  light: { bg: '#f4f4f1', ink: '#1a1a1a', muted: '#555555', ring: 'transparent' },
  dark:  { bg: '#1e1f23', ink: '#f7f7f4', muted: '#c2c2bb', ring: '#4d4e55' },
};
const base = `@font-face { font-family: Geist; src: url(${font}) format("woff2"); font-weight: 100 900; }
html, body { margin: 0; background: transparent; } body { font-family: Geist, sans-serif; }`;

const banner = t => `<style>${base}
.b { width: 960px; height: 200px; box-sizing: border-box; background: ${t.bg}; border-radius: 12px; overflow: hidden; position: relative;
     display: flex; align-items: center; gap: 30px; padding: 0 48px; }
.b img { width: 120px; height: 120px; border-radius: 22%; box-shadow: 0 0 0 1.5px ${t.ring}; }
h1 { margin: 0 0 8px; font-size: 44px; line-height: 1.05; font-weight: 700; letter-spacing: -.03em; color: ${t.ink}; }
p { margin: 0; font-size: 17px; color: ${t.muted}; }
.l { position: absolute; top: 0; right: 0; width: 170px; height: 200px; overflow: hidden; display: grid; grid-template-columns: repeat(6, 28px);
     grid-auto-rows: 28px; padding: 10px 0 0 6px; font: 18px 'DejaVu Serif', Georgia, serif; color: #c9a45c; opacity: .55;
     -webkit-mask-image: linear-gradient(to right, transparent, #000 60%), linear-gradient(#000, transparent); -webkit-mask-composite: source-in; }
.l span { text-align: center; }
.bar { position: absolute; left: 0; right: 0; bottom: 0; height: 6px; background: #e2bc62; }
</style><div class="b"><div class="l">${letters(48)}</div><img src="${icon}"><div><h1>Christian Open Library</h1>
<p>Public-domain Christian books, searchable from Claude, ChatGPT or Gemini</p></div><div class="bar"></div></div>`;

const logo = t => `<style>${base}
.b { width: 1260px; height: 320px; display: flex; align-items: center; gap: 40px; padding: 0 32px; box-sizing: border-box; }
.b img { width: 256px; height: 256px; border-radius: 22%; box-shadow: 0 0 0 3px ${t.ring}; } h1 { margin: 0; font-size: 84px; font-weight: 700; letter-spacing: -.03em; color: ${t.ink}; }
</style><div class="b"><img src="${icon}"><h1>Christian Open Library</h1></div>`;

(async () => {
  const b = await chromium.launch();
  const shot = async (html, w, h, file, scale = 1) => {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: scale });
    await p.setContent(html); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(P, file), omitBackground: true }); await p.close();
  };
  const img = (src, n) => `<style>html,body{margin:0;background:transparent}</style><img src="${src}" width="${n}" height="${n}" style="display:block">`;
  for (const k of ['light', 'dark']) {
    await shot(banner(THEME[k]), 960, 200, `banner-${k}.png`, 2);
    await shot(logo(THEME[k]), 1260, 320, `brand/logo-${k}.png`);
  }
  await shot(img(square, 1024), 1024, 1024, 'logo.png');       // GitHub avatar: square, GitHub rounds it
  await shot(img(icon, 512), 512, 512, 'brand/icon.png');
  await shot(img(icon, 48), 48, 48, 'brand/favicon.png');
  await b.close();
  console.log('drawn');
})();
