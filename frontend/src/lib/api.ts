const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function listRuns() {
  const res = await fetch(`${API_URL}/runs`);
  if (!res.ok) throw new Error('Failed to fetch runs');
  return res.json();
}

export async function createAgent(agent: { name: string; config: any }) {
  const res = await fetch(`${API_URL}/agents`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(agent),
  });
  if (!res.ok) throw new Error('Failed to create agent');
  return res.json();
}

export async function getHealth() {
  const res = await fetch(`${API_URL}/health`);
  if (!res.ok) throw new Error('Health check failed');
  return res.json();
}
