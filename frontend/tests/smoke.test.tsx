import { render, screen } from '@testing-library/react';
import IndexPage from '../src/pages/index';

test('renders dashboard with health check', () => {
  render(<IndexPage />);
  expect(screen.getByText('Dashboard')).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /check api health/i })).toBeInTheDocument();
});
