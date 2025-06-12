const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  // 2.1 Launch chromium in non-headless mode with persistent user data directory
  const userDataDir = path.join(__dirname, 'artifacts', 'chrome-profile');
  const context = await chromium.launchPersistentContext(userDataDir, { headless: false });
  const page = await context.newPage();

  // 2.2 Enable Playwright tracing with screenshots and snapshots
  await context.tracing.start({ screenshots: true, snapshots: true });

  // 2.3 Register page.route interceptor for Gemini XHR/SSE streams
  await page.route('**/*', async (route, request) => {
    const url = request.url();
    if (url.includes('gemini') && (url.includes('xhr') || url.includes('sse'))) {
      const payload = {
        url,
        method: request.method(),
        postData: request.postData(),
        headers: request.headers(),
        timestamp: new Date().toISOString()
      };
      fs.appendFileSync(
        path.join(__dirname, 'artifacts', 'raw_stream.jsonl'),
        JSON.stringify(payload) + '\n'
      );
    }
    route.continue();
  });

  // 2.4 Expose saveArtifact function
  await page.exposeFunction('saveArtifact', async (name, content) => {
    fs.writeFileSync(path.join(__dirname, 'artifacts', name), content);
  });

  // 2.5 Navigate to Gemini chat and wait for prompt input
  await page.goto('https://gemini.google.com/'); // Adjust if needed
  await page.waitForSelector('textarea, [contenteditable]');

  // 2.6 Pass initial project description into Gemini
  await page.type('textarea, [contenteditable]', 'Develop a web-based Tic Tac Toe game. Use modern best practices. Provide clear code and tests.');
  await page.keyboard.press('Enter');

  // Supervision continues as per your protocol...
})(); 