module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  testMatch: ['**/tests/**/*.test.tsx'],
  setupFilesAfterEnv: ['@testing-library/jest-dom'],
};
