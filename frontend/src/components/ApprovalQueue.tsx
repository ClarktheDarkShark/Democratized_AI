import { useEffect, useState } from 'react';
import { decideApproval, listApprovals } from '../lib/api';

export default function ApprovalQueue() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => {
    listApprovals().then(setItems).catch(console.error);
  }, []);

  const act = async (id: number, decision: string) => {
    await decideApproval(id, decision);
    setItems(items.filter((i) => i.id !== id));
  };

  return (
    <ul>
      {items.map((a) => (
        <li key={a.id}>
          Run {a.run_id} - {a.status}
          <button onClick={() => act(a.id, 'approved')}>Approve</button>
          <button onClick={() => act(a.id, 'rejected')}>Reject</button>
        </li>
      ))}
    </ul>
  );
}
