import Link from 'next/link';
import { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div>
      <nav>
        <Link href="/">Dashboard</Link> | <Link href="/agents">Agents</Link> | <Link href="/runs">Runs</Link> | <Link href="/approvals">Approvals</Link>
      </nav>
      <main>{children}</main>
    </div>
  );
}
