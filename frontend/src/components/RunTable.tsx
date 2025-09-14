import { useEffect, useState } from 'react';
import { listRuns } from '../lib/api';

export default function RunTable() {
  const [runs, setRuns] = useState<any[]>([]);
  useEffect(() => {
    listRuns().then(setRuns).catch(console.error);
  }, []);
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {runs.map((r) => (
          <tr key={r.id}>
            <td>{r.id}</td>
            <td>{r.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
