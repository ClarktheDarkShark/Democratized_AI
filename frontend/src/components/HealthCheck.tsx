import { useState } from 'react';
import { getHealth } from '../lib/api';

export default function HealthCheck() {
  const [status, setStatus] = useState<string | null>(null);

  const check = async () => {
    try {
      const res = await getHealth();
      setStatus(res.status);
    } catch (e) {
      setStatus('error');
    }
  };

  return (
    <div className="card">
      <button onClick={check} title="Verify backend connection">Check API health</button>
      {status && <p>API status: {status}</p>}
    </div>
  );
}
