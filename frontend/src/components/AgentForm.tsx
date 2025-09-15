import { useState } from 'react';
import { createAgent } from '../lib/api';

export default function AgentForm() {
  const [name, setName] = useState('');
  const [config, setConfig] = useState('{}');

  const submit = async () => {
    try {
      await createAgent({ name, config: JSON.parse(config) });
      setName('');
      setConfig('{}');
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="name"
        title="Enter a unique agent name"
      />
      <textarea
        value={config}
        onChange={(e) => setConfig(e.target.value)}
        title="Provide JSON configuration for the agent"
      />
      <button onClick={submit} title="Submit the agent configuration">Create</button>
    </div>
  );
}
