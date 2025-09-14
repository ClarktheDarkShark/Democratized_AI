import { render, screen } from '@testing-library/react';
import IndexPage from '../src/pages/index';

test('renders dashboard', () => {
  render(<IndexPage />);
  expect(screen.getByText('Dashboard')).toBeInTheDocument();
});
