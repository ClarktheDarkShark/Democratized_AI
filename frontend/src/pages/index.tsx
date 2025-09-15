import Layout from '../components/Layout';
import HealthCheck from '../components/HealthCheck';

export default function IndexPage() {
  return (
    <Layout>
      <h1>Dashboard</h1>
      <HealthCheck />
    </Layout>
  );
}
