const fs = require('fs');
const path = require('path');
const assert = require('assert');

const indexPath = path.join(__dirname, '..', 'src', 'pages', 'index.tsx');
const healthPath = path.join(__dirname, '..', 'src', 'components', 'HealthCheck.tsx');
const indexContent = fs.readFileSync(indexPath, 'utf8');
const healthContent = fs.readFileSync(healthPath, 'utf8');

assert(indexContent.includes('Dashboard'), 'Dashboard heading missing');
assert(/Check API health/i.test(healthContent), 'Health check button missing');

console.log('frontend smoke test passed');
