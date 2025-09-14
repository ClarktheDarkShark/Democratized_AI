import { test, expect } from '@playwright/test';

test('index', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await expect(page.locator('h1')).toContainText('Dashboard');
});
